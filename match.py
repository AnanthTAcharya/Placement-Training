import  random
n=int(input("enter num of teams"))

teams=[]
for i in range(n):
    a=input("Enter team name{}: ".format(i+1))
    teams.append(a)
meet=int(input("enter the number of meets:"))

matches=[]
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(meet):
            matches.append([teams[i],teams[j]])
random.shuffle(matches)
print("____________________-")
index=1
for i in matches:
    print("matches {}.{} v/s{}".format(index,i[0],i[1]))
    index=index+1

