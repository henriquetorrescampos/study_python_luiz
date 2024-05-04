"""
enumerate - enumera iteráveis (posições)
enumera cada valor na sua lista
"""

lista = ["Maria", "Helena", "Luiz"]
lista.append("João")


for posicao, nome in enumerate(lista):
    print(posicao, nome)
    