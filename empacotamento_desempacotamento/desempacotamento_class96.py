# Desempacotamento em chamadas 

string = "ABCD"
lista = ["Maria", "Helena", 1, 2, 3, "Eduarda"]
tupla = "Python", "é", "legal"

# a, b, c, *_ = lista
# print(a, c)

for nome in lista:
    print(nome, end=" ") #tudo em uma linha só

print(*lista) #tudo em uma linha só tbm