class Celsius:
	def __init__(self, temp=0):
		self.temp = temp

	
today = Celsius()

today.temp = 27

print(today.temp)
