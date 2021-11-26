def funca():
	n=1
	yield n

	n = n+1
	yield n

	n = n+1
	yield n

x = funca()

print(next(x))
print(next(x))
print(next(x))
print(next(x))


