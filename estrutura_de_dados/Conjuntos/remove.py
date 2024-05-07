# O remove serve para apagar elementos de um conjunto. Ele apresenta erros se pedir para remover elementos não existentes.
numeros = {2, 43, 7, 2, 654, 60}
print(numeros)
# {2, 7, 43, 60, 654}

numeros.remove(7)
print(numeros)
# {2, 43, 60, 654}