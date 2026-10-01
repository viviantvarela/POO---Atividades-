# Questão 1 - Tupla de Pares

tupla = (1, 2, 3, 4, 5)
lista_pares = []
tupla_pares = ()

for num in tupla:
    if num % 2 == 0:
        lista_pares += [num]
else:
    print(tupla)
    
tupla_pares = tuple(lista_pares)
print(tupla_pares)
