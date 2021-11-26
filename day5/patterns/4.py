from abc import ABC, abstractmethod
import numpy as np

class Subject(ABC):
	"subscriber management"

	@abstractmethod
	def attach(self, observer):
		# attaching an observer to the Subject
		pass
	
	@abstractmethod
	def detach(self, observer):
		# attaching an observer to the Subject
		pass
	
	@abstractmethod
	def notify(self):
		# notify all observers 
		pass

class ActualSubject(Subject):
	__state = None
	__observer = []

	def attach(self, ob):
		print("attached an observer")
		self.__observer.append(ob)

	def detach(self, ob):
		print("detach an observer")
		self.__observer.remove(ob)

	def notify(self):
		print("notifying subscribers")
		for x in self.__observer:
			x.update(self)

	def appl_logic(self):
		print("some essential activity")
		self.__state = np.random.randint(50, 150)
		
		print("state has change to", self.__state)
		self.notify()

class Observer(ABC):
	@abstractmethod
	def update(self, sb):
		pass

class ActualObserver_one(Observer):
	def update(self, sb):
		if sb.__state < 100:
			print("observer one reacted to event")
	
class ActualObserver_two(Observer):
	def update(self, sb):
		if sb.__state >= 100:
			print("observer two reacted to event")
	
objs = ActualSubject()

ob_a = ActualObserver_one()
objs.attach(ob_a)

ob_b = ActualObserver_two()
objs.attach(ob_b)

objs.appl_logic()
objs.appl_logic()

objs.detach(ob_a)

objs.appl_logic()
objs.appl_logic()		
