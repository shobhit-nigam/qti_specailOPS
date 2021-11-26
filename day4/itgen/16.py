# pseudo code

for x in iterable:
	# do something 


obji = iter(iterable)
while True:
	try:
		val = next(obji)
	except StopIteration:
		break
	 
