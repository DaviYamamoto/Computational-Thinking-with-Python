'''matriz = [[1, 2, 3, 4],      #ou matriz = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

print(matriz) #matriz completa (tudo na mesma linha)
print(matriz[0]) #primeira lista/linha
print(matriz[2][3]) #item especifico

for linha in matriz:
    print(linha) #printa linha por linha
for linha in matriz:
    for item in linha:
        print(item) #printa 1 item por vez da linha

x = len(matriz) #quantidade de linhas
y = len(matriz[0]) #quantidade de colunas
print(x)
print(y)

for i in range(len(matriz)): #mesma coisa do "for linha in matriz: \t for item in linha: \t print(item)"
    for j in range(len(matriz[0])):
        print(matriz[i][j])

#formato de tabela
matrizz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for linha in range (len(matrizz)):
    for coluna in range(len(matriz[0])):
        print(matrizz[linha][coluna], end="\t")
    print()  #pula 1 linha


nota = [2, 4]
nota.append(10)
print(nota)
sla = [5,6]
nota.append(sla)
print(nota)


linhas = int(input("Quantidade de linhas: "))
colunas = int(input("Quantidade de colunas: "))
matrizz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        n = int(input("Número: "))
        linha.append(n)
    matrizz.append(linha)
print(matrizz)





#exercicios
#1
linhas = 3
colunas = 5
matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        n = int(input("Informe o número: "))
        linha.append(n)
    matriz.append(linha) #insere cada linha na matriz
print(matriz)

#2
print("12 Números")
matriz = []
linhas = 3
colunas = 4
for i in range(linhas):
    linha = []
    for j in range(colunas):
        n = int(input("Digite um número: "))
        linha.append(n)
    matriz.append(linha)
print(matriz)'''

#3 e 4 juntos
import random

def criar_matrizz(n_linha, n_coluna):
    matriz = []
    for i in range(linhas):
        linha =[]
        for j in range(colunas):
            linha.append(random.randint(0, 20))
        matriz.append(linha)
    return matriz

def exibir_matriz (matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            print(matriz[linha][coluna], end="\t")
        print()

def soma_diagonal(matriz):
    total = 0
    i = 0
    j = 0
    while i < len(matriz):
        total += matriz[i][j]
        i += 1
        j += 1
    return total

def menor(matriz):
    menor = matriz[0][0]
    for i in matriz:
        for j in i:
            if j < menor:
                menor = j
    print(f"O menor valor da Matriz é:{menor}")


#Main
linhas = 5
colunas = 5
m = []
m = criar_matrizz(linhas, colunas)
exibir_matriz(m)

print(f"O somatório dos valores da diagonal principal da matriz é: {soma_diagonal(m)}")
menor(m)
