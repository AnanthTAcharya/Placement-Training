noto =["Darshan","Anuj","Rohit"]
names=["Anuj","Darshan","Rohit","Jack","Priya","Bala","Rai","Ram","Raj","Ben"]
score=[2,5,6,8,3,5,6,9,8,2]

for i  in range(len(names)):
    if score[i]>5:
        if names[i] not in noto:
            print(names[i])
