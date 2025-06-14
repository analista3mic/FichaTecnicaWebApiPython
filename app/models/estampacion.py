class Estampacion:
    def __init__(self, data):
        self.idrows = data.get("IdRows")
        self.id_estampacion = data.get("IdEstampacion")
        self.nro_arte = data.get("NroArteEstamp")
        self.nro_colores = data.get("NroColoresEstamp")
        self.referencia = data.get("Referencia")
        self.fecha = data.get("FechaRefEstamp")
        self.ancho = data.get("AnchoEstamp")
        self.largo = data.get("LargoEstamp")
        self.ubicacion = data.get("UbicacionEstamp")
        self.aprob_lic = data.get("AprobLicEstamp")
        self.tono_tela = data.get("TonoTelaEstamp")
        self.observacion = data.get("ObservacionEstamp")
        self.descripcion_ubica = data.get("DescripUbicaEstamp")
        self.colores_estamp = data.get("ColoresEstamp1")
        self.nombre_tipo = data.get("NombreTipo")
        self.nombre_comp = data.get("NombreComp")
        self.descripcion_telas = data.get("DescripcionTelas")
        self.descripcion_colores = data.get("DescripcionColores")
        self.tecnica_pri = data.get("TecnicaPri")
        self.tecnica_sec = data.get("TecnicaSec")
        self.maquina = data.get("Maquina")
        self.sam = data.get("SAM")
        self.ruta_imagen = data.get("RutaImagen")
        self.imagen = data.get("Imagen")
        self.id_row_digital_ocean = data.get("IdRowDigitalOcean")
        self.fecha_insercion = data.get("FechaInsercion")

    def to_dict(self):
        return self.__dict__