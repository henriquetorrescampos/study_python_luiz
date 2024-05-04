"""
Iterável -> str, range, etc
Iterável -> entregar um valor por vez
next -> me entrega o próximo valor
iter -> me entrega seu iterador
"""

texto = "Henrique"
iterador = iter(texto)

# o que for faz de baixo dos panos
while True:
    try:
        letra = next(iterador)
        print(letra) 
    except StopIteration:
        break

