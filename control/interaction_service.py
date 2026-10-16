class InteractionService:
    """
    Coordina la recepción, el reconocimiento,
    la validación y la ejecución de los gestos.
    """

    def __init__(
        self,
        sensor,
        reconocedor,
        reglas,
        dispositivo,
        repositorio=None
    ):
        self.sensor = sensor
        self.reconocedor = reconocedor
        self.reglas = reglas
        self.dispositivo = dispositivo
        self.repositorio = repositorio

    def procesar_interaccion(
        self,
        gesto,
        confianza=0.95,
        distancia=15,
        modo_prueba=False
    ):
        # 1. Recibir el evento del sensor.
        evento = self.sensor.recibir_evento(
            gesto,
            confianza=confianza,
            distancia=distancia
        )

        # 2. Normalizar los datos recibidos.
        evento = self.sensor.normalizar_evento(evento)

        # 3. Reconocer el gesto.
        reconocimiento = self.reconocedor.reconocer_gesto(
            evento
        )

        # 4. Validar el gesto.
        decision = self.reglas.evaluar_gesto(
            reconocimiento
        )

        # 5. Consultar el estado anterior.
        estado_anterior = self.dispositivo.consultar_estado()

        # 6. Ejecutar la orden solo si el gesto es válido
        # y no estamos en modo de prueba.
        if decision["aceptado"] and not modo_prueba:
            resultado_dispositivo = self.dispositivo.enviar_orden(
                decision["accion"]
            )

            estado_luz = resultado_dispositivo["estado_luz"]

        else:
            estado_luz = estado_anterior

        # 7. Explicar qué sucedió en el modo de prueba.
        if decision["aceptado"] and modo_prueba:
            decision = {
                **decision,
                "motivo": (
                    "Gesto valido; modo de prueba, "
                    "no se ejecuto la accion"
                )
            }

        # 8. Preparar el resultado.
        resultado = {
            "gesto": reconocimiento["gesto"],
            "aceptado": decision["aceptado"],
            "motivo": decision["motivo"],
            "accion": decision["accion"],
            "modo_prueba": modo_prueba,
            "confianza": reconocimiento["confianza"],
            "distancia": reconocimiento["distancia"],
            "estado_luz": estado_luz,
            "fecha": evento["fecha"]
        }

        # 9. Guardar el resultado si se proporcionó
        # un repositorio compatible.
        if self.repositorio is not None:
            self.repositorio.guardar_evento(resultado)

        return resultado
