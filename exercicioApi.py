import requests
import json

url = "https://jsonplaceholder.typicode.com/users"
requisicao = requests.get(url, verify= False)
nUser = 0
lista_users = []
try:
    if requisicao.status_code == 200:
        resposta_json = requisicao.json()
        for i in resposta_json:
            print(f"Nome: {i["name"]}")
            print(f"E-mail: {i["email"]}")
            print(f"Cidade: {i["address"]["city"]}")
            nUser += 1
            print(f"Número de Usuários: {nUser}")

            dicio = {
                "nome": i["name"],
                "email": i["email"],
                "cidade": i["address"]["city"],
            }
            lista_users.append(dicio)
        lista_users.append({"total de usuários": nUser})

        with open("usuarios.json", "w", encoding="utf-8") as arquivo:
            json.dump(lista_users, arquivo, indent=4, ensure_ascii=False)

    else:
        print(f"ERRO: {requisicao.status_code}")


except ConnectionError:
    print("Erro de Conexão")
