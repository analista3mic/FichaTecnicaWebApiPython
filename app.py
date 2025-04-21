from flask import Flask, render_template, url_for, request
from flask_cors import CORS
import os

from app.routes.ficha import ficha_bp
from app.routes.estampacion import estampacion_bp
from app.routes.validate_reference_ficha_tecnica import validate_reference_ficha_tecnica_bp
from app.routes.validate_reference_estampacion import validate_reference_estampacion_bp

app = Flask(__name__)
CORS(app)  # Habilita CORS

# Registrar blueprints (módulos de rutas)
app.register_blueprint(ficha_bp)
app.register_blueprint(estampacion_bp)
app.register_blueprint(validate_reference_ficha_tecnica_bp)
app.register_blueprint(validate_reference_estampacion_bp)


# Nueva ruta para ficha técnica con rutas absolutas para CSS y Logo
@app.route("/ficha")
def ficha():
    css_url = url_for("static", filename="css/ficha_tecnica.css")
    logo_url = url_for("static", filename="assets/logo-mic.png")

    return render_template("ficha_tecnica.html", css_url=css_url, logo_url=logo_url)


# Ruta de prueba
@app.route("/")
def home():
    return "API funcionando 🚀"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
