
class Rectangle:
	def __init__(self):   #constrcutor
		self.length=int(input("Enter length of rectangle "))
		self.breadth=int(input("Enter breadth of rectangle "))
	def show(self):
		print("rectangle lenegth= ",self.length)
		print("rectangle breadth= ",self.breadth)
	def area(self):
		print("area of rectangle= ",self.length*self.breadth)
	def perimeter(self):
		return 2*(self.length+self.breadth)
r=Rectangle()
r.show()
r.area()
print("perimeter of rectangle= ",r.perimeter())
print("area of rectangle= ",r.area())
		