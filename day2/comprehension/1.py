lista = [11, 22, 33, 44, 55, 66, 77]

listb = []
for val in lista:
    if val%2 == 0:
        listb.append(val)

listc = [val for val in lista if val%2 == 0]

print("lista =", lista)
print("listb =", listb)
print("listc =", listc)
