lista = [11, 22, 33, 44, 55, 66, 77]

listb = []
for val in lista:
    if val%2 == 0:
        listb.append(val)
    else:
        listb.append(1000)

listc = [val  if val%2 == 0 else 1000 for val in lista]

print("lista =", lista)
print("listb =", listb)
print("listc =", listc)
