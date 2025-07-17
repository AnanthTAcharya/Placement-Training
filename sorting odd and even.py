a=[10,11,"zakir","balla",123,44,53,"anuj",20,46,7,"jack"]
even=[]
odd=[]
string=[]
for i in a:
    if(type(i)==str):
        string.append(i)
    elif (i%2==1):
       odd.append(i)

    elif (i%2==0):
        even.append(i)

    odd.sort()
    even.sort()
    string.sort()
print(odd+even+string)
