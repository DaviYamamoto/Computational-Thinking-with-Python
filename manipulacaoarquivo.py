#Exemplo: Conjunto tem que receber 5 valores diferentes e parar + Tratamento de Erro
'''conjunto = set()
while len(conjunto) < 5:
    try:
        valor = int(input("Digite um valor: "))
        conjunto.add(valor)
    except ValueError:
        print("Valor invalido. Digite apenas valores inteiros.")
print(conjunto)

#Manipulação de Arquivos de Texto
#Um arquivo chamado "teste.txt" será aberto para leitura
arquivo = open("teste.txt", "r")

#A função read() irá copiar todo o conteudo do arquivo para uma STRING
texto = arquivo.read()
print(texto)

#Outra maneira de percorrer o arquivo
for linha in arquivo:
    print(linha)

#fecha o arquivo e liberação da memória
arquivo.close()


#Um arquivo chamado "nomearquivo.txt" será criado e aberto para escrita
arquivo = open("nomearquivo.txt", "w")
#Escreve uma string no arquivo com a função write
arquivo.write("Este texto será escrito no arquivo\n")
#Fecha o arquivo e libera memória
arquivo.close()


#testando na prática
arquivo = open("exemplo.txt", "w", encoding="utf-8") #"encouding="utf-8" é para a IDE reconhecer os acentos, sem isso ela coloca um monte de simbolo estranho

arquivo.write("Olá, esse é o nosso primeiro arquivo.\nVai Corithians!\n")

arquivo.close()


#lendo arquivo que criei na máquina
arquivo = open("exemplo2.txt", "r", encoding="utf-8")
for i in arquivo:
    print(i)

arquivo.close()
'''

#Abrir arquivo utilizando "with" == melhor e mais seguro, o arquivo vai ser fechado automaticamente
with open("exemplo2.txt", 'a', encoding="utf-8") as arquivo:
    arquivo.write("\nEsse texto deve aparecer no final do arquivo.")
    arquivo.write("Esse novo texto estará grudado no anterior\n") #vai estar grudado pq não coloquei o "\n" no final da linha anterior
