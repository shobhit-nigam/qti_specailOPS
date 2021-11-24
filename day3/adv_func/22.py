lista = [10, 20, 30, 40, 50]
listb = [40, 50, 60, 70, 80]

def calc(la, lb):
    return 2*la + lb**2 - 10

listc = []
if len(lista) > len(listb):
    for i in range(len(listb)):
        listc.append(calc(lista[i], listb[i]))
else:
    for i in range(len(lista)):
        listc.append(calc(lista[i], listb[i]))

print(listc)
