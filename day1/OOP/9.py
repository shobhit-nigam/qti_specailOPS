import sys

class Avenger:
	ranking = 0
	strength = None

	def fight(self):
		# uses the string strength
		print("uses", strength)


hulk = Avenger()
# removed the refernece 
hulk.ranking = 30
print("Avenger.ranking =", Avenger.ranking)

Avenger.ranking = 100
print("----")
print("Avenger.ranking =", Avenger.ranking)
print("----")

DrStrange = Avenger()

print("hulk.ranking =", hulk.ranking)
print("----")
print("DrStrange.ranking =", DrStrange.ranking)
print("----")
