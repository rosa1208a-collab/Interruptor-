
from sensor.sensor_gateway import SensorGateway
from sensor.gesture_recognizer import GestureRecognizer


sensor = SensorGateway()
reconocedor = GestureRecognizer()

gestos = [
    "SWIPE_RIGHT",
    "SWIPE_LEFT",
    "UNKNOWN"
]

for gesto in gestos:
    evento = sensor.recibir_evento(
        gesto,
        confianza=0.95,
        distancia=15
    )

    evento = sensor.normalizar_evento(evento)

    resultado = reconocedor.reconocer_gesto(evento)

    print(resultado)
