class DeviceAdapter:
    """
    Simula el dispositivo encargado de controlar la luz.
    """

    def __init__(self):
        self.estado_luz = "APAGADA"

    def enviar_orden(self, accion):
        """
        Recibe una orden y actualiza el estado de la luz.
        """

        if accion == "ENCENDER":
            self.estado_luz = "ENCENDIDA"

        elif accion == "APAGAR":
            self.estado_luz = "APAGADA"

        else:
            raise ValueError(
                f"Accion no valida: {accion}"
            )

        return {
            "accion": accion,
            "estado_luz": self.estado_luz
        }

    def consultar_estado(self):
        return self.estado_luz
