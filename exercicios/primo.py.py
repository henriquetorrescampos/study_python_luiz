def primo_check(numero):
    primo = True
    # for i in range(2, numero):
    #     if numero % i == 0:
    #        primo = False
    # if primo:
    #     print("Número primo")
    # else:
    #     print("Número não primo")
    
    
    if numero > 1:
        i = 0
        while numero <= i:
            if numero % i == 0:
                primo = False
        if primo:
            print("primo") 
        else: 
            print("nao primo")
        i += 1
    else:
        print("Número digitado menor que 1.")
    

n = int(input("Digite um número: "))
primo_check(numero=n)




