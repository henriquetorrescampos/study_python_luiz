d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

d2 = d1.copy() # shallow copy, 

d2['c1'] = 10

print(d1)
print(d2)