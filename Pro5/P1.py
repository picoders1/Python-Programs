# Hierarchical inheritance
class Student:
    def getData(self):
        self.name = input("Enter Name:")
        self.usn = input("Enter USN:")
        self.age = int(input("Enter age:"))
class PgStudent(Student):
    def PgGetData(self):
        super().getData()
        self.sem = int(input("Enter Semester:"))
        self.fees = int(input("Enter Fee:"))
        self.stipend = int(input("Enter Stipend:"))
    def display(self):
        print("USN:", self.usn)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Semester:", self.sem)
        print("Fee:", self.fees)
        print("Stipend:", self.stipend)
class UgStudent(Student):
    def UgGetData(self):
        super().getData()
        self.sem = int(input("Enter Semester:"))
        self.fees = int(input("Enter Fee:"))
        self.stipend = int(input("Enter Stipend:"))
    def display(self):
        print("USN:", self.usn)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Semester:", self.sem)
        print("Fee:", self.fees)
        print("Stipend:", self.stipend)
ug={}
pg={}
n=int(input("Enter the number of students:"))
for i in range(n):
    print("1.Enter PG Student Details:")
    print("2.Enter UG Student Details:")
    ch = int(input("Enter Choice:"))
    if ch == 1:
        obj1=PgStudent()
        obj1.PgGetData()
        pg[obj1.name]=obj1._dict_
    elif ch == 2:
        obj2=UgStudent()
        obj2.UgGetData()
        ug[obj2.name]=obj2._dict_

print(ug)
print(pg)

