class rangex:
	def __init__(self, num):
		self.num = num

	def __iter__(self):
		self.i = 0
		print("__iter__ called")
		return self

	def __next__(self):
		if self.i < self.num:
			if self.i%2 ==0:
				val = self.i 
				self.i = self.i + 1
				return val
			else:
				self.i = self.i + 1
				return "hey"
		else:
			raise StopIteration

for i in rangex(5):
	print(i)

