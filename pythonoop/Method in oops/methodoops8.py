class Simpleinterest:
	"""docstring for Simpleinterest"""
	def __init__(self):
		self.pr=int(input("enter principal amount "))
		self.r=int(input("enter rate of interest "))
		self.t=int(input("enter time period "))
	def show(self):
		print("principal amount=",self.pr)
		print("rate of interest=",self.r)
		print("time period=",self.t)
	def simpleinterest(self):
		return (self.pr*self.r*self.t)/100
d=Simpleinterest()
d.show()
#d.simpleinterest()
print("Simpleinterest=",d.simpleinterest())
