from app.services.db import execute_stored_procedure

def get_ficha_tecnica(reference):
    """Consulta la base de datos y devuelve los datos crudos."""
    result = execute_stored_procedure("SP_GetFichaTecnica", (reference,))
    
    if not result or not isinstance(result, list) or len(result) == 0:
        return None, {"error": "No se encontró información para la referencia"}, 404

    return result, None, 200