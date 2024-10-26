from random import randint

lista = [randint(1, 100) for _ in range(100)]
print(lista)

lista = [x for x in lista if x > 50]
print(lista)