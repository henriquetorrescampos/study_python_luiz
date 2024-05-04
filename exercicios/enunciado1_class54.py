#Exercise 1
number = input("Digite um número inteiro: ")

# try:
#     new_number = int(number)
#     if new_number % 2 == 0:
#         print(f"O número {new_number} é par.")
#     else:
#         print(f"O número {new_number} é ímpar.")
# except:
#     print(f"O número {number} não é inteiro.")

#Second way
if number.isdigit():
    new_number = int(number)
    if new_number % 2 == 0:
        print(f"O número {new_number} par.")
    else:
        print(f"O número {new_number} impar")
else:
    print(f"O numero {number} não é inteiro")
