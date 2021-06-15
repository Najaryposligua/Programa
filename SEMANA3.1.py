# class For:
#     def __init__(self):
#         pass
#
#       #ciclo repetivo de incremento o descremento se ejecuta por verdadero
#     def usoFor(self):
#         datos=["Daniel",50,True]
#         materias = (2,5,6,4,1)
#         docente = {'nombre': 'Daniel', 'edad': 50, 'fac': 'facil'}
#         listaNotas= [(30,40)], [(20,40)],[(50,40)]
#         listaAlumnos = [{"nombre":"Erick","final":70},{"nombre":"Yady","final":60},{"nombre":"Danny","final":90}]
#         #! range ([inicio=0],[inc/dec=1]. Genera un rango de valores desde un valor inicial a un valor final)
#         # * se ejecuta desde inicio hasta el limite
#         for i in range(5):
#             print("i={}".format(i))
# bucle1= For()
# bucle1.usoFor()




class For:
    def __init__(self):
        pass

      #ciclo repetivo de incremento o descremento se ejecuta por verdadero
    def usoFor(self):
        nombre="daniel"
        datos=["Daniel",50,True]
        materias = (2,5,6,4,1)
        docente = {'nombre': 'Daniel', 'edad': 50, 'fac': 'facil'}
        listaNotas= [(30,40)], [(20,40)],[(50,40)]
        listaAlumnos = [{"nombre":"Erick","final":70},{"nombre":"Yady","final":60},{"nombre":"Danny","final":90}]
        #! range ([inicio=0],[inc/dec=1]. Genera un rango de valores desde un valor inicial a un valor final)
        # * se ejecuta desde inicio hasta el limite
        # for i in range(5):
        #     print("i={}".format(i))
        # for i in range(2,10): #rango(2,3,4,5,6,7,8,9)
        #     print("i={}".format(i))
        # for i in range(4,10,2):  # rango(4,6,8)
        #     print("i={}".format(i),end=" ")
        # for i in range(12,3,-3): #rango(12,9,6)
        #     print("i={}".format(i),end="  ")


        # longitud = len(datos)
        # print(datos[0])
        # print(datos[1])
        # print(datos[2])
        # j=0
        # while j< longitud:
        #     print("While ", datos[j])
        #     j=j+1
        # for i in range(longitud-1,-1,-1):
        #     print(("for",datos[i]))

        # for i in range(longitud):
        #     print(datos[i])

        # for i,dato in enumerate(numero):
        #     print("for",i,dato)
            #dato toma elemento por caracter de la coleccion numero (cadena, lista, tupla)
        for dato in nombre:
            print(dato)


bucle1= For()
bucle1.usoFor()