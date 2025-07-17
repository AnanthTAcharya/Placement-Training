str1=input("enter string1")
str2 =input("enter string2")
a=str1.lower()
b=str2.lower()

x="".join(i for i in a if i!=" " )
y="".join(i for i in b if i!=" ")

a1=sorted(x)
a2=sorted(y)

if(a1==a2):
    print("It is Anargam")
else:
    print("It is not anargam")
