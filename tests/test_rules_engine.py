import unittest

from control.rules_engine import RulesEngine


class TestRulesEngine(unittest.TestCase):

    def setUp(self):
        self.reglas = RulesEngine()

    def test_acepta_gesto_derecha(self):
        evento = {
            "gesto": "SWIPE_RIGHT",
            "reconocido": True,
            "confianza": 0.95,
            "distancia": 15
        }

        resultado = self.reglas.evaluar_gesto(evento)

        self.assertTrue(resultado["aceptado"])
        self.assertEqual(resultado["accion"], "ENCENDER")

    def test_acepta_gesto_izquierda(self):
        evento = {
            "gesto": "SWIPE_LEFT",
            "reconocido": True,
            "confianza": 0.95,
            "distancia": 15
        }

        resultado = self.reglas.evaluar_gesto(evento)

        self.assertTrue(resultado["aceptado"])
        self.assertEqual(resultado["accion"], "APAGAR")

    def test_rechaza_baja_confianza(self):
        evento = {
            "gesto": "SWIPE_RIGHT",
            "reconocido": True,
            "confianza": 0.60,
            "distancia": 15
        }

        resultado = self.reglas.evaluar_gesto(evento)

        self.assertFalse(resultado["aceptado"])
        self.assertIsNone(resultado["accion"])

    def test_rechaza_distancia_fuera_de_rango(self):
        evento = {
            "gesto": "SWIPE_RIGHT",
            "reconocido": True,
            "confianza": 0.95,
            "distancia": 70
        }

        resultado = self.reglas.evaluar_gesto(evento)

        self.assertFalse(resultado["aceptado"])

    def test_rechaza_gesto_desconocido(self):
        evento = {
            "gesto": "UNKNOWN",
            "reconocido": False,
            "confianza": 0.95,
            "distancia": 15
        }

        resultado = self.reglas.evaluar_gesto(evento)

        self.assertFalse(resultado["aceptado"])


if __name__ == "__main__":
    unittest.main()
