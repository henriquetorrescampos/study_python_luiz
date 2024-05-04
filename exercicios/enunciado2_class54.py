#Exercise 2
hours = int(input("Digite as horas: "))
minutes = int(input("Digite os minutos: "))

if hours >= 0 and hours < 12:
    print(f"Bom dia {hours}-{minutes}")
elif hours >= 12 and hours <= 17:
    print(f"Boa tarde {hours}-{minutes}")
else:
    print(f"Boa noite {hours}-{minutes}")


