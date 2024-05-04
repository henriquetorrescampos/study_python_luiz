### Printe os valores para mostrar o resultado correto. ### Encontre os valores pares na lista abaixo 
pair_numbers_list = [1,2,8,12,17,18,25,26,32,33,34,35,39,40,45,58,95,112,248] 
pair_numbers = [] 
for number in pair_numbers_list:
     if number % 2 == 0: 
         pair_numbers.append(number) 
print(pair_numbers) 

### Encontre quantas vezes os valores se repetem na lista abaixo: ### Ex: list = [1,1,1,2,4,4,6,6,7,7,7,7,7,9]
### result = {1 : 3, 2 : 1, 4: 2, 6: 2, 7: 5, 9: 1}
repeated_list = [1,1,1,1,1,2,2,4,4,4,4,4,4,6,6,7,7,7,7,7,9,10,10,10] 
repeated_dic = {} 
for repeated in repeated_list: 
    if repeated in repeated_dic.keys(): 
        print(repeated_dic.keys()) 
        repeated_dic[repeated] += 1 
    else: 
        repeated_dic[repeated] = 1 
print(repeated_dic)