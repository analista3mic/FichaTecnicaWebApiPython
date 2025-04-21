
import base64
from flask import Blueprint, request, jsonify, render_template_string, current_app, url_for
from app.models.ficha_tecnica import FichaTecnica
from app.models.procesos import Procesos
from app.models.operaciones import Operaciones
from app.services.pdf_utils import link_callback
from app.services.pdf_utils import html_to_pdf
from app.services.get_ficha_tecnica import get_ficha_tecnica
from app.services.get_operaciones import get_operaciones
from app.services.get_procesos import get_procesos, agrupar_procesos_por_componente

ficha_bp = Blueprint('ficha', __name__)


def render_ficha_tecnica_pdf(ficha_data, procesos_data, operaciones_data):
    """Renderiza el HTML con los datos, genera el PDF en base64 y lo retorna junto con los datos."""
    ficha_obj = [FichaTecnica(item) for item in ficha_data]
    procesos_obj = [Procesos(item) for item in procesos_data]
    operaciones_obj = [Operaciones(item) for item in operaciones_data]
    procesos_agrupados = agrupar_procesos_por_componente(procesos_obj)

    # Leer plantilla HTML
    html_path = "templates/ficha_tecnica.html"
    try:
        with open(html_path, "r", encoding="utf-8") as file:
            html_template = file.read()
    except FileNotFoundError:
        return None, None, "Archivo HTML no encontrado", 500
    except Exception as e:
        return None, None, f"No se pudo leer el archivo HTML: {str(e)}", 500

    # URLs para recursos estáticos
    css_url = url_for("static", filename="css/ficha_tecnica.css")
    logo_url = url_for("static", filename="assets/logo-mic.png")

    # Renderizar HTML con Jinja
    html_content = render_template_string(html_template, css_url=css_url, logo_url=logo_url, ficha_obj=ficha_obj, procesos_obj=procesos_agrupados, operaciones_obj=operaciones_obj)

    # Convertir HTML a PDF
    pdf_bytes, error = html_to_pdf(html_content, link_callback=link_callback)
    if error:
        return None, None, error, 500

    # Convertir PDF a Base64
    try:
        pdf_base64 = base64.b64encode(pdf_bytes).decode("utf-8")
    except Exception as e:
        return None, None, f"No se pudo convertir PDF a Base64: {str(e)}", 500

    return ficha_data, procesos_data, operaciones_data, pdf_base64, None, 200


@ficha_bp.route("/GetFichaTecnica", methods=["GET"])
def generate_ficha_tecnica_pdf():
    """Endpoint principal: consulta MySQL, genera PDF y responde a Angular."""
    referencia = request.args.get("reference")
    if not referencia:
        return jsonify({"error": "Falta el parámetro de referencia"}), 400

    # Obtener datos desde la DB Ficha Tecnica
    ficha_data, error_response, status = get_ficha_tecnica(referencia)
    if error_response:
        return jsonify(error_response), status
    
    # Obtener datos desde la DB Ficha Tecnica
    procesos, error_response, status = get_procesos(referencia)
    if error_response:
        return jsonify(error_response), status
    
    operaciones, error_response, status = get_operaciones(referencia)
    if error_response:
        return jsonify(error_response), status

    # Generar PDF
    ficha_data, procesos_data, operaciones_data, pdf_base64, error_message, status = render_ficha_tecnica_pdf(ficha_data, procesos, operaciones)
    if error_message:
        return jsonify({"error": error_message}), status

    return jsonify({
        "Ficha Data": ficha_data,
        "Procesos Data": procesos_data,
        "Operaciones Data": operaciones_data,
        "pdf_base64": pdf_base64
    })
