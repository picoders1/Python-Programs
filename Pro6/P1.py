class Student:
    def hello(self,name=None,age=None):
        if name is not None and age is None:
            print("Hello "+ name)
        elif name is not None and age is not None:
            print("Hello "+name+" your age is "+age)
        else:
            print("Hello")
obj=Student()
obj.hello()
obj.hello("Piku")
obj.hello("Piku","22")