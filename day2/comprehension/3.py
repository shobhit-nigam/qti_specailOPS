lista = [10, 20, 30, 40, 50]

listb = []

for val in lista:
    if val%20 == 0:
        listb.append("xxx")
    elif val%3==0:
        listb.append("yyy")
    else:
        listb.append("zzz")

listc = ["xxx" if val%20 == 0 else "yyy" if val%3==0 else "zzz" for val in lista]

print("lista =", lista)
print("listb =", listb)
print("listc =", listc)
