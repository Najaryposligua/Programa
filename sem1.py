print("Ejercicios diapositiva 1")
#NUMERICOS
edad, _peso= 50, 70.5

#STRING
nombres='Najary Posligua   '
dirDomiciliaria ="Guasmo Sur"
Tipo_sexo="F"

#BOOLEAN
civil=True

#COLECCIONES
usuario=('dchiki','1234','chiki@gmail.com')
materias=['Programacion Web','PHP','POO']
docente={'nombre':'Daniel','edad':50,'fac':'facil'}
print("""Mi nombre es {}, tengo {}
años""".format(nombres,edad))
print(usuario,materias,docente)
print()
print("--------------------------------------------------")
print("Ejercicios diapositiva 2")
#USO DEL IF
x=int(input("Ingresar un numero entero: "))
if x<0:
    x=0
    print("Negativo cambiado a cero")
elif x==0:
    print("Cero")
elif x==1:
    print('Uno')
else:
    print('Ninguna opcion')
print(("OK") if type(x)==int else print("."))

print()
print("--------------------------------------------------")
print("Ejercicios diapositiva 3")
#CICLO WHILE INFINIFITO
## c=1
## while True:
##     print(c)

#CICLO WHILE VALIDACION
vocal =input("Ingrese vocal:")
while vocal not in("a","e","i","o","u"):
    if vocal==".":
        break
    vocal=input("Vocal:")
print('Su vocal o punto es:{} '.format((vocal)))

print()
print("--------------------------------------------------")
print("Ejercicios diapositiva 4")
#CICLOS FOR range
frase=input("Ingrese frase: ")
###for indice in range(len(frase)):
###    print(indice,'=',frase[indice])
cvoc=0
for car in frase:
    if car in ("a","e","i","o","u","A","E","I","O","U"):
        if car in ("A","E","I","O","U"):
            continue
        else:
            cvoc=cvoc+1
print('cantidad de vocales:{}'.format(cvoc))

#Comprehension
[car for car in ['a','e','i','o','u']if car not in('a','i','o')]
print()
print("--------------------------------------------------")
print("Ejercicios diapositiva 5")
#funciones sin retorno
def vocales(frase):
    for car in frase:
        if car in ("a","e","i","o","u"):
            print(car)

oracion=input("Ingrese oracion: ")
vocales(oracion.lower())

#funcion con retorno valor
print()
def promedio(notas):
    summ=0
    for n in notas:
        summ+=n
    return summ/len(notas)
listanotas=[2,4,6,8,10]
prom=promedio(listanotas)
print("promedio:{}={}".format(listanotas,prom))

print()
print("--------------------------------------------------")
print("Ejercicios diapositiva 6")
#FUNCIONES MATEMATICAS
import math
num1,num2,num,men=12.572,15.4,4,'1234'
print(math.ceil(num1),"\t",math.floor(num1))
print(round(num1,1),"\t",type(num),"\t",type(men))

#FUNCIONES DE CADENAS
print()
mensaje='Hola' + 'mundo' + 'Python'
men1=mensaje.split()
men2=''.join(men1)
print(mensaje[0],mensaje[0:4],men1,men2)
print(mensaje.find("mundo"),mensaje.lower())

#FUNCIONES DE FECHAS
print()
from datetime import datetime,timedelta,date
hoy,fdia=datetime.now(),date.today()
futuro=hoy+timedelta(days=30)
dif,aa,mm,dd=futuro-hoy, hoy.year, hoy.month, hoy.day
fecha= date(aa,mm,dd+2)
print(hoy,fdia,futuro,dif,fecha)