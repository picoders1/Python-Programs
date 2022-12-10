# Multilevel inheritance
class Student:
    def getdata(self):
        self.usn=input("Enter the USN:")
        self.name=input("Enter the Name:")
        self.age=int(input("Enter the age:"))

class Derived1(Student):
    def getmarks(self):
        super().getdata()
        self.s1=int(input("Enter the subject1 marks:"))
        self.s2=int(input("Enter the subject2 marks:"))
        self.s3=int(input("Enter the subject3 marks:"))
        self.s4=int(input("Enter the subject4 marks:"))
        self.s5=int(input("Enter the subject5 marks:"))
        self.total = self.s1 + self.s2 + self.s3 + self.s4 + self.s5
        self.percent = self.total / 500 * 100

class Derived2(Derived1):
    def display(self):
        print("USN :", self.usn)
        print("Name :", self.name)
        print("Age :", self.age)
        print("Total :",self.total)
        print("Percentage :", self.percent)

d={}
n=int(input("Enter the number of students:"))
for i in range(n):
        d2=Derived2()
        d2.getmarks()
        d[d2.name]=d2._dict_
print(d)
