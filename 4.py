a=1
sum=0
while(a!=0):
    a=int(input("enter a number"))
    if a>100:
        continue
    elif a == 0:
        break
    else:
        sum+=a
print(sum)
