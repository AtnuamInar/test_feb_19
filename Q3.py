class Employee():
    def __init__(self, fname, lname, salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.email=self.fname+'.'+self.lname+'@deerwalk.edu.np'

    def printstring(self):
        print(self.fname)
        print(self.lname)
        print(self.salary)
        print(self.email)


std=Employee("maunta","gautam",20000)
std.printstring()
