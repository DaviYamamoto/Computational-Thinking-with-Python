#Estrutura e como alterar um valor existente nos Dicionários
'''
dicionario = {"Banana" : 3.00,
              "Laranja" : 5.00,
              "Manga" : 4.00,}

dicionario["Manga"] = 3.00
print(dicionario)
print(dicionario["Banana"])
#Inserir novo item
dicionario["Maça"] = 6.00
print(dicionario)
#Remover item
dicionario.pop("Maça")
print(dicionario)
#Percorrer as chaves(keys) do dicionário
for i in dicionario.keys():
    print(i)
#Percorrer os valores(values) do dicionário
for i in dicionario.values():
    print(i)
#Percorrer chaves e valores (keys and values) do dicionário
for chave, valor in dicionario.items():
    print(chave, valor)
#Verificar se uma chave existe no dicionário (in)
if "Banana" in dicionario:
    print("A chave existe no dicionário")
else:
    print("A chave não existe no dicionario")

#Preencher dicionário com entradas do usuário
alunos = {} #dicionário vazio
for i in range(5):
    ra = int(input("Insira o RA do aluno: "))
    nome = str(input("Insira o nome do aluno: "))
    alunos[ra] = nome #insere no dicionário
print(alunos)


#Dicionário com listas (cada chave só pode ter um valor, se precisar ter mais, precisamos de uma lista ou um dicionário com outros dicionários)
notas = {"123" : [8,9,10],
         "456" : [8,7,9],
         "789" : [7,8,9],}
print(notas["123"])
print(notas["123"][0])


#Dicionário com outros dicionários
clientes = {1234: {'nome': 'João', 'idade': 24, 'telefone': '(11)93333-5678'},
            5678: {'nome': 'Pedro', 'idade': 30, 'telefone': '(11)98456-2233'},
            8456: {'nome': 'Maria', 'idade': 28, 'telefone': '(11)92332-9832'},
            6543: {'nome': 'Antônio', 'idade': 45, 'telefone': '(11)99432-1234'} }

print(clientes[1234])
print(clientes[1234]["telefone"])
'''









#1
'''
chave = {}
for i in range(5):
    cpf = int(input("Digite um CPF: "))
    nome = input("Digite um nome: ")
    chave[cpf] = nome
print(chave)


#2
produtos = {}
for i in range(5):
    nomep = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: "))
    produtos[nomep] = preco

print("Produtos com valor igual ou superior à R$50:")
for nome, preco in (produtos.items()):
    if preco >= 50:
        print(nome , f"R${preco:.2f}")


#3
#Como adicionar uma lista dentro do Dicionário
alunos = {}
f = 1
for i in range(5):
    rm = int(input("Insira o RM do aluno: "))
    notas = [] #zera as notas, se nao vai pegar as notas do aluno anterior
    for j in range(3):
        n = float(input(f"Insira a {f}° nota do aluno: "))
        notas.append(n)
        f += 1
    alunos[rm] = notas
print(alunos)
for nome, notas1 in alunos.items():
    media = (notas1[0] + notas1[1] + notas1[2]) / 3
    print(nome, f"Média: {media}")
'''

#4
#Contar a quantidade de vogais em um texto e armazena essa vogal
vogais = {}
texto = str(input("Seu Texto: "))
for letra in texto:
    if letra in "aeiou":
        if letra in vogais:
            vogais[letra] += 1
        else:
            vogais[letra] = 1
print(vogais)
