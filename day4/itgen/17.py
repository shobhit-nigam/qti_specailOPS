def funca():
	n=1
	yield n

	n = n+1
	yield n

	n = n+1
	yield n

print(type(funca))
