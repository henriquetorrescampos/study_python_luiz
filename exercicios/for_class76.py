import os

tentivas = 0
palavra_secreta = "henrique"
letras_acertadas = ""

while True:
    letra_usuario = input("Digite uma letra: ")
    tentivas += 1

    if len(letra_usuario) > 1:
       print("Digite apenas uma letra: ")
       continue

    if letra_usuario in palavra_secreta:
       letras_acertadas += letra_usuario
    print(letras_acertadas)

    palavra_formada = ""
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += "*"

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
    #    os.system("clear")
       print("Parabens acertou.")
       print(f"Foram {tentivas} tentativas.")
       break
       tentivas = 0
       palavra_secreta = "henrique"
       letras_acertadas = ""
    