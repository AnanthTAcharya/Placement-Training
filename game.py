import random
name=input("enter the name: ")
name2=input("enter the name: ")
print("comp has fixed first 5 nums in range of 1 to 10")
print("you guys have to guess it ... Ready?")

nums=[]
while(len(nums)!=5):
    d=random.randint(1,10)
    if (d not in nums):


for i in range(3):
    print("_____ROUND{}_____________".format(i+1))
    print("Dear {} guess ur choice ".format(name+1))
    ch=input(input())
    player1.append(ch)
    if(ch in nums):
        print("_>>Correct")
        s1=s1+1
    else:
        print("_____>>Wrong")
        s2=s2+1
        print()

