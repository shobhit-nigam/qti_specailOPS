import sys

class Avenger:
	ranking = 0
	strength = None

	def fight():
		print("uses", strength)


hulk = Avenger()
DrStrange = Avenger()

print(sys.getsizeof(hulk))
print(sys.getsizeof(Avenger))
