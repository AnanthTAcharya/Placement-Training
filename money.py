amt=int(input("enter the amt"))
coins=[500,200,100,50,20,]
for i in coins:
    while amt>=i:
        amt=amt-i
        print(i)
