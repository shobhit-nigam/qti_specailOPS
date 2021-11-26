class SingletonMain:
	__instance__ = None	
	def __init__(self):
		if SingletonMain.__instance__ is None:
			SingletonMain.__instance__ = self
		else:
			raise Exception("can not create new object")
	
objs = SingletonMain()
print("created objs")

print("------")

objt = SingletonMain()
print("created objt")

