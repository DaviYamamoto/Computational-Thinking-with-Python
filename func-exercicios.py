#exercicio 2
'''def triangular(num):
    i = 1
    while True:
        if i * (i + 1) * (i + 2) == num:
            return True
        elif i * (i + 1) * (i * 2) > num:
            return False
        i += 1

#Main
n = int(input("Informe um número para verificar se é triângular: "))
if triangular(n):
    print(f"O número {n} é triângular!")
else:
    print(f"O número {n} não é triângular.")

#exercicio 3
import random
def randomss():
    nums = [0,0,0,0,0,0]
    for i in range(1000000):
        x = random.randint(1, 6)
        match x:
            case 1:
                nums[x - 1] += 1
            case 2:
                nums[x - 1] += 1
            case 3:
                nums[x - 1] += 1
            case 4:
                nums[x - 1] += 1
            case 5:
                nums[x - 1] += 1
            case 6:
                nums[x - 1] += 1
    return nums

#Main
nums = randomss()
for i in range(len(nums)):
    print(f"O número {i + 1} apareceu {nums[i]} vezes.")
'''

#exercicio 4
import math
def bhaskara():
    a = float(input("Informe o primeiro número: "))
    b = float(input("Informe o segundo número: "))
    c = float(input("Informe o terceiro número: "))
    x = (b**2) - (4*a*c)
    if a == 0 or b == 0 or c ==0:
        print("Não existe raízes reais")
    elif x< 0:
        print("Não existe raízes reais")
    else:
        x1 = (-b + math.sqrt(x)) / (2 * a)
        x2 = (-b - math.sqrt(x)) / (2 * a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

bhaskara()
