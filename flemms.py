boy=input("enter the name of boy: ")
girl =input ("enter the name of girl: ")

b=list(boy)
g=list(girl)

for i in range(len(b)):
    for j in range(len(g)):
        if(b[i]==g[j]):
            b[i]='2'
            g[j]='2'

#print(b)
#print(g)

for i in b:
    if(i=="2"):
        b.remove(i)
for i in g:
    if(i=="2"):
        g.remove(i)

num=len(b)+len(g)
print(num)

ans=['f','l','a','m','e','s']
index=0
while(len(ans)!=1):
    index=(index+(num-1))%len(ans)
    ans.pop(index)
print("The relation is",ans[0])

