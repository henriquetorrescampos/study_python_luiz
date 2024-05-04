"""
Listas em Python
TIpo list = mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, ...+
append = adiciona um valor no final
insert = adiciona um valor na posição escolhida
pop = remove do final ou do índice escolhido
del = apaga um valor em uma posição
clear = limpa a lista
extend = estende a lista
Criar/Ler/Alterar/Apagar = lista[i] chama de CRUD
É interessante que se remova ou adiciona algo na lista no último item
"""
#         0,   1,    2,                 3,   4
#         -5,  -4,   -3,               -2,  -1
# lista = [123, True, "Henrique Torres", 1.2, []]
# lista.append = "Maria"
# print(lista)
#         0   1   2   3
lista = [10, 20, 30, 40]
lista.append("Henrique")
lista.insert(0, 5) # adiciona um valor na lista (posição, valor)
print(lista)