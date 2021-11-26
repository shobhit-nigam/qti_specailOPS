import weakref
class Celsius:
	def __init__(self, temp=0):
		self.temp = temp
	
today = Celsius()
fri = weakref.ref(today)
thu = today
# sat = weakref.ref(tom)

print(tom is today)
print(tom is today.__weakref__)
