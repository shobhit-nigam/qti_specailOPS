
#check = lambda x: True if (type(x) is int) else False
check = lambda x: type(x) is int

print(check(11))
print(check(23.78))
print(check([111, 22, 33]))
