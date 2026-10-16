
class GestureRecognizer:

    def reconocer_gesto(self, evento):
        """Identifica los gestos que reconoce el sistema."""

        gesto = evento.get(
            "gesto_detectado", "UNKNOWN"
        ).upper()

        gestos_validos = [
            "SWIPE_RIGHT",
            "SWIPE_LEFT"
        ]

        return {
            "gesto": gesto,
            "reconocido": gesto in gestos_validos,
            "confianza": evento.get("confianza", 0),
            "distancia": evento.get("distancia", 0)
        }
