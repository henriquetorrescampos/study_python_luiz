"""
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""

condicao = 10 == 10
variavel = "Valor" if condicao else "outro valor"
print(variavel)

digito = 9
new_digito = digito if digito <= 9 else 0
new_digito = 0 if digito > 9 else digito
print(new_digito)


