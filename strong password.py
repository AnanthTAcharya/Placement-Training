s=input("enter the password")
sp=0
dg=0
up=0
lp=0
if(len(s)>7):
    for i in s:
        if(i.isupper()):
            up=up+1
        elif(i.islower()):
            lp=lp+1
        elif(i.isdigit()):
            dg=dg+1
        else:
            sp=sp+1
    if(up>0 and lp>0 and dg>0 and sp>0):
        print("good Password")
    else:
        print("bad password")
else:
    print("bad pasword due to less character")
