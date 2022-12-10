while True:
    print("1-->Change Upper case")
    print("2-->Change Lower Case")
    print("3-->Reverse String")
    print("4-->Print specific index charater on given string")
    print("5-->Join Underscore ")
    print("6-->Check Length given String")
    print("7-->Concat two String")
    print("8-->IsDigit Method")
    print("9-->Find String or charater of index on given String")
    print("10->Check Minimum charater on given String")
    print("11->Check Maximum Charater on give String")
    print("12->Shorting String")
    print('13->Match two String')
    print('14->Replace charater')
    print("0-->Exit")

    choice = int(input("Enter Choice:"))
    if choice == 1:
        print("Enter String:")
        print(input().upper())
    elif choice == 2:
        print("Enter String:")
        print(input().lower())
    elif choice == 3:
        print("Enter String:")
        print(input()[::-1])
    elif choice == 4:
        print("Enter String:")
        str1 = input()
        startIndex = int(input("Enter Starting index:"))
        endingIndex = int(input("Enter Ending index:"))
        print(str1[startIndex:endingIndex])
    elif choice == 5:
        print("_".join(input("Enter String:")))
    elif choice == 6:
        print(len(input("Enter String:")))
    elif choice == 7:
        str1 = input("Enter First String:")
        str2 = input("Enter Second String:")
        print(str1 + " " + str2)
    elif choice == 8:
        print(input("Enter String:").isdigit())
    elif choice == 9:
        str1 = input("Enter String:")
        find = input("Enter Findind String:")
        print(str1.find(find))
    elif choice == 10:
        print(min(input("Enter String:")))
    elif choice == 11:
        print(max(input("Enter String:")))
    elif choice == 12:
        print(sorted(input("Enter string:")))
    elif choice == 13:
        str1 = input("Enter First String:")
        str2 = input("Enter Second String:")
        print(str1 == str2)
    elif choice == 14:
        str1 = input("Enter String:")
        oldChar = input("Enter old charater:")
        newChar = input("Enter new charater:")
        print(str1.replace(oldChar, newChar))
    elif choice == 0:
        break
    else:
        print("Invalid input please try again!")
