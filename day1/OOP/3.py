import sys

class Avenger:
	ranking = 0
	strength = None

	def fight():
		print("uses", strength)


hulk = Avenger()
DrStrange = Avenger()

print(hulk.strength)
hulk.strength = "smash"
print("----")
print(hulk.strength)
