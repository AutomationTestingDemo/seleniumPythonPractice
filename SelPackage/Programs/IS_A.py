class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def p1(self):
		print("Parent Method")
class Employee(Person):

	def __init__(self,name,age,enum,esal):
		super().__init__(name,age)
		self.enum=enum
		self.esal=esal
	def display(self):
		print(self.name)
		print(self.age)
		print(self.enum)
		print(self.esal)
e=Employee('Kalyan','26','100','90000')
e.p1()
e.display()