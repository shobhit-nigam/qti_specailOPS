import sys

strength = "nuclear"

class Avenger:
	ranking = 0
	strength = None

	def fight(self):
		# uses the string strength
		print("uses", strength)


hulk = Avenger()
DrStrange = Avenger()

hulk.strength = "smash"

#error
hulk.fight()

# hulk.fight()
# translates to
# Avenger.fight(hulk)

DrStrange.fight()
# translates to
# Avenger.fight(DrStrange)
