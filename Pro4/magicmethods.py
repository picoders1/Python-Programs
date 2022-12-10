from magic import *
ob = magic()
ob1 = magic()
ob.input()
ob1.input()


while True:
    print("1-add \n2-sub\n3-mul\n4-div\n5-exit ")
    ch = int(input("enter your choice:"))
    if ch == 1:
        ob+ob1
    elif ch == 2:
        ob-ob1
    elif ch == 3:
        ob*ob1
    elif ch == 4:
        ob/ob1
    elif ch == 5:
        break
    else:
        print("Invalid input please try again")