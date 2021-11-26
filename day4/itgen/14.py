def funca():
	n=1
	yield n

	n = n+1
	yield n

	n = n+1
	yield n

for i in funca():
	print(i)

