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

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount


    @classmethod
    def from_string(cls, emp_str):
        fname,lname,pay=emp_str.split("-")
        return cls(fname,lname,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return "NO Work Today HUrray"
        return "Go to Work"




"""emp_1=Employee("Corey", "Schafer", 50000)
emp_2=Employee("AbdlMalik", "Sharif", 60000)
emp_3=Employee("Joxa", "Yakhya", 35000)
emp_4=Employee("Farrukh", "Said", 55000)

emp_str_1="John-Doe-70000"
emp_str_2="Steve-Smith-45000"
emp_str_3="Jane-White-53000"

new_emp_1=Employee.from_string(emp_str_1)

print(new_emp_1.fulname())
"""

import datetime
my_date=datetime.date(2016,5,28)
print(Employee.is_workday(my_date))
