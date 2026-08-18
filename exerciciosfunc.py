"""
#exercicio 1
Escreva um programa em Python para calcular o salário de um
funcionário. Implemente uma função calcular-salario que permita
receber o salário atual de um funcionário e retorna o salário
com reajuste de aumento, sendo que:
- caso o salário seja maior que 2k, o funcionário receberá
7% de aumento
- caso contrário, o funcionário receberá 15% de aumento
"""

def calcular_salario(salario:float) -> float:
    """
    Esta função permite o usuário informar seu salário atual e saber
    quantos % de aumento ele receberá, além de saber seu salário final com reajuste
    """
    if salario > 2000:
        print("Seu salário receberá um aumento de 7%")
        return salario + (salario * 7 / 100)
    else:
        print("Seu salário receberá um aumento de 15%")
        return salario + (salario * 15 / 100)

#Main
salario = float(input("Qual é o seu salário atual? "))
ajuste = calcular_salario(salario)
print(f"Salário com ajuste de aumento: R${ajuste:.2f}")


#exercicio 2
def cps(cp1:float, cp2:float, cp3:float) -> float:
    """
    Esta função recebe 3 notas de CPs, mantem as duas maiores (exclui a menor) e
    calcula a média delas
    :param cp1: float
    :param cp2: float
    :param cp3: float
    :return: float
    """
    li_cps = [cp1, cp2]
    li_cps.sort() #deixa a lista em ordem crescente
    if li_cps[0] < cp3:
        li_cps[0] = cp3
    mcps = (li_cps[0] + li_cps[1]) / 2
    print(li_cps)
    return mcps

def sprints(sp1:float, sp2:float) -> float:
    """
    Esta funcao recebe a nota das duas Sprints Semestrais e calcula a média delas
    :param sp1: float
    :param sp2: float
    :return: float
    """
    media_sprints = (sp1 + sp2) / 2
    return media_sprints

def globals() -> float:
    """
    Esta funcao recebe a nota da Global Solution e a retorna
    :return: float
    """
    gs = float(input("Digite sua nota da Global Solution: "))
    return gs




#Main
#1 Semestre
cp1 = float(input("Digite a nota da 1° CP: "))
cp2 = float(input("Digite a nota da 2° CP: "))
cp3 = float(input("Digite a nota da 3° CP: "))
m_cps = cps(cp1, cp2, cp3)
print(f"Média CPs: {m_cps}")
f_cps = m_cps* 0.2
print(f"Média Final (20%) da CPs: {f_cps:.2f}")

sp1 = float(input("Digite a nota da 1° Sprint: "))
sp2 = float(input("Digite a nota da 2° Sprint: "))
m_sprints = sprints(sp1,sp2)
print(f"Média Sprints: {m_sprints}")
f_sprints = m_sprints* 0.2
print(f"Média Final (20%) da Sprints: {f_sprints:.2f}")

notags1 = globals()
print(f"Nota Global Solution 1: {notags1}")
notags1f = notags1* 0.6
print(f"Nota Final (60%) da Global Solution 1: {notags1f:.2f}")


msemestre1 = f_cps + f_sprints + notags1f
print(f"Sua média do 1° Semestre: {msemestre1:.2f}")

#2 Semestre
cp1_2 = float(input("Digite a nota da 1° CP: "))
cp2_2 = float(input("Digite a nota da 2° CP: "))
cp3_2 = float(input("Digite a nota da 3° CP: "))
m2_cps = cps(cp1_2, cp2_2, cp3_2)
print(f"Média CPs: {m2_cps}")
f2_cps = m2_cps* 0.2
print(f"Média Final (20%) da CPs: {f2_cps:.2f}")

sp3 = float(input("Digite a nota da 3° Sprint: "))
sp4 = float(input("Digite a nota da 4° Sprint: "))
m2_sprints = sprints(sp3,sp4)
print(f"Média Sprints: {m2_sprints}")
f2_sprints = m2_sprints* 0.2
print(f"Média Final (20%) da Sprints: {f2_sprints:.2f}")

notags2 = globals()
print(f"Nota Global Solution 1: {notags2}")
notags2f = notags2* 0.6
print(f"Nota Final (60%) da Global Solution 2: {notags2f:.2f}")


msemestre2 = f2_cps + f2_sprints + notags2f
print(f"Sua média do 2° Semestre: {msemestre2:.2f}")

#Média Final
media_final = (msemestre1 * 0.4) + (msemestre2 * 0.6)
print(f"Sua Média Final desse ano é: {media_final:.2f}")
