"""
args = argumentos nao nomeados
*args empacotamento e desempacotamento
"""

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

def sum(*args): # args: sem precisa nomear o argumento, tupla
    count = 0
    for num in args:
        count += num
        print(num)

sum(1, 2, 3, 4, 5, 6)