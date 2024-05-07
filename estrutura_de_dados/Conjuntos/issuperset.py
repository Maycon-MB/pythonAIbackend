# O issuperset serve para identificar se um conjunto é super conjunto do outro.
conjunto_a = {1, 2, 3}
conjunto_b = {2, 4, 6, 7, 1, 3}

resultado = conjunto_a.issuperset(conjunto_b)
print(resultado)
# False

resultado = conjunto_b.issuperset(conjunto_a)
print(resultado)
# True