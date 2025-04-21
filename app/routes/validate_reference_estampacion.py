from flask import Blueprint, request, jsonify
from app.services.db import execute_stored_procedure

validate_reference_estampacion_bp = Blueprint('validate_reference_estampacion', __name__)

@validate_reference_estampacion_bp.route("/GetValidateReferenceEstampacion", methods=["GET"])
def get_validate_reference_estampacion():
    referencia = request.args.get("reference")

    if not referencia:
        return jsonify({"error": "Falta el parámetro de referencia"}), 400

    result = execute_stored_procedure("SP_GetValidateReferenceEstampacion", (referencia,))
    return jsonify(result)
