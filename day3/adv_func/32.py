lista = [10, 20, 30, 40, 50]
listb = [40, 50, 60, 70, 80, 90, 100, 110]

liste = list(filter(lambda x: x%40!=0 and x%50!=0, listb))

print(liste)
