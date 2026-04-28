'''
m = 9
lista = ["Pedro", "Andy", "Raniele", "Neymar"]
print(f"Quem é o GOAT? \nResposta: {lista[2]}")
for i in range(len(lista)):
    print(lista[i])

lista[1] = "Hugo Souza"
print(lista)

lista.insert(2, 67)
print(lista)

lista.pop(0)
print(lista)

for item in lista:
    print(item)

numeros = []
for i in range(5):
    n = int(input("Informe um número: "))
    numeros.append(n)
print(numeros)

numeros1 = []
while True:
    n1 = int(input("Informe um número: "))
    if n1 == 0:
        break
    numeros1.append(n1)
print(numeros1)

lista = [4, 6, 8, 10 , 67, 10 , 40]
cont = 0
for indice in range(len(lista)):
    if lista[indice] % 2 == 0:
        lista[indice] = 0
print(lista)
'''

#exercícios
'''numerospar = []
numerosimpar= []
for i in range(10):
    n = int(input(f"Informe o {i+1}° número: "))
    if n % 2 == 0:
        numerospar.append(n)
    else:
        numerosimpar.append(n)
print(f"Pares: {numerospar}\nImpar: {numerosimpar}")

tudo = []
par = []
soma = 0
somatd = 0
for i in range(10):
    n = int(input(f"Informe o {i+1}° número: "))
    tudo.append(n)
for s in tudo:
    somatd += s
    media = somatd / len(tudo)
    if s % 2 == 0:
        soma += s


print(f"Media aritmetica: {media}\nSoma Par: {soma}")


import random
numeros = []
for i in range(20):
    numeros.append(random.randint(1,50))
print(f"Números armazenados: {numeros}")
soma = 0
for n in numeros:
    soma += n
print(f"Soma: {soma}")
maior = numeros[0]
for n in numeros:
    if n> maior:
        maior = n
print(f"Maior número: {maior}")
menor = 0
for n in numeros:
    if n < menor:
        menor = n
print(f"Menor número: {menor}")

nomes = []
idades = []
for s in range(10):
    n = str(input("Informe o seu nome: "))
    nomes.append(n)
    i = int(input("Informe a sua idade: "))
    idades.append(i)
for o in range(len(idades)):
    if idades[o] >= 18:
        print(nomes[o])

import random
conta = 0
numeros = []
for s in range(10):
    numeros.append(random.randint(1,11))
escolha = int(input("Informe um número: "))
for i in numeros:
    if escolha == i:
        conta += 1
print(f"O número {escolha} apareceu {conta} vezes")

notas = []
cont = 0
while True:
    notas1 = float(input("Informe as notas: "))
    if notas1 < 0:
        break
    notas.append(notas1)
print(f"A quantidade de notas que foram armazanadas foram: {len(notas)}")
print(f"Ordem informada: {notas}")
media = sum(notas) / len(notas)
print(f"Média das notas: {media}")
for i in notas:
    if i > media:
        cont += 1
print(f"Notas acima da média: {notas}")'''
