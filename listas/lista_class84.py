"""
Cuidados com dados mutáveis
"=" copiado o valor (imutáveis)
"=" aponta para o mesmo valor na memória (mutável)
"""

lista_a = ["Henrique", "Lara"]
lista_b = lista_a.copy()

lista_a[0] = "Ronaldo"
print(lista_a)
print(lista_b)