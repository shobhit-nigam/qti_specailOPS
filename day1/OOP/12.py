class Bank:

	def __init__(self, an=0, ob=0, name="John Doe"):
		self.accNum = an
		self.opnBal = ob
		self.curBal = self.opnBal
		self.cusName = name
		self.__rating = 0

	def display(self):
		print("welcome", self.cusName)
		print("account balance is", self.curBal)

	def deposit(self, amt):
		self.curBal = self.curBal + amt
		print(f"thank you {self.cusName}, deposit is successful")

	def __calcRating(self):
		# criteria 1
		# criteria 2
		# criteria 3
		self.__rating = round(self.opnBal/1000,1)

	def loan(self):
		self.__calcRating()
		if self.__rating > 0 and self.__rating < 2:
			print("you can get a loan of", self.__rating * 1000)
		elif self.__rating >= 2 and self.__rating < 4:
			print("you can get a loan of", self.__rating * 1500)
		else:
			print("you can get a loan of", self.__rating * 2000)

obja = Bank(65302, 2000, "Benedict")
objb = Bank(65304, 1800, "Chris Evans")

print("----")

obja.loan()
print("-----")


# error
print(obja.__rating)
