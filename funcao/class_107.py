"""
Valores padrao para parametros. 
Ao definir uma funcao, os paramaetros podem ter valores padrao.
Caso o valor nao seja enviado para o parametro o valor padrao sera usado.
"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}, x + y + z')
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(9, 4, 3)
soma(y=9, z=0, x= 5)