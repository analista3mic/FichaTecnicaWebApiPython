from app.services.db import execute_stored_procedure
from collections import defaultdict

def get_procesos(reference):
    """Consulta la base de datos y devuelve los datos crudos."""
    result = execute_stored_procedure("SP_GetProcesos", (reference,))
    
    if not result or not isinstance(result, list) or len(result) == 0:
        return None, {"error": "No se encontró información para la referencia"}, 404

    return result, None, 200

def agrupar_procesos_por_componente(procesos_obj):
    agrupado = defaultdict(lambda: {"procesos": [], "observacion": ""})
    for p in procesos_obj:
        agrupado[p.nombre]["procesos"].append(p.procesos)
        if not agrupado[p.nombre]["observacion"]:
            agrupado[p.nombre]["observacion"] = p.observacion or ""
    return [{"nombre": k, "procesos": v["procesos"], "observacion": v["observacion"]} for k, v in agrupado.items()]