while True:
    print("1.Check Divisible By Zero Exception")
    print("2.Check Value Error")
    print("3.Check Name Error")
    print("4.Check Index Error")
    print("5.Check Attribute Error")
    print("6.Check Keyboard Interrupted")
    print("0.Exit")
    n=int(input("Enter Choice:"))
    if n==1:
        try:
            # When n1=11, n2=0 then generate (ZeroDivisionError)
            # when n1=11,n2=12 then O/P:- Successfully
            n1 = int(input("Enter First Number:"))
            n2 = int(input("Enter Second Number:"))
            c=n1/n2
            print("Successfully")
        except ZeroDivisionError:
            print("Zero Divisible Error")
    elif n==2:
        try:
            # when a="Hello" then generate (value Error)
            # when a=22 then ) O/P:-Successfully
            a=int(input("Enter Integer Data:"))
            print("Successfully")
        except ValueError:
            print("Value Error")
    elif n==3:
        try:
            # When n1=33 , n2="Hello" the generate TypeError
            n1 = int(input("Enter First Number:"))
            n2 = input("Enter String:")
            c = n1 + n2
            print("Successfully")
        except TypeError:
            print("Type Error")
    elif n==4:
        try:
            list1=[11,22,33]
            print(list1[2])
            print(list1[5])
            print("Successfully")
        except IndexError:
            print("Index Error")
    elif n==5:
        try:
            X = 10
            X.append(6)
            print("Successfully")
        except AttributeError:
            print("Attribute Error")
    elif n==6:
        try:
            raise KeyboardInterrupt
            print("Successfully")
        except KeyboardInterrupt:
            print("Keyboard interrupt exception caught")
    elif n==0:
        break
    else:
        print("Invalid input Please try again ")


