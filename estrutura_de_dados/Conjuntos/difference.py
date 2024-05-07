# O difference serve para identificar quais elementos de um primeiro conjunto são diferentes do segundo conjunto.
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

diff_conjunto1 = conjunto_a.difference(conjunto_b)
print(diff_conjunto1)
# {1}

diff_conjunto2 = conjunto_b.difference(conjunto_a)
print(diff_conjunto2)
# {4}