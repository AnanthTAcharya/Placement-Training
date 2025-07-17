
import  time

names=[]
marks=[]
for i in range(2):
    n=input("enter name:")
    names.append(n)
    student=[]
    for j in range(3):
        m=int(input("enter mark {}: ".format(j+1)))
        student.append(m)
    marks.append(student)
#print(names)
#print(marks)

per=[]
for i in marks:
    res=sum(i)//3
    per.append(res)
time.sleep(3)
print("_________________________")
for i in range(2):
    print("{}.{}:{}%".format(i+1,names[i],per[i]))
