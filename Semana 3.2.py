# listaNotas = [(30, 40),(20,40,20), (50,40,20,10,5)]
# acum=0
# long=0
# for notas in listaNotas:
#     parcial=0
#     print(notas, end= " ")
#     for nota in notas:
#         long=long+1
#         acum = acum + nota
#         parcial += nota
#     promparcial=parcial/len(notas)
#     print("Notas Parciales= {} Promedio Parcial {}".format(parcial,promparcial))
# prom = acum/long
# print(("Total notas {} - #Notas {}: Promedio {}".format(acum,long,prom)))


# listaAlumnos = [{"nombre":"Erick","final":70},{"nombre":"Yady","final":60},{"nombre":"Danny","final":90}]
# acum=0
# cont=0
# for alumnos in listaAlumnos:
#     print(alumnos)
#     for clave,valor in alumnos.items():
#         print(clave, ":",valor, end= " " )
#         if clave== "final": acum=acum=valor
#     cont+=1
# print(acum/cont)


frase = "Hola como estas"
# vocales = []
# for car in frase:
#     if car in ("a","e","i", "o", "u"):
#         vocales.append(car)
#     print(vocales)

vocales=[car for car in frase]
print(vocales)
