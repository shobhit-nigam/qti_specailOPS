lista = [10, 20, 30, 40, 50]
listb = [40, 50, 60, 70, 80, 90, 100, 110]

def only_vowels(ch):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if ch in vowels:
        return True
    else:
        return False
    # return ch in ['a', 'e', 'i', 'o', 'u']

liste = list(filter(only_vowels , "world peace"))

print(liste)
