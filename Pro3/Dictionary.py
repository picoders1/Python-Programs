d = {}
class employee():
    def add_emp(self):
        self.name = input("enter employee name: ")
        self.address = input("enter employee address: ")
        self.pan = input("enter pan number: ")
        self.basic = int(input("enter basic salary: "))
        self.tds = int(input("enter tds: "))
        self.ded = int(input("enter deduction: "))
        self.hra = 1.25 * self.basic
        self.da = 0.25 * self.basic
        self.gross_sal = self.basic + self.hra + self.da
        self.net_sal = self.basic - self.ded

    def search_emp(self, name):
        flag = 0
        for key in d:
            if key == name:
                print("EMPLOYEE FOUND")
                for i in d[key]:
                    print(i, d[key][i])
                    flag = 1
        if flag == 0:
            print("EMPLOYEE NOT FOUND")

    def print_emp(self):
        for key in d:
            print(key, d[key])

while True:
        print("1.Add employee")
        print("2.Search an employee")
        print("3.Print employee details")
        print("4.Update employee details")
        print("5.EXIT")
        em = employee()
        ch = int(input("enter your choice:"))
        if ch == 1:
            em.add_emp()
            d[em.name]=em.__dict__
        elif ch == 2:
            name = input("enter employee name to search:")
            em.search_emp(name)
        elif ch == 3:
            em.print_emp()
        elif ch == 4:
            name = input("enter employee name to update:")
            em.add_emp()
            for key in d:
                if key==name:
                    d[em.name]=em.__dict__
        elif ch==5:
            break
        else:
            print("Invalid Input please try again!")
