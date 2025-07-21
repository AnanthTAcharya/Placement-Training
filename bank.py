def deposit(ch):
        amt1=int(input("Enter the ammount to be deposited: "))
        acct[ch]+=amt1
        print("The RS {} is successfully deposied toyou account {}" .format(amt1,ch))
        print("The current balance is ",acct[ch])

def withdraw(ch):
    amt2 =int(input("Enter the amount to be withdrawn : "))
    if (amt2>acct[ch]):
        print("insuffienct amt  ")
    else:
        acct[ch]-=amt2
        print("The RS{} is successfully withdrawn from your account {}" .format(amt2,ch))
        print("The current balance is ",acct[ch])

def transfer(ch):
    amt3 =int(input("Enter the ammount to be transferred: "))
    to_acc=int(input("Enter the to account number:"))
    if(to_acc not in acct):
        print("The entered account doesn't exist")
    elif (amt3>acct[ch]):
         print("insuffienct amt  ")
    else:
        to_acc[ch]+= amt3
        print()





acct={101:1000,102:2000,103:3000}

while True:
    ch =int(input("enter the account number: "))
    if (ch not in acct):
        print("your account doesn't exist ")
    else:
        print("your account is: ",ch)

        print("1.Deposit")
        print("2.Withdraw")
        print("3.Transfer")
        print("4.check Balance")
        print("5.Loggout")
        c=int(input ("enter your choice: "))

        match c:
            case 1:
                #amt1=int(input("Enter the ammount to be deposited: "))
                deposit(ch)

            case 2:
                #amt2 =int(input("Enter the amount to be withdrawn : "))
                withdraw(ch)

            case 3:
                #amt3 =int(input("Enter the ammount to be transferred: "))
                transfer(ch)

            case 4:
                print("The available balance of {} is :{} ".format(ch,acct[ch]))

            case 5:
                exit(0)
            case _:
                print("invalid choice, please enter the below valid choice")
