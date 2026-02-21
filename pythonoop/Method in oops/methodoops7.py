class Square:
	def __init__(self):   #constrcutor
		self.side=int(input("Enter side of the square"))
		
	def show(self):
		print("side of the square=",self.side)
	def area(self):
	    return (self.side*self.side)
d=Square()
d.show()
print("Area of square=",d.area())
