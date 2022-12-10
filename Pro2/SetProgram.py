while True:
    print("1-->size of the set")
    print("2-->length of the set")
    print("3-->Add new value")
    print("4-->pop")
    print("5-->Union of two set")
    print("6-->Intersection")
    print("7-->set Difference")
    print("8-->symmetric Difference")
    print("9-->check for a element in a set")
    print("10->print element in a set")
    print("11->clear all data form set")
    print("12->Exit")
    choice=int(input("Enter Choice:"))

    if choice==1:
        set1=set(input("Enter set:").split(" "))
        print("set size:",set1.__sizeof__())
    elif choice==2:
        set1=set(input("Enter set:").split(" "))
        print("set first length:", len(set1))
    elif choice==3:
        set1 = set(input("Enter set:").split(" "))
        print("Set:",set1)
        data=input("Enter data:")
        set1.add(data)
        print(set1)
    elif choice==4:
        set1 = set(input("Enter set:").split(" "))
        print("Set:", set1)
        set1.pop()
        print("set:",set1)
    elif choice==5:
        set1=set(input("Enter first set:").split(" "))
        set2=set(input("Enter second set:").split(" "))
        print(set1|set2)
    elif choice==6:
        set1=set(input("Enter first set:").split(" "))
        set2=set(input("Enter second set:").split(" "))
        print("intersection of set first and second",set1&set2)
    elif choice==7:
        set1 = set(input("Enter first set:").split(" "))
        set2 = set(input("Enter second set:").split(" "))
        print("Difference two set",set1-set2)
    elif choice==8:
        set1 = set(input("Enter first set:").split(" "))
        set2 = set(input("Enter second set:").split(" "))
        print("Symmetric difference:",set1^set2)
    elif choice==9:
        set1 = set(input("Enter first set:").split(" "))
        print("Set:",set1)
        check_data=input("Enter data:")
        print(set1.__contains__(check_data))
    elif choice==10:
        set1 = set(input("Enter first set:").split(" "))
        print("Set:",set1)
    elif choice==11:
        set1 = set(input("Enter first set:").split(" "))
        print("Set:", set1)
        set1.clear()
        print("Set:",set1)
    elif choice==12:
        break
    else:
        print("Invalid input please try again!")
