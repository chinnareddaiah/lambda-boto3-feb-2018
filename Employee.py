class Employee:
    emp_id = None
    name = None
    # Constructor of Employee,This is invoked implicitly when object is created
    def __init__(self,emp_id,name):
        self.emp_id = emp_id
        self.name = name


    def get_details(self):
        print('Name is {}'.format(self.name))
        print('Id is {}'.format(self.emp_id))


emp1 = Employee('123','Hari')

emp2 = Employee('456','Raghu')

emp1.get_details()
emp2.get_details()