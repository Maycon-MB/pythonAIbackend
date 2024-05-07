# O discard serve para apagar elementos de um conjunto. Ele não apresenta erros mesmo pedindo para remover elementos não existentes.
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

numeros.discard(1)
print(numeros)
# {2, 3, 4, 5, 6, 7, 8, 9, 10}

numeros.discard(9)
numeros.discard(5)
numeros.discard(1000)
print(numeros)
# {2, 3, 4, 6, 7, 8, 10}