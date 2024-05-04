"""
Funções (def) são trechos de código usados para replicar determinada ação ao longo do código
Funções podem receber valores para parâmetros (argumentos) e retornar um valor específico.
Por padrão, funões python retornam none
"""

# def teste(a, b, c): #Parametro é a variavel na função
#     print(a, b, c)

# teste(1, 2, 3) #Argumento é o valor que vc envia para a função

def exemplo(nome="Sem Nome"): # nome é o Parametro
    print(f"Olá, {nome}!")


exemplo("Luiz")  #Luiz é o argumento
exemplo("Maria") #Maria é o argumento
exemplo("Julia") #Julia é o argumento
exemplo()