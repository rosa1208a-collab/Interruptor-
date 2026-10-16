from control.rules_engine import RulesEngine

reglas = RulesEngine()

eventos = [
    {
        "gesto": "SWIPE_RIGHT",
        "reconocido": True,
        "confianza": 0.95,
        "distancia": 15
    },
    {
        "gesto": "SWIPE_LEFT",
        "reconocido": True,
        "confianza": 0.95,
        "distancia": 15
    },
    {
        "gesto": "SWIPE_RIGHT",
        "reconocido": True,
        "confianza": 0.60,
        "distancia": 15
    },
    {
        "gesto": "UNKNOWN",
        "reconocido": False,
        "confianza": 0.95,
        "distancia": 15
    }
]

for evento in eventos:
    resultado = reglas.evaluar_gesto(evento)
    print("Evento:", evento["gesto"])
    print("Resultado:", resultado)
    print("-" * 40)
