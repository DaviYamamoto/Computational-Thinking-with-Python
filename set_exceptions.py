#Conjuntos (set)
#Estrutura de Dados (coleção de dados)
#Definidas entre chaves {}
#Estrutura não ordenada (não mostrar na ordem) e não indexada
'''conjunto = {"maça", "banana", "manga"}
print(conjunto)
conjunto = {"maça", "banana", "manga", "banana"}
print(conjunto) #não repete se tiver 2 items iguais

#Conjuntos são heterogêneos (pode ter str, int, float, bool e etc)
conjunto = {"FIAP" , 34, 50, "abc", True, 1, 1}
print(conjunto) #não vai printar o "1" pq True = 1 - ele nao reconhece o 1 como int e o True como bool,
# ele reconhece como se os dois fossem as mesmas coisas - se voce precisar desse 1 ele nao poderia estar
#em um set (se o true estivesse nesse set tambem)

#Tamanho do Conjunto(len - todas as estruturas em Python usa o "len" para saber o tamanho)
len(conjunto) #já ignora repetições
print(len(conjunto))

#Acessando elementos do Conjunto
x = 34 in conjunto #verificar se o elemento está no conjunto(in)
print(x)
y = 35 in conjunto
print(y)
for item in conjunto: #verificar todos os items no conjunto
    print(item)

if 34 in conjunto: #verificar se o elemento está no conjunto(if-else + in)
    print("Está contido")
else:
    print("Não está contido")

#Inserindo itens ao conjunto (add())
nomes = {"Paulo", "Ana", "Pedro", "Maria"}
print(nomes)
nomes.add("FIAP")
print(nomes)
nomes.add("FIAP")
print(nomes) #não vai repetir

#Removendo um elemento do Conjunto (remove/discard)
#nomes.remove("Fernando") #ele vai retornar (remove) erro pq Fernando não está contido no set
nomes.remove("Ana") #apagou pq esse nome existe no set
print(nomes)
nomes.discard("Fernando") #não da erro, mas não fala se removeu ou não
print(nomes)
nomes.discard("Maria") #removeu normalmente
print(nomes)

#Preenchendo conjuntos com input() + add()
numeros = set() #da para criar um set dessas maneira, tambem da para criar listas, tuplas e etc da mesma maneira
for i in range(5):
    n = int(input("Número: "))
    numeros.add(n)
print(numeros)

#Unindo Conjuntos(sets)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
#union - junta todos os elementos, se tivesse repetidos ele não os colocaria
set3 = set1.union(set2)
print(set3)

#Intersecção entre os Conjuntos(sets) - Ver o que está presente nos dois conjuntos que você está comparando
x1 = {"Apple", "Orange", "Cherry"}
y1 = {"Google", "Microsoft", "Apple"}
z1 = x1.intersection(y1)
print(z1)

#Difference - oposto da intersecção, retorna o que tem de diferente nos dois conjuntos(sets)
z2 = x1.difference(y1) #o que tem de diferença do x1 pro y1
print(z2)
z2 = y1.difference(x1) #o que tem de diferença do y1 pro x1
print(z2)

#Transformar lista em conjunto ou vice-versa - Função Set
texto = "bananeira"
print(type(texto))
caracteres = set(texto)
print(caracteres) #ele retira as repetições

lista =  ["Apple", "Banana", "Cherry", "Apple"]
a = set(lista)
print(a)

#Exercícios Conjuntos
#1 - Criar e manipular Sets()

pares = set()
impares = set()
f = 1

for i in range(5):
    p = int(input(f"Digite o {f} número par: "))
    im = int(input(f"Digite o {f} número impar: "))
    pares.add(p)
    impares.add(im)
    f += 1
print(pares)
print(impares)


#2 - Remover duplicatas
lista = ["Apple", "Microsoft", "Google", "Apple"]
print(lista)
set1 = set(lista) #transformei em set() para remover as duplicatas
print(set1)
lista1 = list(set1) #transformei em lista denovo mas dessa vez sem items duplicados
print(lista1)


#3 - Contar elementos únicos
lista = ["Apple", "Microsoft", "Google", "Apple", "BMW" , "Google", "Xiaomi"]
set1 = set(lista)
tamanho = len(set1) #contar a quantidade de elementos únicos
print(tamanho)
'''

#=======================================================================================
#=======================================================================================
#Tratamento de erros e exceções

#print(4/0) #dá erro de exceção, não tem como dividir por 0 no python, Traceback ZeroDivisionError

#n - int(input("Número: "))
#Número: a #da erro tambem, ValueError

#x = 5
#y = "Hello"
#z = x + y #da erro tambem, TypeError

#Instruções try-except
#Erros de sintaxe
#Exceções*
'''
while True:

    try:
        n1 = int(input("Numerador: "))
        n2 = int(input("Denominador: "))

        resultado = n1/n2

        #validação
        if n1 < 0 or n2 < 0:
            raise TypeError

    except ValueError:
        print("Digite apenas números!")
        print("Tente novamente...")
    except ZeroDivisionError:
        print("Denominador deve ser DIFERENTE DE ZERO!")
        print("Tente novamente...")
    except TypeError: #erro que eu criei a exceção lá encima
        print("Apenas valores positivos devem ser inseridos!")
        print("Tente novamente...")
    except Exception: #cai aqui se der algum erro que nao foi especificado antes, SEMPRE DEIXAR O EXCEPTION POR ULTIMO, senao cai nele antes de cair nos outros erros(caso der)
        print("Ocorreu um erro!")
        print("Tente novamente...")
    else:
        print(f"Resultado: {resultado:.2f}")
    finally:
        print("Tchau, Obrigado!")
'''

#Calcular a densidade de um material com base em sua massa e volume
#Fórmula: densidade = massa/volume
#1) Obter as medidas (massa e volume)
#2) Calcular a densidade com base na fórmula acima
#RESTRIÇÕES: -massa < 0 or volume < 0 / volume != 0
#3) Executar análise da densidade
#Função responsável por executar as funções dos itens 1 e 2
#Tratamento de exceções

#1)
def obter_massa() -> float:
    massa = float(input("Massa do Material (em Kg): "))
    return massa

def obter_volume() -> float:
    volume = float(input("Volume do Material (em m³): "))
    return volume
#2)
def calcular_densidade(massa:float, volume:float) -> float:
    #validação
    if massa < 0 or volume < 0:
        raise ValueError("[ValueError]: Massa e Volume não podem ser NEGATIVOS!") #vai lançar esse tipo de erro, vamos tratar esse erro no 3)
    if volume == 0:
        raise ZeroDivisionError("[ZeroDivisionError]: O volume do material não pode ser ZERO!")
    densidade = massa/volume
    return densidade

#3)
def executar_analise_densidade() -> None:

    try:
        massa = obter_massa()
        volume = obter_volume()

        densidade = calcular_densidade(massa, volume)
    except ValueError as erro: #erro = nome da variável
        print(f"[ERRO DE ENTRADA DE DADOS]: {erro}")
        print("Divisão por ZERO impede o cálculo da densidade")
    except ZeroDivisionError as erro:
        print(f"[ERRO FÍSICO]: {erro}")
        print("Divisão por ZERO impede o cálculo da densidade")
    else:
        print(f"\n[SUCESSO]: Densidade do Material: {densidade:.2f} em kg/m³")
    finally:
        print("--- Encerrando o cálculo da densidade ---")

#Main
while True: #só para executar várias vezes na demonstração
    executar_analise_densidade()
    print("\n")


