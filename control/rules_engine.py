class RulesEngine:
    """
    Valida los gestos reconocidos y determina
    qué acción puede ejecutar el sistema.
    """

    def evaluar_gesto(self, evento):
        gesto = evento.get("gesto", "UNKNOWN")
        reconocido = evento.get("reconocido", False)
        confianza = evento.get("confianza", 0)
        distancia = evento.get("distancia", 0)

        # Regla 1: el gesto debe haber sido reconocido.
        if not reconocido:
            return {
                "aceptado": False,
                "motivo": "El gesto no fue reconocido",
                "accion": None
            }

        # Regla 2: la confianza debe ser de al menos 0.80.
        if confianza < 0.80:
            return {
                "aceptado": False,
                "motivo": "Confianza de deteccion insuficiente",
                "accion": None
            }

        # Regla 3: la distancia debe estar entre 2 y 50 cm.
        if not 2 <= distancia <= 50:
            return {
                "aceptado": False,
                "motivo": "La distancia esta fuera del rango permitido",
                "accion": None
            }

        # Regla 4: asociar cada gesto con una acción.
        if gesto == "SWIPE_RIGHT":
            accion = "ENCENDER"

        elif gesto == "SWIPE_LEFT":
            accion = "APAGAR"

        else:
            return {
                "aceptado": False,
                "motivo": "No existe una accion asociada al gesto",
                "accion": None
            }

        # Si todas las reglas se cumplen, aceptar el gesto.
        return {
            "aceptado": True,
            "motivo": "Gesto valido",
            "accion": accion
        }
