#Manipulação de Strings
'''
for x in "Corinthians":
    print(x)

#Ver se uma certa palavra está na lista
txt = "The best things in life are free"
print("free" in txt)

#Tirar espaços do começo e final da string
txt1 = "     Vai Corinthians    "
print(txt1.strip())

#Contar quantas palavras (que voce quiser verificar) está presente na lista
txt2 = "I love apples, apple are my favorite fruit"
x2 = txt2.count("apple")
print(x2)

#Substituir caracter
txt3 = "Hello World"
print(txt3.replace("o", "j"))

#Dividir a string em substrings sempre que algo especificado aparecer
txt4= "Banana, Abacaxi, Maça"
print(txt4.split(","))

#Concatenar/Juntar duas ou mais strings
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Title = Deixa o primeiro caracter de cada palavras maiuscula
#Startswith = Retorna True se a string comecar com o valor especificado
#Endswith = Retorna True se a strings terminar com o valor especificado
#Find = procura na string um valor especificado e retorna sua posicao
#Isalnum = Retorna True se todos os caracteres da string forem alfanumericos
#Isalpha = Retorna True se todos os caracteres da string estiverem no alfabeto
#Isdigit = Retorna True se todos os caracteres da string forem digitos
#Isspace = Retorna True se todos os caracteres da string forem espaços em branco
#Islower = Retorna True se todos os caracteres da string forem minusculos
#Isupper = Retorna True se todos os caracteres da string forem maiusculos

#Fatiamento de Strings (slicing)
texto = "Exemplo de Texto"

a = texto[0:7] #nao pega o 7, vai até 6
b = texto[8:16] #nao pega o 16, vai ate o 15
c = texto[8:10] #nao pega o 10, vai ate o 9

print(a)
print(b)
print(c)
print(texto[3:])
print(texto[:3])
print(texto[:])
print(texto[::-1]) #printa tudo de tras para frente

#Tupla - Ela é imutavel, nao da para mexer nos valores dentro dela
tupla = (2,"abc", 7, 8)
print(tupla) #nao pode adicionar coisas na tupla. Para fazer isso tem que transforma-la em uma lista e ai sim modifica-la
#lista = list(tupla) -> Transforma a Tupla em Lista
#tupla = tuple(lista) -> Transforma a Lista em Tupla

def somar (a, b):
    c = a + b
    d = a * b
    return c,d #em algumas linguagens principais isso daria erro, nao pode retornar 2 valores(c, d)

#Main
x = somar(10, 15) #X é uma Tupla
print(x)
#x[0] = 10 -> da erro pq é uma tupla, nao tem como modificar

y = list(x)
print(y)
y[0] = 10 #agora que é lista, da para modificar
print(y)

#Exercicios
#1
def quantidade(a: str):
    return len(a)

a = str(input("Digite uma frase: "))
b = quantidade(a)
print(f"Quantidade de Caracteres: {b}")

#2
def maius(frase: str):
    frase = frase.upper()
    return frase

frase = str(input("Digite uma frase: "))
frase1 = maius(frase)
print(frase1)

#3
def vogais(letras: str):
    a = letras.count("a", "e", "i", "o", "u")
    return a

a = str(input("Digite uma frase: "))
b = vogais(a)
print(b)

txt2 = "I love apples, apple are my favorite fruit"
x2 = txt2.count("apple")

#4
frase = str(input("Digite uma frase: "))
print(frase.split())


#5
def quantidade_palavras(frase:str):
    frase = frase.split()
    return len(frase)

frase = str(input("Digite uma frase: "))
a = quantidade_palavras(frase)
print(a)

#6
def tirar_espacos(frase:str):
    frase = frase.strip()
    return frase

frase = str(input("Digite uma frase: "))
a = tirar_espacos(frase)
print(a)

#7
lista = []
maior = []
for i in range(10):
    n = int(input("Digite um valor: "))
    lista.append(n)
    if n > maior:

#8
lista = []
pares = []
soma = 0
for i in range(10):
    n = int(input("Digite um valor: "))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        soma += n

print(f"Números pares na lista: {pares}")
print(f"Soma dos números impares: {soma}")

#9
lista = []
impares = []
pares = []
for i in range(10):
    n = int(input("Digite um valor: "))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(pares)
print(impares)

#10
nomes = []
idades = []
maior = []
while True:
    n = str(input("Digite um nome: "))
    nomes.append(n)
    if n == "":
        break
    i = int(input("Digite sua idade: "))
    idades.append(i)
for i in range(len(idades)):
    if idades[i] >= 18:
        maior.append(nomes[i])
print(maior)



#11
tupla1 = []
tupla2 = []
for i in range(5):
    n1 = int(input("Digite um valor: "))
    a = tupla1.append(n1)
for i in range(5):
    n2 = int(input("Digite outro valor: "))
    b = tupla2.append(n2)
tupla1 = tuple(tupla1)
tupla2 = tuple(tupla2)
tupla3 = tupla1 + tupla2
print(tupla3)
'''
