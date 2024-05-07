"""
Escopo de funcoes em Python
Escopo significa o local onde aquele codigo pode atingit
Existe o escopo global e local
O escopo global é o escopo onde todo o codigo é alcancavel
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados
"""
x = 1

def escopo():
    # x = 10

    # def another_function():
    #     y = 2 # essa função consegue acessar o x
    #     x = 5
    #     print(x, y)
    # another_function()
    print(x)

print(x)
escopo()
print(x)
