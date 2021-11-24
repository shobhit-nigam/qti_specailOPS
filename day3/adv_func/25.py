lista = [10, 20, 30, 40, 50]
listb = [40, 50, 60, 70, 80, 90, 100, 110]

def calc(la, lb):
    return 2*la + lb**2 - 10

listc = []
if len(lista) > len(listb):
    for i in range(len(listb)):
        listc.append(calc(lista[i], listb[i]))
else:
    for i in range(len(lista)):
        listc.append(calc(lista[i], listb[i]))

if len(lista) > len(listb):
    listd = [calc(lista[i], listb[i]) for i in range(len(listb))]
else:
    listd = [calc(lista[i], listb[i]) for i in range(len(lista))]


liste = list(map(calc, lista, listb))

print(listc)
print(listd)
print(liste)
