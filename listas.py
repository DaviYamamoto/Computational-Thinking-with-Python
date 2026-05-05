#listas != variável
#lista(array) == estrutura de armazenamento temporario
from itertools import count

from sqlalchemy.sql.operators import truediv

'''
lista = []
print(lista)
#print(lista[0]) #erro, não existe a posição na lista

#append == criar espaço de memória na ultima posição, ai sim adicionar valor
lista.append(1)
print(lista)
lista.append(2)
print(lista)
lista[0] = 10
print(lista)
n = len(lista)
print(f"A lista possuí {n} items")

#pop == remove uma posição
lista.pop(1)
print(lista)

nomes = ["Paulo", "Pedro", "João"]
for i in range(len(nomes)):
    print(nomes[i])

numeros = []
while True:
    n = int(input("Informe um Número: "))
    if n == 0:
        break
    numeros.append(n)
print(numeros)

print(nomes.count("Paulo")) #quantos "Paulo" tem na lista?
print(nomes.index("Pedro")) #retorna a primeira ocorrência

lista = [10, 5, 67, 8, 9, 2]
if 67 in lista:                  #se 67 estiver in lista == retorna algo
    print("Item encontrado!")
else:
    print("Item não encontrado.")

lista.insert(5, 22) #insere um item em determinado indice, não apaga nenhum valor, apenas adiciona
print(lista)

lista.sort() #ordena a lista/deixa na ordem crescente
print(lista)

lista.sort(reverse=True) #ordena a lista na ordem decrescente
print(lista)

print(min(lista)) #retorna o menor valor da lista 
print(max(lista)) #retorna o maior valor da lista

print(sum(lista)) #soma os valores da lista

#exercicios
#retornar o menor e maior valor da lista sem usar o "min"
lista = [3, 10, 7, 8, 1, 9, 8, 5, 8]
menor = lista[0]
maior = lista[0]
for i in lista:
    if menor > i:
        menor = i
    if maior < i:
        maior = i
print(f"o menor valor da lista é {menor}\nO maior valor da lista é {maior}")

lista = [3, 10, 7, 8, 1, 9, 8, 5, 8]
soma = 0
for item in lista:
    soma += item
print(f"O somatório dos valores da lista é {soma}")

#ordenar a lista em ordem crescente sem usar o ".sort"
lista = [1, 4, 6, 20, 1, 64, 5, 2, 10]
lista2 = []

for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[i] < lista[j]:
            x = lista[i]
            lista[i] = lista[j]
            lista[j] = x
print(lista)
#mesma coisa os dois
while lista:
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    lista2.append(menor)
    lista.remove(menor)

print(lista2)
'''

#exercicio 5
lista1 = [22, 17, 67, 10, 9, 11, 12, 15, 23, 30]
lista2 = [8, 12, 84, 83, 2, 65, 12, 14, 27, 75]
lista3 = []

for i in lista1:
    lista3.append(i)
    #nao terminei, COMMITAR DEPOIS
print(lista3)
