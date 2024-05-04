def leapYear(ano): #recebe um parametro
    return (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

print(leapYear(2020)) #argumento

 