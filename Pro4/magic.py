class magic:
    def __init__(self):
        self.l = []

    def input(self):
        no = int(input("Enter length of list data:"))
        if not no:
            print("invalid input")
        else:
            for i in range(0, no):
                ele = int(input("enter element:"))
                self.l.append(ele)

    def __add__(self, other):
        ans = []
        if len(self.l) == len(other.l):
            for i in range(len(self.l)):
                ans.append(self.l[i]+other.l[i])
            print(ans)
        else:
            print("input not accepted")

    def __sub__(self, other):
        ans = []
        if len(self.l) == len(other.l):
            for i in range(len(self.l)):
                ans.append(self.l[i]-other.l[i])
            print(ans)
        else:
            print("input not accepted")

    def __mul__(self, other):
        ans = []
        if len(self.l) == len(other.l):
            for i in range(len(self.l)):
                ans.append(self.l[i]*other.l[i])
            print(ans)
        else:
            print("input not accepted")

    def __truediv__(self, other):
        ans = []
        if len(self.l) == len(other.l):
            for i in range(len(self.l)):
                ans.append(self.l[i]/other.l[i])
            print(ans)
        else:
            print("input not accepted")