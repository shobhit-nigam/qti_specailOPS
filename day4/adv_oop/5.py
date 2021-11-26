class Celsius:
	def __init__(self, temp=0):
		self.temp =temp

	def to_far(self):
		return self.temp * (9/5) + 32
	
	def get_temp(self):
		print("getting temp")
		return self.__temp

	def set_temp(self, val):
		print("setting temp")
		if val < -273.25:
			stra = "temperature beyond absolute zero not possible"
			raise ValueError(stra)
		self.__temp = val

	temp = property(get_temp, set_temp)
	
today = Celsius(27)
print("----")
print("in cel =", today.temp)
print("----")
print("in far =", today.to_far())
today.temp = 30
print("in cel =", today.temp)

