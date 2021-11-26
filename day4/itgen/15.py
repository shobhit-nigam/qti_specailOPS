def funca(start=0, end=0, step=1):
	n=start
	while(n < end):
		yield n
		n = n + step

for i in funca(3, 7):
	print(i)

