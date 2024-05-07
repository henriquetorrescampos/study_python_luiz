"""cria uma funcao que multiplica todos os argumentos nao nomedados recebidos
retorne o total para uma variavel e mostre o valor 

crie uma funcao fala se um numero e par ou impar
retorne se o numero e par ou impar
"""

# def multiply(*args):
#     multiply = 1
#     for num in args:
#         multiply *= num
#     return multiply

# new_multiply = multiply(1, 2, 3, 4, 5)
# print(new_multiply)


def odd_even(n):
    multiplo_de_dois = n % 2 == 0

    if multiplo_de_dois:
        return (f'{n} e par')
    return (f'{n} e impar')

new_odd_even = odd_even(3)
print(new_odd_even)
