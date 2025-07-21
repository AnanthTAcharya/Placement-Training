def facto(n):
    if n==1:
        return
    i=2
    while(n%i!=0):
        i=i+1


    #for i in range(2,n+1):

        #if(n%i==0):
    print(i,end=" ")#if we use the for loop then the print and recursive call will be inside the loop
    facto(n//i)
         #break
n =int(input("enter the number"))
facto(n)
