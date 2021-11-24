lista = [10, 20, 30, 40, 50]
listb = [40, 15, 36, 27, 38]

liste = list(map(lambda x, y: x if x > y else y, lista, listb))

print(liste)
