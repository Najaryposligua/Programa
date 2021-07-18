class cargo:
    secuencia=0
    def __init__(self,des="Sin cargo"):
        cargo.secuencia=cargo.secuencia+1
        self.codigo= cargo.secuencia
        self.descripcion= des

cargo1= cargo()
print(cargo1.codigo,cargo1.descripcion)
cargo2 = cargo()
cargo2.descripcion ="Director"
print(cargo2.codigo,cargo2.descripcion)
cargo3= cargo("Analisista")
print(cargo3.codigo, cargo3.descripcion)
# print(cargo.secuencia)
# print(cargo1.secuencia)
# print(cargo2.secuencia)
# print(cargo3.secuencia)


