class Car:
	def __init__(self,carname,carmodel,carcolor):
		self.carname=carname
		self.carmodel=carmodel
		self.carcolor=carcolor

	def carinfo(self):
		print(self.carname, self.carmodel, self.carcolor)

class Emp:
	def __init__(self,eno,ename,car):
		self.eno=eno
		self.ename=ename
		self.car=car
	def empinfo(self):
		print(self.eno)
		print(self.ename)
		self.car.carinfo()
c=Car('Benz','1000v','Black')
e=Emp('100','Kalyan',c)
e.empinfo()