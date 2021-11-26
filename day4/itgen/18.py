# list, set, dict
# no tuple comprehension 

lista = [11, 22, 33, 44, 55]

listb = [x**2 for x in lista]
listc = (x**2 for x in lista)

print("listb =", listb)
print("listc =", listc)


