from random import randint

def insertion_sort(lista):
    for i in range(1, len(lista)):
        valor = lista[i]
        j = i - 1
        while j >= 0 and valor < lista[j]:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = valor
        print(lista)


lista = list()
cont = 0
while True:
    num = randint(0,100)
    if num %2 == 1 and num not in lista:
        lista.append(num)
        cont += 1
    if cont >= 30:
        break 
print(lista)
print('='*120)
insertion_sort(lista)
