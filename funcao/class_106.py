"""
Argumentos nomeados e nao nomeados em funcoes Python
Argumento nomeado tem nome com sinal de igual
Argumento nao nomeado recebe apenas o argumento (valor)
"""

def soma(x, y ,z): #parametro vem da definicao da funcao e a variavel
    #Definicao
    print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z)

soma(1, 2, 3) #argumento e o valor que passa para a variavel para o paramatro
soma(x=2, y=3, z=5) #argumento e o valor que passa para a variavel para o paramatro
# se nomear um argumento é necessario nomear o restante