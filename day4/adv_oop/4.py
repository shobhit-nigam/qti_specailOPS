class Celsius:
	def __init__(self, temp=0):
		self.set_temp(temp)

	def to_far(self):
		return self.get_temp() * (9/5) + 32
	
	def get_temp(self):
		return self.__temp

	def set_temp(self, val):
		if val < -273.25:
			stra = "temperature beyond absolute zero not possible"
			raise ValueError(stra)
		self.__temp = val


today = Celsius(27)

print("in cel =", today.get_temp())
print("in far =", today.to_far())

today.set_temp(30)
print("in cel =", today.get_temp())

#error
today.set_temp(-295)
