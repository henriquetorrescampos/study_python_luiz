"""
crie funcoes que duplicam, triplicam e quadriplicam o numero recebido de parametro
"""

def multiply(multiplicador):
    def multiply_2(num):
        return multiplicador * num
    return multiply_2

multiply_for_2 = multiply(2)
multiply_for_3 = multiply(3)
multiply_for_4 = multiply(4)

print(multiply_for_2(2))
print(multiply_for_3(3))
print(multiply_for_4(4))