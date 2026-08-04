'''
import random
a = random.randint(1,100)
soma = 0
while True:
    tent = int(input("Qual número você acha que foi sorteado? "))
    if tent < a:
        print(f"O número sorteado é maior que {tent}")
        soma += 1
        continue
    elif tent > a:
        print(f"O número sorteado é menor que {tent}")
        soma += 1
        continue
    else:
        print(f"Você acertou o número sorteado em {soma+1} tentativas!")
        break
'''

#exercicio 1
def media(soma_valores, quantidade):
    media = soma_valores/quantidade
    return media

def soma(a, b):
    return a + b

a = int(input("Informe a primeira nota: "))
b = int(input("Informe a segunda nota: "))
quant= 2
a = soma(a, b)
while True:
    yn = int(input("Deseja informar mais alguma nota? Sim(1) Não(2) "))
    if yn == 1:
        b = int(input("Informe a próxima nota: "))
        quant = quant+1
        a = soma(a, b)
    else:
        break

print(media(a, quant))

