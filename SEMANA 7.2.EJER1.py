class For:
    def __init__(self):
        pass

    #ciclo repetitivo de incrementos o decrementos se ejecuta por verdadero
    def usoFor(self):
        datos=["Ashley",21,True]
        numeross=(2,5.6,4,1)
        docente={"nombre":"Ashley", "edad":21,"fac":"facil"}
        listanotas=[(30,40),(20,40),(50,40)]
        #range([inicio=0],limite,[incremento/decremento]. Genera un rang de valores desde un valor inicial a un valor dinal
        #se ejecuta desde inicio hasta el limite
        for i in range(5):
            print("i={}".format(i))#ciclo de uno en uno
        for i in range(2,10):
            print("i={}".format(i))#ciclo de un valor inicial a un valor final
        for i in range(4,10,2):
            print("i={}".format(i),end=" ")#ciclo con valor inicial y valor final, y con parametros de saltos en aumento
        for i in range(12,3,-3):
            print("i={}".format(i))#ciclo con valor inicial y valor final, y con parametros de saltos de decremento
        
        longitud=len(datos)
        for i in range(longitud):
            print(datos[i])

        for j in range(longitud-1,-1,-1):
            print(datos[j])

        for i, valor in enumerate(datos):
            print(i,valor)
            
        print("\n Diccionario de notas")
        # for clave,valor in docente.items():
        #     print(clave,":",valor, end=" ")

        listanota=[(30,40),[20,40,20],(50,40,20,10,5)]
        acu=0
        con=0
        prom=0
        prom1 = 0
        for notas in listanota:
            print(notas)
            acu1 = 0
            con1 = 0
            for nota in notas:
                print(nota)
                con+=1
                acu=acu+nota
                prom=acu/con
                acu1=acu1+nota
                con1=con1+1
                prom1 = acu1 / con1
            print("aumuado:",acu1,"notas:",con1)
            print(acu1,con1,prom1)
        print("")
        print(acu)
        print(con)
        print(prom)
       
        listaalumnos=[{"nombre":"Shaynee","final":70},{"nombre":"Nath","final":60},{"nombre":"James","final":90}]
        acu=0
        con=0
        for alumnos in listaalumnos:
            print(alumnos)
            for clave,valor in alumnos.items():
                print(clave,":",valor, end="  ")
                if clave=="final":
                    acu=acu+valor
            con=con+1
        pro=acu/con
        print(pro)
    
        frase="Hola como estas"
        vocales=[]
        for car in frase:
            if car in ("a","e","i","o","u"):
                vocales.append(car)
        print(vocales)
    
objFor=For()
objFor.usoFor()