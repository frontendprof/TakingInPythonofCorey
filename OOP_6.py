# B_R_R
# M_S_A_W


"""
We used special attributes:
@property
@getter
@setter
@deleter

"""

class Employee:

    def __init__(self, fname, lname, pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay


    @property
    def email(self):
        return '{}{}@email.com'.format(self.fname, self.lname)
    @property
    def fulname(self):
        return '{} {}'.format(self.fname, self.lname)

    @fulname.setter
    def fulname(self,name):
        fname, lname=name.split(" ")
        self.fname=fname
        self.lname=lname

    @fulname.deleter
    def fulname(self):
        print("Deleting Name ...")
        self.fname = None
        self.lname = None


emp_2=Employee("AbdlMalik", "Sharif", 60000)

emp_2.fulname="Joxa Yakhya"

print(emp_2.fname)
print(emp_2.email)
print(emp_2.fulname)

del emp_2.fulname
