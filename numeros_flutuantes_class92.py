"""
Imprecisão de ponto flutuante
double-precision floating-point format
Se precisar a precisa de um numero 0,00000001 
precisa utilizar o import decimal/ decimal.Decimal("numero")
"""

import decimal

numero1 = 0.1933
numero2 = 0.7
numero3 = numero1 + numero2
print(numero3)
print(f"{numero3:.2f}")
print(round(numero1, 2))
