lista = []

while True:
    option = input("Selecione uma opção:\n[i]nserir [a]pagar [l]istar ")

    if option == "i":
        valor = input("Valor: ")
        lista.append(valor)
    elif option == "a":
        indice_str = input("Escolha o índice para apagar: ")

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print("Digite numero inteiro: ")
        except IndexError:
            print("Não foi possível apagar este índice.")
        except Exception:
            print("Erro desconhecido.")
    elif option == "l":
        if len(lista) == 0:
            print("Não há nada para listar")

        for posicao, valor in enumerate(lista):
            print(posicao, valor)
    else:
        print("Digite i, a ou l. ")