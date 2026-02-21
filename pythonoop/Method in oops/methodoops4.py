class Demo:
	def show(self):
		print("instance method show")
	@classmethod
	def look(cls):
		print("classmethod look")
    @staticmethod
	def disp():
		print("disp staticmethod")
d=Demo()
d.show()
d.look()
d.disp()
Demo.look()
Demo.disp()		
		