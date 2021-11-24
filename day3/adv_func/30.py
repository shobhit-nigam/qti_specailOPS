lista = [10, 20, 30, 40, 50]
listb = [40, '', 'Hello', None, 0, 0.0, [], False, 60, [12, 13]]

liste = list(filter(None, listb))
print(liste)
