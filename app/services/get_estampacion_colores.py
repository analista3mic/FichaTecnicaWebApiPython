from app.services.db import execute_stored_procedure
from collections import defaultdict

def get_estampacion_colores(reference):
    """Consulta la base de datos y devuelve los datos crudos."""
    result = execute_stored_procedure("SP_GetEstampacionColoresInfo", (reference,))
    
    if not result or not isinstance(result, list) or len(result) == 0:
        return None, {"error": "No se encontró información para la referencia"}, 404

    return result, None, 200

def agrupar_colores_nro_arte(estampacion_colores_obj):
    agrupados = defaultdict(list)
    for item in estampacion_colores_obj:
        agrupados[item.nro_arte].append(item)
    return dict(agrupados)