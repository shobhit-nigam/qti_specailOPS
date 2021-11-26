# singleton
# maintain state

class SingletonMain():
	__state = dict()

	def __init__(self):
		self.__dict__ = self.__state
		self.data = "monday"

objs = SingletonMain()
objt = SingletonMain()

print(objs.data)
print(objt.data)

print("---")
objs.data = "tuesday"

print(objs.data)
print(objt.data)

obju = SingletonMain()
obju.data = "wednesday"

print(objs.data)
print(objt.data)
print(obju.data)

