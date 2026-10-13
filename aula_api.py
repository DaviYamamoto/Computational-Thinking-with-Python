import requests
'''

#1)Obter o CEP
#2)Receber o CEP (1) e realizar a requisição
#3)Imprimir os dados recebidos


def receber_cep():
    cep = input("Digite seu CEP: ")
    url = f"https://viacep.com.br/ws/{cep}/json/"
    return url

def search_cep(url):
        requisicao = requests.get(url)
        
        if requisicao.status_code == 200:
            resposta_json = requisicao.json()
        
            print(f"CEP: {resposta_json["cep"]}")
            print(f"Logradouro: {resposta_json["logradouro"]}")
            print(f"Complemento: {resposta_json["complemento"]}")
            print(f"Bairro: {resposta_json["bairro"]}")
            print(f"Localidade: {resposta_json["localidade"]}")
            print(f"Estado: {resposta_json["uf"]}")
        
        elif requisicao.status_code == 404:
            print("Não foi possível encontrar o endereço!")
        elif requisicao.status_code == 500:
            print("Ocorreu algum erro no Servidor!")
        else:
            print(requisicao.status_code) #vai vir o erro do python mesmo, ja que nao tratamos todos os erros


#Main
cep = receber_cep()
try:
    search_cep(cep)
except ConnectionError:
    print("Houve um erro de conexão!") 
except Exception as e:  #"as e" -> para ajudar a identificar qual o erro
    print(f"Erro: {e}")


#Exemplo API Pokemon
import requests

contador = 1
url = "http://pokeapi.co/api/v2/pokemon"

response = requests.get(url)

dados = response.json()

lista = dados["results"]

for pokemon in lista:
    print(f"{contador}: {pokemon["name"]}")
    contador+=1
'''

#Exemplo 3
import requests


url = f"http://dummyjson.com/recipes?limit=50"
try:
    resposta = requests.get(url, verify=False)

    ing_busca = input("Ingrediente: ")

    if resposta.status_code == 200:
        dicionario = resposta.json()

        lista_receitas = dicionario["recipes"]

        for receita in lista_receitas:
            lista_ingredientes = receita["ingredients"]
            for ingredient in lista_ingredientes:
                if ing_busca.lower() in ingredient.lower():
                    print("-"*50)
                    print(receita["name"])
                    print(receita["ingredients"])

    else:
        print("Erro de requisição!")



except Exception as erro:
    print(f"Erro: {erro}")  
