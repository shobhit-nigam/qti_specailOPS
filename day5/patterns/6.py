from abc import ABC, abstractmethod

class Creator(ABC):
	
	@abstractmethod
	def method_f(self):
		pass

	def some_operation(self):
		product = self.method_f()
		
		res = f"creator's code worked with {product.operation()}"
		return res

class Concreate_A(Creator):
	def method_f(self):
		return ConcreteProduct_A()

class Concreate_B(Creator):
	def method_f(self):
		return ConcreteProduct_B()


class Product(ABC):
	"opertaion that concrete products implement"

	def operation(self):
		pass

class ConcreteProduct_A(ABC):
	def operation(self):
		return "result of Concrete_product_A"

class ConcreteProduct_B(ABC):
	def operation(self):
		return "result of Concrete_product_B"


######### client code
def client_code(ct):
	print(f"not aware about Creator's class")
	print(f"{ct.some_operation()}")

print("application launched with Concrete_A")
client_code(Concreate_B())
print("----")
print("application launched with Concrete_B")
client_code(Concreate_B())




