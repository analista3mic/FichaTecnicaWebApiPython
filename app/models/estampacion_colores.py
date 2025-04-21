class Estampacion_Colores:
    def __init__(self, data):
        self.idrows = data.get("IdRows")
        self.codigo = data.get("Codigo")
        self.referencia = data.get("Referencia")
        self.nro_arte = data.get("NroArte")
        self.descripcion = data.get("Descripcion")
        self.observacion = data.get("Observacion")
        self.componente = data.get("Componente")
        self.subcolor = data.get("SubColor")
        self.fecha_insercion = data.get("FechaInsercion")

    def to_dict(self):
        return self.__dict__