class p:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def disp(self):
		print(self.name)
		print(self.age)
class c(p):
	def __init__(self,name,age,num,marks):
		super().__init__(name,age)
		self.num=num
		self.marks=marks
	def display(self):
		self.disp()
		print(self.num)
		print(self.marks)
c = c('Kalyan',26,101,98)
c.display()