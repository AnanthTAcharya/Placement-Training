b=int(input("Enter the number of blocks"))
l=int(input("enter the number of lines"))
s=int(input("enter the number of stars"))
sum=0
print(f"---------------------")
for i in range(b):
    print(f"___________block{i+1}__________")
    count=0
    for j in range(l-i):
        for k in range(s):
            print("*",end=" ")
            count=count+1
        print()
    print(count)
    sum +=count
print(f"total:{sum}")
