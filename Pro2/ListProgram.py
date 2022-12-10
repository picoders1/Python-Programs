while True:
    print("Some List opertions:")
    print("1.Insert list data")
    print("2.Remove Element")
    print("3.concat two List")
    print("4.Extend list")
    print("5.Sorting of list")
    print("6.Reverse order print")
    print("7.Append list")
    print("8.Pop element")
    print("9.clear all element")
    print("10.copy data another list")
    print("11.count Element")
    print("12.Index find on given element")
    print("13.Display list")
    print("0.exit")

    choice = int(input("Enter Choice:"))
    if choice == 1:
        list1 = list(input("Enter list data:").split(" "))
        print("List:", list1)
        pos = int(input("Enter position:"))
        data = input("Enter data:")
        list1.insert(pos, data)
        print("List:", list1)
    elif choice == 2:
        list1 = list(input("Enter list data:").split(" "))
        print("List:", list1)
        data = input("Enter remove data:")
        list1.remove(data)
        print("List:", list1)
    elif choice == 3:
        list1 = list(input("Enter first list data:").split(" "))
        print("List:", list1)
        list2 = list(input("Enter second data:").split(" "))
        print("List:", list2)
        l4 = list1 + list2
        print("Concat of two list:")
        print(l4)
    elif choice == 4:
        list1 = list(input("Enter first list data:").split(" "))
        print("List:", list1)
        list2 = list(input("Enter second list data:").split(" "))
        print("List:", list2)
        list1.extend(list2)
        print("Extends List:", list1)
    elif choice == 5:
        list1 = list(input("Enter list data:").split(" "))
        print("List:", list1)
        list1.sort()
        print("Sorted Element:", list1)
    elif choice == 6:
        list1 = list(input("Enter list data:").split(" "))
        print("List:", list1)
        list1.reverse()
        print("Reverse order print data:", list1)
    elif choice == 7:
        list1 = list(input("Enter list data:").split(" "))
        print("List:", list1)
        print("Enter data:")
        l2 = input()
        list1.append(l2)
        print("List:", list1)
    elif choice == 8:
        list1 = list(input("Enter list data:").split(" "))
        print("List:", list1)
        pos = int(input("Enter position:"))
        pop_data = list1.pop(pos)
        print("Pop Data:", pop_data)
        print("List:", list1)
    elif choice == 9:
        list1 = list(input("Enter list data:").split(" "))
        print("List:", list1)
        list1.clear()
        print("List:", list1)
        print("Your list data is successfully clear")
    elif choice == 10:
        list1 = list(input("Enter list data:").split(" "))
        print("List_1:", list1)
        list2 = list1.copy()
        print("List_2:", list2)
    elif choice == 11:
        list1 = list(input("Enter list data:").split(" "))
        print("List_1:", list1)
        data = input("Enter Data:")
        print("Number of element:", list1.count(data))
    elif choice == 12:
        list1 = list(input("Enter list data:").split(" "))
        print("List_1:", list1)
        data = input("Enter index data:")
        print("Data position is:", list1.index(data))
    elif choice == 13:
        list1 = list(input("Enter list data:").split(" "))
        print("List:", list1)
    elif choice == 0:
        break
    else:
        print("Invalid input please try again!")