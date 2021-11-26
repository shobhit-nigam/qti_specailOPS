# iterator protocol 
# iter()
# __iter__() __next__()

lista = [11, 22, 33]

it = iter(lista)

print(type(it))

print(next(it))
print(next(it))
print(next(it))

#error
print(next(it))
