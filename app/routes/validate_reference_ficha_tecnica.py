from flask import Blueprint, request, jsonify
from app.services.db import execute_stored_procedure

validate_reference_ficha_tecnica_bp = Blueprint('validate_reference_ficha_tecnica', __name__)

@validate_reference_ficha_tecnica_bp.route("/GetValidateReferenceFichaTecnica", methods=["GET"])
def get_validate_reference_ficha_tecnica():
    referencia = request.args.get("reference")

    if not referencia:
        return jsonify({"error": "Falta el parámetro de referencia"}), 400

    result = execute_stored_procedure("SP_GetValidateReferenceFichaTecnica", (referencia,))
    return jsonify(result)
