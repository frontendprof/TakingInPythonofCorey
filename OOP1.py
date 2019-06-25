# B_R_R
# M_S_A_W


class Employee:
    def __init__(self, fname, lname, pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.email=fname+"."+lname+'@company.com'

    def fulname(self):
        return '{} {}'.format(self.fname, self.lname)

emp_1=Employee("Corey", "Schafer", 50000)
emp_2=Employee("AbdlMalik", "Sharif", 60000)



print(emp_1.email)
print(emp_2.pay)

print(Employee.fulname(emp_1))
print(emp_2.fulname())
