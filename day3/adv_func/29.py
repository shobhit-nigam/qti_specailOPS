lista = [10, 20, 30, 40, 50]
listb = [40, 'a', 50, 60, 'Hello', [2, 3, 4], {3, 4}, 12]

def filter_int(lb):
    if type(lb) is int:
        return False
    else:
        return True

liste = list(filter(filter_int , listb))

print(liste)
