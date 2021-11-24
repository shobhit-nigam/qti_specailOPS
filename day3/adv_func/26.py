lista = [10, 20, 30, 40, 50]
listb = [40, 50, 60, 70, 80, 90, 100, 110]

def funca(la):
    return la.upper()

liste = list(map(funca, "hello"))

print(liste)
