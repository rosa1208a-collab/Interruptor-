from sensor.sensor_gateway import SensorGateway
from sensor.gesture_recognizer import GestureRecognizer

from control.rules_engine import RulesEngine
from control.device_adapter import DeviceAdapter
from control.interaction_service import InteractionService


# Crear los componentes.
sensor = SensorGateway()
reconocedor = GestureRecognizer()
reglas = RulesEngine()
dispositivo = DeviceAdapter()

# Crear el servicio.
servicio = InteractionService(
    sensor=sensor,
    reconocedor=reconocedor,
    reglas=reglas,
    dispositivo=dispositivo
)

# Prueba 1: encender la luz.
print("PRUEBA 1: ENCENDER")

resultado = servicio.procesar_interaccion(
    gesto="SWIPE_RIGHT"
)

print(resultado)
print("Estado actual:", dispositivo.consultar_estado())


# Prueba 2: apagar la luz.
print("\nPRUEBA 2: APAGAR")

resultado = servicio.procesar_interaccion(
    gesto="SWIPE_LEFT"
)

print(resultado)
print("Estado actual:", dispositivo.consultar_estado())


# Prueba 3: rechazar un gesto con poca confianza.
print("\nPRUEBA 3: CONFIANZA INSUFICIENTE")

resultado = servicio.procesar_interaccion(
    gesto="SWIPE_RIGHT",
    confianza=0.60
)

print(resultado)
print("Estado actual:", dispositivo.consultar_estado())


# Prueba 4: modo de prueba.
print("\nPRUEBA 4: MODO DE PRUEBA")

resultado = servicio.procesar_interaccion(
    gesto="SWIPE_RIGHT",
    modo_prueba=True
)

print(resultado)
print("Estado actual:", dispositivo.consultar_estado())
