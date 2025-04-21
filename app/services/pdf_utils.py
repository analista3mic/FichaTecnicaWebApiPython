import os
import io
from flask import current_app
from xhtml2pdf import pisa

def link_callback(uri, rel):
    """
    Callback para permitir a pisa acceder a los recursos locales.
    Convierte rutas relativas (como /static/img.png) en rutas absolutas para PDF.
    """
    path = os.path.join(current_app.root_path, 'static', uri.replace(current_app.static_url_path + '/', ''))
    if os.path.exists(path):
        return path
    return uri

def html_to_pdf(html_content, link_callback=None):
    """Convierte HTML en PDF y lo retorna en bytes."""
    try:
        pdf_buffer = io.BytesIO()
        pisa_status = pisa.CreatePDF(
            io.StringIO(html_content),
            dest=pdf_buffer,
            link_callback=link_callback
        )

        if pisa_status.err:
            return None, "Error al convertir HTML a PDF"

        pdf_buffer.seek(0)
        return pdf_buffer.read(), None
    except Exception as e:
        return None, f"Excepción generando PDF: {str(e)}"