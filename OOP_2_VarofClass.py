# B_R_R
# M_S_A_W


class Employee:

    raise_amount=1.04
    num_of_emp=0

    def __init__(self, fname, lname, pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.email=fname+"."+lname+'@company.com'
        Employee.num_of_emp+=1

    def fulname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)

emp_1=Employee("Corey", "Schafer", 50000)
emp_2=Employee("AbdlMalik", "Sharif", 60000)
emp_3=Employee("Joxa", "Yakhya", 35000)
emp_4=Employee("Farrukh", "Said", 55000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.num_of_emp)
