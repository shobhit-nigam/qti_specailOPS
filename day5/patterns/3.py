class SingletonMain:
	__instance__ = None	

	def __init__(self):
		if SingletonMain.__instance__ is None:
			SingletonMain.__instance__ = self
		else:
			raise Exception("can not create new object")

	@staticmethod
	def get_instance():
		if not SingletonMain.__instance__:
			SingletonMain()
		return SingletonMain.__instance__
	
objs = SingletonMain()
print("created objs")

print("------")

objt = SingletonMain.get_instance()
print("created objt")
print(id(objs))
print(id(objt))
print("------")

obju = SingletonMain()
print("created obju")


objt = SingletonMain()
print("created objt")

