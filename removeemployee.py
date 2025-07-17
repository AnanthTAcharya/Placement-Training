names=["a","b","c","d","e","f","g","h","i","j"]
memo=[0,1,1,1,2,2,1,2,1,2]
salary=[1000,2000,3000,4500,2000,5000,1500,2300,1300,1100]
res=list(zip(names,memo,salary))
#q=sorted(res,key=lambda x:x[0] x[1] x[2])
print(res)
removed=[]
for i in res:

    if i[2]>4000:
        removed.append(i)
print(removed)
remaining=[i for i in res if i[2]<4000]
print(remaining)
a=sorted(remaining,key=lambda x:x[2],reverse=True)
print(a)
removed2=[]
for i in a:
    if(i[1]>=2):
        removed2.append(i)
    if(len(removed2)>3):
        break
final =removed+removed2
index=1
for i in final:
    print("{}.{}: Memo {} :salary{} ".format(index,i[0],i[1],i[2]))
    index=index+1
