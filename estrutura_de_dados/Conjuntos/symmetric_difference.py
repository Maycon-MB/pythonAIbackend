# O symmetric_difference serve para identificar quais são os elementos diferentes de ambos os conjuntos.
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

sym_diff = conjunto_a.symmetric_difference(conjunto_b)
print(sym_diff)
# {1, 4}