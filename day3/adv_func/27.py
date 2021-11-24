lista = [10, 20, 30, 40, 50]
listb = [40, 50, 60, 70, 80, 90, 100, 110]

def calc(la, lb):
    return 2*la + lb**2 - 10

liste = list(map(lambda la, lb: 2*la+lb**2-10, lista, listb))

print(liste)
