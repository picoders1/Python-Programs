# Enter student name and five subject marks calculate
students=dict()
n=int(input("Enter Number of student:"))
for i in range(1,n+1):
    list1=[]
    temp=dict()
    temp["Name"]=input("Enter Student name:")
    temp["Roll No"]=input("Enter Roll Number:")
    temp["Marks"]=list1
    for j in range(0,5):
        m=int(input("Enter marks:"))
        list1.append(m)
    temp["total"]=list1[0]+list1[1]+list1[2]+list1[3]+list1[4]
    avg=temp["total"]/5
    if avg>=91 and avg<=100:
        print("Your grade is S")
    elif avg>=81 and avg<91:
        print("Your grade is A")
    elif avg>=71 and avg<81:
        print("Your grade is B")
    elif avg>=61 and avg<71:
        print("Grade C")
    elif avg>=51 and avg<61:
        print("Your grade is D")
    else:
        print("Fail")
    students[i]=temp
    for key in students.keys():
        print(key,students[key])