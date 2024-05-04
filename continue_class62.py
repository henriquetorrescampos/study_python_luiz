# break e continue, usado parao while mais proximo


count = 0

while count <= 100:
    count += 1
    
    if count == 6:
        print("nao vou mostrar o 6")
        continue
    print(count)

    if count == 40:
        break