import sys

class Avenger:
	ranking = 0
	strength = None

	def fight():
		print("uses", strength)


hulk = Avenger()
DrStrange = Avenger()

#error
hulk.fight()

# hulk.fight()
# translates to
# Avenger.fight(hulk)

DrStrange.fight()
# translates to
# Avenger.fight(DrStrange)
