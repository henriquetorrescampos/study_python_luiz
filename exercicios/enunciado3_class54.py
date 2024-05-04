#Exercise 3

name = input("Digite seu nome: ")
quantidade_letras_name = len(name)

if quantidade_letras_name <= 4:
    print(f"Seu nome tem {quantidade_letras_name}, é curto.")
elif quantidade_letras_name <= 6:
     print(f"Seu nome tem {quantidade_letras_name}, é normal.")
else:
     print(f"Seu nome tem {quantidade_letras_name}, é grande.")
