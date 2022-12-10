class Parent:
    def __init__(self):
        self.__name = None
        self.__USN = None
        self.__m1 = None
        self.__m2 = None
        self.__m3 = None
        self.__m4 = None
        self.__m5 = None

    def set_name(self,name):
        self.__name=name
    def set_usn(self,USN):
        self.__USN=USN
    def set_marks(self,m1,m2,m3,m4,m5):
        self.__m1=m1
        self.__m2 = m2
        self.__m3 = m3
        self.__m4 = m4
        self.__m5 = m5
    def get_name(self):
        return self.__name
    def get_usn(self):
        return self.__USN
    def get_marks(self):
        return self.__m1,self.__m2,self.__m3,self.__m4,self.__m5

class Child(Parent):
    def view(self):
        print("Name:", ob.get_name(), "\nUSN:", ob.get_usn())
        marks=ob.get_marks()
        total=marks[0]+marks[1]+marks[2]+marks[3]+marks[4]
        print("Total Marks:",total)
        avg = total / 5
        if avg >= 91 and avg <= 100:
            print("Your grade is S")
        elif avg >= 81 and avg < 91:
            print("Your grade is A")
        elif avg >= 71 and avg < 81:
            print("Your grade is B")
        elif avg >= 61 and avg < 71:
            print("Grade C")
        elif avg >= 51 and avg < 61:
            print("Your grade is D")
        else:
            print("Fail")


name = input("Enter name:")
usn = input("Enter USN:")
m1 = int(input("Enter First Marks:"))
m2 = int(input("Enter Second Marks:"))
m3 = int(input("Enter Third Marks:"))
m4 = int(input("Enter Fourth Marks:"))
m5 = int(input("Enter Fifth Marks:"))

ob=Child()
ob.set_name(name)
ob.set_usn(usn)
ob.set_marks(m1,m2,m3,m4,m5)
ob.view()
