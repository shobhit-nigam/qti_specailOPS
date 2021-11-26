import numpy as np

# numeric python

lista = [13, 23, 33, 44]
listb = [11, 15, 10, 31]
listc = [19, 29, 39, 49]

na = np.array([lista, listb, listc])
print(na)

print(na[:, 1:3])

print(na[-2:, 1:3])
