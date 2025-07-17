a=input("Enter the string")
c=1
res=""
for i in range(len(a)):
    #c=1
    if(i+1<len(a) and a[i]==a[i+1]):
        c=c+1
    else:
        res=res+a[i]+str(c)
        c=1
print(res)
