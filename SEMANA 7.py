class logica:
    def __init__(self,lista=None):
        self.__lista=lista

    @property
    def lista(self):
        return self.__lista
    @lista.setter
    def lista(self,value):
        self.__lista=value

    def parimpar(self,numero):
        rec=numero%2
        if rec==0:
            print("{}es par".format(numero))
        else:
            print("{}es par".format(numero))

    def perfecto(self,numero):
        pass


class ejercicio(logica):
    def __init__(self,lista=None):
        pass
    def suma(self,n1,n2):
        return n1+n2

ejer= ejercicio()
ejer.parimpar(6)
print(ejer.suma(4,8))


#ejer=logica([2,4,6])
# ejer.lista=[1,3]
# print(ejer.lista)