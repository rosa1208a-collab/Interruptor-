from flask import Blueprint, render_template, request, redirect, url_for


def crear_web_controller(servicio, repositorio, dispositivos_db, dispositivo):
    """
    Crea las rutas web del sistema de iluminación.
    """

    web = Blueprint("web", __name__)

    @web.route("/", methods=["GET", "POST"])
    def inicio():

        if request.method == "POST":

            gesto = request.form.get("gesto", "UNKNOWN")

            try:
                confianza = float(
                    request.form.get("confianza", 0.95)
                )

                distancia = float(
                    request.form.get("distancia", 15)
                )

            except (ValueError, TypeError):
                return "Los valores ingresados no son validos", 400

            if not 0 <= confianza <= 1:
                return "La confianza debe estar entre 0 y 1", 400

            if distancia < 0:
                return "La distancia no puede ser negativa", 400

            modo_prueba = (
                request.form.get("modo_prueba") == "on"
            )

            servicio.procesar_interaccion(
                gesto=gesto,
                confianza=confianza,
                distancia=distancia,
                modo_prueba=modo_prueba
            )

            return redirect(url_for("web.inicio"))

        historial = repositorio.consultar_historial()

        dispositivos = dispositivos_db.consultar_dispositivos()

        estado_luz = dispositivo.consultar_estado()

        return render_template(
            "index.html",
            historial=historial,
            dispositivos=dispositivos,
            estado_luz=estado_luz
        )

    @web.route("/registrar_dispositivo", methods=["POST"])
    def registrar_dispositivo():

        nombre = request.form.get("nombre", "").strip()

        zona = request.form.get("zona", "").strip()

        if not nombre or not zona:
            return "Debes ingresar un nombre y una zona", 400

        dispositivos_db.registrar_dispositivo(
            nombre=nombre,
            zona=zona
        )

        return redirect(url_for("web.inicio"))

    return web
