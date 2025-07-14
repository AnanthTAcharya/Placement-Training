a=int(input("enter a number"))
b=int(input("enter a number"))

#if a%b==0 or b%a==0:
 #   print(max(a,b))
#else:
 #   print(a*b)

big=max(a,b)
step=big
while True:
    if(big%a==0 and big%b==0):
        print("lcm is:",big)
        break
    else:
        big +=step
