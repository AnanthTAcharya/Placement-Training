def circle():
    r=int(input("enter the radius"))
    print("Area of circle is :",3.14*r*r)
def square(a):
    print("Area of squuare is:",a*a)

def Triangle():
    l=int(input("enter the length:"))
    b=int(input("enter the base: "))
    return 0.5*l*b

def Rectangle(l,b):
    return l*b

while(True):
    print("1.Circle")
    print("2.Square")
    print("3.Triangle")
    print("4.Rectangle")
    print("5.Exit")

    ch =int(input("Enter ur choice: "))
    match ch:
        case 1:
            circle()
        case 2:
            a=int(input("Enter side of square"))
            square=(a)
        case 3:
            res=Triangle()
            print("Area of triangle is",res)
        case 4:
            a=int(input("Enter length"))
            b=int(input("enter breadth"))
            res=Rectangle(a,b)
            print("Area of rectangle")
        case 5:
            exit(0)
        case _:
            print("invalid choice, please enter the below valid choice")


