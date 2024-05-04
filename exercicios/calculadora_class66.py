"""Calculadora com while"""
while True:
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    operador = input("Digite o operador numerico:(+, -, *, /) ")

    if operador == "+":
        soma = (numero1 + numero2)
        print(soma)
    elif operador == "-":
        menos = (numero1 - numero2)
        print(menos)
    elif operador == "*":
        multiplica = (numero1 * numero2)
        print(multiplica)
    elif operador == "/":
        divisao = (numero1 / numero2)
        print(f"{divisao:.}")
    
    sair = input("Quar sair ? escreva 's': ").lower().startswith("s")
    if sair:
        break


    
