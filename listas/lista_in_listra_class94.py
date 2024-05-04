"""
Lista de listas e seus índices
Em uma lista é importante deixar todos os itens do mesmo tipo
"""

salas = [
    # 0          1
    ["Maria", "Helena",], # 0
    # 0
    ["Elaine",], # 1
    # 0        1         2                 3
    ["Luiz", "João", "Eduarda",], # 2
]

# print(salas[0][1])
# print(salas[1][0])
# print(salas[2][3][2])


for sala in salas: 
    print(f"A sala é {sala}")
    for aluno in sala:
        print(aluno)


