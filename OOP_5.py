# B_R_R
# M_S_A_W


"""
In this program we learn about magic/dunder methods.
@__repr__
@__str__
@__add__
@__len__
"""



class Employee:

    raise_amount=1.04

    def __init__(self, fname, lname, pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.email=fname+"."+lname+'@company.com'


    def fulname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)


    def __repr__(self):
        return "Employee({}, {}, {})".format(self.fname, self.lname, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fulname(), self.email)

    def __add__(self,other):
        return self.pay+other.pay

emp_1=Employee("Corey", "Schafer", 50000)
emp_2=Employee("AbdlMalik", "Sharif", 60000)

print(emp_1)
print(repr(emp_2))
print(str(emp_2))


print(emp_1+emp_2)
