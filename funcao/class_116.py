"""
Closure e funcoes que retornam outras funcoes
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

s1 = criar_saudacao('bom dia')
s2 = criar_saudacao('bom dia')

print(s1('ronaldo'))
print(s2('ricardo'))

