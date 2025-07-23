from datetime import datetime
class Bus:
    def __init__(self,bno,ac,cap):
        self.bno=bno
        self.ac=ac
        self.cap=cap

    def get_bno(self):
        return self.bno


    def get_cap(self):
        return self.cap


    def get_ac(self):
        return self.ac


    def dispaly(self):
        print("1.Bus No:",self.get_bno())
        print("2.AC:",self.get_ac())
        print("3.Bus capacity: ",self.get_cap())

class Booking:
    def __init__(self):
        name=(input("enter the name: "))
        bno=(int(input("enter the bno:")))
        d=int(input("enter the date(dd-mm-yyyy)"))
        date=datetime.strptime(d,"%dd-%mm-%yyyy").date()
        self.name=name
        self.bno=bno
        self.date=date

    def make_booking(self,BUSES,BOOKINGS):
         if(self.is_available(BUSES,BOOKINGS,self.bno,self.date)):
             BOOKINGS.append(self)
         else:
             print("bus is full")

    def is_available(self,BUSES,BOOKINGS,bno,date):
        booked=0
        capacity=0

        for i in BUSES:
            if(i.bno==bno):
                capacity=i.capacity




BUSES=[]
print("The available buses are")
for i in BUSES:
    i.display()
    print("____________________")

BOOKINGS=[]
while(True):
    print("1. enter the booking")
    print("2.view the availability")
    print("3.exit")
    ch=int(input("Enter the choice: "))
    if(ch==1):
        b=Booking()
        b.make_booking(BUSES,BOOKINGS)

    elif(ch==2):
        if(not BOOKINGS):
            print()
        else:
            for i in BOOKINGS:
                i.display_book_info()
    elif(ch==3):
        print("Exiting the system .. Thank You")
        break
    else:
        print("The ivalid choice")

