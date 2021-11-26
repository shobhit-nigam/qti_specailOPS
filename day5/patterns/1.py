# singleton
# maintain state

class SingletonMain():
	__state = dict()   #2000

	def __init__(self):
		self.__dict__ = self.__state #2000
		self.data = "monday"         # varies for every object

	def display(self):
		print("data id =", id(self.data))
		print("__dict__ id =", id(self.__dict__))

objs = SingletonMain()
objt = SingletonMain()

print(objs.data)
print(objt.data)

print("---")
objs.data = "tuesday"


print(objs.data)
print(objt.data)
objs.display()
print("---")

obju = SingletonMain()
obju.data = "wednesday"

print("---")

print(objs.data)
print(objt.data)
print(obju.data)
objs.display()

