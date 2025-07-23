class emp:
    profit=1000000
    tax=10
    company="cognizant"

    def __init__(self,name,age,sal,per):
        self.name=name
        self.age=age
        self.sal=sal
        self.per=per

    def taxa(self):
        return ((emp.tax/100)*self.sal)
    def profits(self):
        return ((self.per/100)*emp.profit)
    def display(self):
        print("1.",self.name)
        print("2.",emp.company)
        print("3.",self.sal)
        print("4.",self.taxa())
        print("5.",self.profits())
        print("6.",self.age)

a1=emp("ananth",21,100001,23)
a1.display()
