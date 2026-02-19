class Student:
    clg="iter"
    def __init__(self):   # constructor   but in java and c++ constructor same as classname
        self.name="muna" # instance variable  object data 
        self.rollno=1
s=Student() # object create  got where constrcutor 
print("my name=",s.name)
print("my rollno=",s.rollno)
print("clg name=",s.clg)
s1=Student()
print("my name =",s1.name)
print("my name =",s1.rollno)
print("my name =",s1.clg)
