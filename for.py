#for var in range(stop) -- "var" == variável
#for var in range(start , stop)
#for var in range(start, stop, step)
'''for a in range(-1, 98):
    print(a+1)
for a in range(99,-1 ,-1):
    print(a)

for a in range(51):
    print(a)
for a in range(199, 99, -2):
    print(a)

for a in range(1, 101, 2):
    print(a)

from random import randint
for a in range(0, 21):
    print(randint(1,50))

first = int(input("Digite o 1° número: "))
maior = first
menor = first
for a in range(2 ,11 ,1):
    num = int(input(f"Digite o {a}° número: "))
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f"O maior número digitado foi {maior}\nO menor número digitado foi {menor}")

n = -1
while n < 0:
    n = int(input("Digite um número inteiro e positivo: "))

if n == 0 or n == 1:
    print(f"O fatorial de {n}! = 1")
else:
    for i in range (2, n):
        n *= i
    print(f"O fatorial de {i+1}! = {n}")

#Sequencia de Fibonacci
n = 0
a = 1
b = 1
while n <= 0:
    n = int(input("Digite um número para visualizar a sequencia de Fibonacci: "))
match n:
    case 1:
        print("1")
    case 2:
        print(f"f{a}\n{b}")
    case _:
        print(a, "\t", b, end = "\t")
        for i in range(n-2):
            fib = a + b
            print(fib, end = " ")
            a = b
            b = fib

num = int(input("Digite um número: "))
for i in range(2, num, 2):
    if num % i == 0:
        print("Não é primo")
    else:
        print()

alu = int(input("Quantos alunos tem na sala? "))
notas = int(input("Quantas notas por aluno? "))
soma = 0
for i in range(alu):
    for x in range(notas):
        nt = float(input(f"{x+1}° Nota: "))
        soma += nt
    media = soma / notas
    print(f"A média do {i+1}° aluno é {media}")
    soma = 0
'''
#Acerte o Número aleatório
import random
a = random.randint(1, 100)
soma = 0
while True:
    tent = int(input("Qual número você acha que foi sorteado? "))
    if tent < a:
        print(f"O número sorteado é maior do que {tent}")
        soma += 1
        continue
    elif tent > a:
        print(f"O número sorteado é menor do que {tent}")
        soma += 1
        continue
    else:
        print(f"Parábens! Você acertou em {soma+1} tentativas")
        break
