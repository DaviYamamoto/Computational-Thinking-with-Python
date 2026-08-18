'''
def nome_funcao(arg1:tipo, arg2:tipo, arg3:tipo) -> tipo_retorno
'''
def exibir_dados(nome:str, idade:int, altura:float) -> None:
    print(f"{nome} tem {idade} anos e {altura} de altura")

def somar_numeros(n1:float, n2:float) -> float:
    """
    Esta função recebe dois números do tipo float e
    retorna a soma desses dois números.

    Parâmentros: (float, float)
    Retorno: float
    """
    return n1 + n2


#Main()
exibir_dados("Memphis Depay", 32, 1.88)
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))

resultado = somar_numeros(n1, n2)

print(f"Resultado: {resultado}")


"""
DOCSTRING
- Tem como objetivo explicar o funcionamento de uma função
- É um comentário sempre documentado na primeira linha
- Deve estar entre 3 aspas duplas
- Objetivo: Contribuir para a documentação de um código fonte e melhorar o seu atendimento

ANOTAÇÕES DE TIPO
- Anotações de tipo (type hint) são utilizadas para indicar os tipos de dados das variáveis (parâmetros das funções)
- Objetivo: Tornar o código mais legível e organizado
"""

def somar(a:float, b:float) -> float:
    """
    Esta função realizada a soma de dois números (float)
    e retorna o resultado
    """
    return a + b

def media(a:int, b:int, c:int) -> float:
    """
    Esta função realiza a média aritmética de 3 números (int)
    e retorna o resultado
    """
    if type(a) == int and type(b) == int and type(c) == int:
        m = (a + b + c) / 3
        return m
    else:
        print("Erro: Todos os números devem ser inteiros (int)")
        return None

def entrada_dados() -> int:
    """
    Esta função permite o usuário digitar um número e retorná-lo
    """
    n = int(input("Número: "))
    return n

#Main
result1 = somar(5, 10)
print(f"Soma: {result1}")
n1 = entrada_dados()
n2 = entrada_dados()
n3 = entrada_dados()
result2 = media(n1, n2, n3)
print(f"Média: {result2}")
