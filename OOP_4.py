# B_R_R
# M_S_A_W




"""
In this program, we worked on inheritance, relation of subclasses and 
@isinstance(ClassA, ClassB)
@issubclass(Classc, ClassD)
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


class Developer(Employee):
    raise_amount = 1.1
    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname,lname,pay)
        self.prog_lang=prog_lang



class Manager(Employee):

    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname,lname,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees


    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)


    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)



    def print_emps(self):
        for emp in self.employees:
            print("---->", emp.fulname())


dev_1=Developer("Corey", "Schafer", 50000, "Java")
dev_2=Developer("AbdlMalik", "Sharif", 60000, "Python")

mr_1=Manager("Sue", "Black", 90000, [dev_2])
print(mr_1.email)
mr_1.add_emp(dev_1)
mr_1.print_emps()


print(isinstance(Manager, Employee))
print(issubclass(Developer, Employee))
