class Veiculo:
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas

    def ligar_motor(self):
        print("Ligando o motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, carregado):
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("Preta", "XYZ-0987", 2)
moto.ligar_motor()

carro = Carro("Vinho", "ABC-1234", 4)
carro.ligar_motor()

caminhao = Caminhao("Azul", "QWE-4567", 6)
caminhao.ligar_motor()
caminhao.esta_carregado()