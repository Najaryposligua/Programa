# num="20"
# if type(num) ==str:
#     print("El dato no es numerico")
# else:
#     print("Respuesta: ", num*2)

# def mensaje(men):
#     print(men)

# mensaje("mi primer programa")
# mensaje("Mi segundo programa")

#--------------------------------------------------------
# class Sintaxis:
#     def userVariable(self):
#         edad, _peso= 50, 70.50
#         print(edad, _peso)

# ejer1= Sintaxis()
# ejer1.userVariable()
#---------------------------------------------------------
class Sintaxis:
    instancia=0 #variable de clases
    #_init_ metodo constructor qe se ejecuta cuando se instancia la clase cuyo objetivo es crear
    #inicializar los atributos de la clase. Slef es un objeto que represenya la clase creada
    def _init_(self,dato="Inicializacion"):
        self.frase=dato #Variable de instancia
        #Sintaxis.instancia=sintaxis.instancia+1
    
    def userVariable(self):
        edad, _peso= 30, 68,50
        nombres="Bairon Reyes"
        Tipo_sexo="M"
        civil=True
        #Tuplas =() son colecciones de datos de cualquier tipo inmutables
        
        usuario=()
        usuario=("Breyes",7986,'bareca90@gmail.com',True)
        #usuario[3]=milagro
        #listas=[] colecciones mutables
        materias=[]
        materias=['Programacion Web','PHP','POO']
        materias[1]="python"
        materias.append("Go")
        #diccionario ={} colecciones de objetos clave:valor tipo jsen

        print(nombres,edad)

ejer1=Sintaxis() #se crea un objeto que es una instancia de la clase
ejer1.userVariable()