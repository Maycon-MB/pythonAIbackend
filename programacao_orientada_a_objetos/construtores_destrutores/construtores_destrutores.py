class Cachorro:
    def __init__(self, nome, cor, raca, acordado=True):
        print("Iniciando a classe")
        self.nome = nome
        self.cor = cor
        self.raca = raca
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")
    
    def latir(self):
        print("au au")

def criar_cachorro():
    c = Cachorro("Bubbaloo","Marrom", "Yorkshire", False)
    print(c.nome)

dog = Cachorro("Pepe", "Preto", "Dachshund")
dog.latir()