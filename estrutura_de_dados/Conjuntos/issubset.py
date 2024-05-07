# O issubset serve para identificar se um conjunto é subconjunto do outro.
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 7, 1, 9}

resultado = conjunto_a.issubset(conjunto_b)
print(resultado) 
# True

resultado = conjunto_b.issubset(conjunto_a)
print(resultado)
# False