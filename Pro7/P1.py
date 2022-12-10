class Employee:
    def setData(self):
        self.first=input("Enter First Name:")
        self.last=input("Enter Last Name:")
        self.empid=input("Enter ID:")
    def apply_raise(self):
        self.raise_amt = int(input("Enter Raise amount:"))
        self.pay = int(input("Enter Pay Amount:"))
        self.pay=self.pay+self.raise_amt
    def display(self):
        print("First Name:",self.first)
        print("Last Name:",self.last)
        print("Employee ID:",self.empid)
        print("Pay:",self.pay)
class Developer(Employee):
    def apply_raise(self):
        self.raise_amt = int(input("Enter Raise amount:"))
        self.pay = int(input("Enter Pay Amount:"))
        self.pay = self.pay + self.raise_amt
class Manager(Employee):
    def apply_raise(self):
        self.raise_amt = int(input("Enter Raise amount:"))
        self.pay = int(input("Enter Pay Amount:"))
        self.pay = self.pay + self.raise_amt

man={}
dev={}
n=int(input("Enter Number of Employee:"))
for i in range(n):
    print("1.Enter Manager Data:")
    print("2.Enter Developer Data:")
    print("3.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        e1=Manager()
        e1.setData()
        e1.apply_raise()
        man[i]=e1.__dict__
    elif ch==2:
        e2 = Developer()
        e2.setData()
        e2.apply_raise()
        dev[i] = e2.__dict__
    elif ch==3:
        break
    else:
        print("Invalid Input please try again")

print(man)
print(dev)
