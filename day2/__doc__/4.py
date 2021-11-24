class Avenger:
    "defend the earth"
    ranking = 0
    strength = None

    def fight(self):
        print("uses", self.strength)

Avenger.__doc__ = Avenger.__doc__ + "\nalso avenge it sometimes"

help(Avenger)
