import sys

class Avenger:
	ranking = 0
	strength = None

	def fight(ttt):
		print("uses", ttt.strength)


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
