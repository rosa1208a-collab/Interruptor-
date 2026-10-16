from flask import Flask

# Modulos de Rosa
from sensor.sensor_gateway import SensorGateway
from sensor.gesture_recognizer import GestureRecognizer

# Modulos de Pamela
from control.rules_engine import RulesEngine
from control.device_adapter import DeviceAdapter
from control.interaction_service import InteractionService

# Modulos de Angel
from database.event_repository import EventRepository
from database.device_repository import DeviceRepository
from web.web_controller import crear_web_controller


def crear_app():

    # Crear la aplicacion Flask
    app = Flask(__name__)

    # Inicializar el sensor y el reconocimiento
    sensor = SensorGateway()
    reconocedor = GestureRecognizer()

    # Inicializar las reglas y el dispositivo
    reglas = RulesEngine()
    dispositivo = DeviceAdapter()

    # Inicializar la base de datos
    repositorio = EventRepository()
    dispositivos_db = DeviceRepository()

    # Crear el servicio de interacciones
    servicio = InteractionService(
        sensor,
        reconocedor,
        reglas,
        dispositivo,
        repositorio
    )

    # Registrar las rutas web
    web_controller = crear_web_controller(
        servicio,
        repositorio,
        dispositivos_db,
        dispositivo
    )

    app.register_blueprint(web_controller)

    return app


app = crear_app()


if __name__ == "__main__":
    app.run(debug=True)
