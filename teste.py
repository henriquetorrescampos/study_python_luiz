soma = 0
n = int(input("Numero? "))

while n >= 0:
    soma = soma + n
    if soma >= 100:
        soma = 0
        n1 = int(input("Numero2? "))
print(soma)