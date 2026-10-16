from datetime import datetime


class SensorGateway:

    def recibir_evento(self, gesto, confianza=0.95, distancia=15):
        """Simula un evento recibido desde el sensor."""

        evento = {
            "gesto_detectado": gesto,
            "confianza": confianza,
            "distancia": distancia,
            "fecha": datetime.now().isoformat()
        }

        return evento

    def normalizar_evento(self, evento):
        """Organiza los datos en un formato uniforme."""

        return {
            "gesto_detectado": str(
                evento.get("gesto_detectado", "UNKNOWN")
            ).upper(),
            "confianza": float(evento.get("confianza", 0)),
            "distancia": float(evento.get("distancia", 0)),
            "fecha": evento.get(
                "fecha",
                datetime.now().isoformat()
            )
        }
