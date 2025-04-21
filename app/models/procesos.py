class Procesos:
    def __init__(self, data):
        self.idrows = data.get("IdRows")
        self.id_componente_prenda = data.get("IdComponentePrenda")
        self.referencia = data.get("ReferenciaFTec")
        self.nombre = data.get("Nombre")
        self.procesos = data.get("ProcesosFTec")
        self.observacion = data.get("Observacion")
        self.fecha_insercion = data.get("FechaInsercion")

    def to_dict(self):
        return self.__dict__