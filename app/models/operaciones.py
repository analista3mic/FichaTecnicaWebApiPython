class Operaciones:
    def __init__(self, data):
        self.idrows = data.get("IdRows")
        self.id_operacion = data.get("IDOperacion")
        self.id_row_ficha_tecnica = data.get("IdRowsFichaTecnica")
        self.referencia = data.get("ReferenciaOp")
        self.numero_operacion = data.get("NumeroOp")
        self.ubicacion = data.get("UbicacionOp")
        self.operacion = data.get("OperacionOp")
        self.usuario_registra = data.get("UsrRegOp")
        self.usuario_modifica = data.get("UsrModOp")
        self.fecha_registro = data.get("FechaRegOp")
        self.fecha_modificacion = data.get("FechaModOp")
        self.fecha_insercion = data.get("FechaInsercion")

    def to_dict(self):
        return self.__dict__