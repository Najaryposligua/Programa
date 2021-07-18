class Persona:
    _sigue=0
    def __init__(self,nombre="Invitado",activo=True):
        #Persona._sigue=Persona._sigue+1
        #Persona._sigue=self.sigue()
        self.__codigo=self.sigue()
        self.__nombre=self.__nombreMayus(nombre)
        self.activo=activo

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nom):
        self.__nombre=nom

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, cod):
        self.__codigo = cod

    def sigue(self):
        Persona._sigue=Persona._sigue+1
        return Persona._sigue

    def __nombreMayus(self,nom):
        return nom.upper()

    def mostrar_datos(self):
        return "Codigo: {} - Nombre: {} - Activo: {}".format(self.codigo,self.nombre, self.activo)

class Empleado(Persona):
    def __init__(self,nom="Inivtado", act=True, sueldo=450):
        Persona.__init__(self,nom,act)
        self.sueldo=sueldo

    def mostrar_datos(self):
        return Persona.mostrar_datos(self)+"Sueldo: "+ str(self.sueldo)

# per1=Persona()
# print(per1.mostrar_datos())
# per2=Persona("Ashley",False)
# print(per2.mostrar_datos())