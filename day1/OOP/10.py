class Bank:
	accNum = 0
	opnBal = 0
	curBal = opnBal
	cusName = "John Doe"

	def update(self, an, ob, name):
		self.accNum = an
		self.opnBal = ob
		self.curBal = self.opnBal
		self.cusName = name

	def display(self):
		print("welcome", self.cusName)
		print("account balance is", self.curBal)

obja = Bank()
objb = Bank()

obja.update(65302, 2000, "Benedict")

obja.display()
print("-----")
objb.display()
