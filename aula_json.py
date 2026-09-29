'''
with open("clientes.txt", "r") as arquivo:
    cli = {} #dicionário vazio
    for linha in arquivo: #varer o "arquivo"
        dados = linha.split(",") #separar os items da linha com vírgula
        cod = dados[0] #a posição 0 do arquivo está guardando o código
        nome = dados[1] #segunda posicao da lista e joguei dentro da variável nome
        compras = [float(dados[2]), float(dados[3])] #transformei os items 3 e 4 da lista e joguei dentro de outra lista
        cli[cod] = {"nome": nome, "compra": compras} #cli é o nome do dicionario que decladou la encima, o [cod] é a chave para eu identificar o valor ou valores
    print(cli)


#Aula JSON
import json
x = '{"name": "John", "age": 30, "city": "New York"}'
y = json.loads(x) #carregar json
print(y["age"]) #o resultado é um dicionário python

y1 = json.dumps(x) #converte em json
print(y1) #o resultado é uma string json

with open("arquivo.json", "r") as arquivo:
    y = json.load(arquivo) #pega um arquivo json, abro o arquivo(with open), e o transformo em dicionário (json.load())
print(y["emails"])

#com string usa o "s" no final de dump(dumps) e load(loads), com arquivo é sem o s (dump e load)


#Exercícios
#1
import json
from textwrap import indent

with open("notas.txt", "r") as arquivo:
    alunos ={}
    for linha in arquivo:
        dados = linha.split(",")
        cod = dados[0]
        nome = dados[1]
        notas = [float(dados[2]), float(dados[3]), float(dados[4]), float(dados[5])]
        alunos[cod] = {"nome": nome, "notas": notas}
with open("notas.json", "w", encouding='utf-8') as arquivo:
    json.dump(alunos, arquivo, indent=4, ensure_ascii=False))


#2
import json
with open("foods.txt", "r") as arquivo:
    cli = {}
    for linha in arquivo:
        dados = linha.split(",")
        cod = dados[1]
        nome = dados[0]
        food = dados[2]
        cli[cod] = {"name": nome, "food": food}
    with open("foods.json", "w") as arquivo:
        json.dump(cli, arquivo, indent=4)


#3
import json
herois = list()
with open("heroes.json", "r") as arquivo:
    arquivo = json.load(arquivo)
    for dado in arquivo["members"]:
        if "Flight" in dado["powers"]:
            herois.append(dado["name"])
print(herois)
'''

# 4
import json

print("---CADASTRO DE PETS---")
while True:
    opcao = int(input("OPÇÕES:\n1.Inserir\n2.Excluir\n3.Listar Todos\n4.Sair\nOpção desejada: "))
    match opcao:
        case 1:
            with open('pets.json', 'r') as arquivo:
                pets = json.load(arquivo)
                novo_pets = {
                    "tipo": str(input("Insira o tipo do pet: ")),
                    "nome": str(input("Insira o nome do pet: ")),
                    "idade": int(input("Insira o idade do pet: "))
                }
                pets.append(novo_pets)
                with open('pets.json', 'w') as arquivo:
                    json.dump(pets, arquivo, indent=4)
        case 2:
            with open('pets.json', 'r') as arquivo:
                pets = json.load(arquivo)
            nome_remover = str(input("Insira o nome do pet que deseja excluir: "))
            for pet in pets:
                if pet["nome"] == nome_remover:
                    pets.remove(pet)
                    with open('pets.json', 'w') as arquivo:
                        json.dump(pets, arquivo, indent=4)
                    break
        case 3:
            with open('pets.json', 'r') as arquivo:
                pets = json.load(arquivo)

            print(json.dumps(pets, indent=4, ensure_ascii=False))
        case 4:
            break
