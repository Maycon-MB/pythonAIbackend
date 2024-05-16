class Bicicleta:
    def __init__ (self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("bi-bi")
    
    def parar(self):
        print("Parando... ")
        print("bicleta parada.")

    def correr(self):
        print("Vrummmmm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

obj1 = Bicicleta("azul", "caloi", 2024, 700)
obj1.buzinar()
obj1.parar()
obj1.correr()
print(obj1.cor, obj1.modelo, obj1.ano, obj1.valor) 

obj2 = Bicicleta("vermelho", "GTSM1", 2020, 450)
print(obj2)