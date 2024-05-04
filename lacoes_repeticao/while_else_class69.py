string = "Valorcqualquer"

i = 0
while i < len(string):
    letra = string[i]

    if " " in letra:
        break

    print(letra)
    i += 1
else:
    print("Nao encontrei espaco na string.")
print("Fora do laço while")