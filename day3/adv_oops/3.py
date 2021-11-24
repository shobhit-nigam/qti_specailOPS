class Bank:
	accNum = 0
	opnBal = 0
	curBal = opnBal
	cusName = "John Doe"

	def display(self):
		print("welcome", self.cusName)
		print("account balance is", self.curBal)

    @staticmethod
    def water_cooler():
        print("have some water")

obja = Bank()
objb = Bank()
