class Cliente:
    def __init__(self, ced,nom,dir,tel):
        self.cedula=ced
        self.nombre=nom
        self.direccion=dir
        self.telefono=tel
        
        
class Venta:
    def __init__(self,fac,fec,cliente,total,detalleven):
        self.factura=fac
        self.fecha=fec
        self.cliente=cliente
        self.total=total
        self.detalleven=detalleven
        
class VentaDet:
    def __init__(self,articulo,precio,cantidad):
        self.articulo=articulo
        self.precio=precio
        self.cantidad=cantidad
