while True:
    print("1-->Add two tuple")
    print("2-->Multiply tuple")
    print("3-->Find length")
    print("4-->Find maximum data max")
    print("5-->Find minimum data min")
    print("6-->limited data print")
    print("7-->Reverse Order print")
    print("8-->Compare two list")
    print("9-->check data is there or not")
    print("10->count")
    print("11->Exit")

    choice = int(input("Enter choice:"))
    if choice == 1:
        t1 = tuple(input("Enter first tuple:").split(" "))
        t2 = tuple(input("Enter second tuple:").split(" "))
        print("Add two tuple:", t1 + t2)
    elif choice == 2:
        t1 = tuple(input("Enter tuple:").split(" "))
        print("Multiply tuple:", t1 * 2)
    elif choice == 3:
        t1 = tuple(input("Enter tuple:").split(" "))
        print("Length:", len(t1))
    elif choice == 4:
        t1 = tuple(input("Enter tuple:").split(" "))
        print("Max:", max(t1))
    elif choice == 5:
        t1 = tuple(input("Enter tuple:;").split(" "))
        print("Min:", min(t1))
    elif choice == 6:
        t1 = tuple(input("Enter tuple:").split(" "))
        starting_index = int(input("Enter starting index:"))
        ending_index = int(input("Enter ending index:"))
        print("limited data:", t1[starting_index:ending_index])
    elif choice == 7:
        t1 = tuple(input("Enter tuple:").split(" "))
        print("Reverse order:", t1[::-1])
    elif choice == 8:
        t1 = tuple(input("Enter first tuple:").split(" "))
        t2 = tuple(input("Enter second tuple:").split(" "))
        print("Compare two tuple:", t1 == t2)
    elif choice == 9:
        t1 = tuple(input("Enter tuple:").split(" "))
        n = input("Enter data:")
        print("Check Data:", n in t1)
    elif choice == 10:
        t1 = tuple(input("Enter tuple:").split(" "))
        n = input("Enter data:")
        print("Total number of data:", t1.count(n))
    elif choice == 11:
        break
    else:
        print("Invalid input please try again!")