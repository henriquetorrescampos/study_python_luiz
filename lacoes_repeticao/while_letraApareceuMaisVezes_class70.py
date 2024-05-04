frase = "Python e uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum."

i = 0
qtd_letra_apareceu = 0
letra_apareceu_mais = ""

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == " ":
        break

    count_letter = frase.count(letra_atual)

    if qtd_letra_apareceu <= count_letter:
        qtd_letra_apareceu = count_letter
        letra_apareceu_mais = letra_atual

    i += 1 

print(f"Letra que apareceu mais vezes foi '{letra_apareceu_mais}'" 
      f" que apareceu {qtd_letra_apareceu}x.")
