import numpy as np

# numeric python

lista = [10, 23, 40, 27]
listb = [11, 15, 10, 31]
listc = [15, 11, 21, 10]

na = np.array([lista, listb, listc])

nb = na.reshape(2, 3, 2)
print(na)

print(na.ndim)
print(na.shape)

print(nb)

print(nb.ndim)
print(nb.shape)
