class Employee:
    id=None
    name=None

    def GetEmp(self):
       self.id=1
       self.name='xyz'

    def ShowEmp(self): 
        print(f'ID:{self.id}')
        print(f'name:{self.name}')  

class payroll(Employee):
    salary=None    

    def Getdata(self):
        self.GetEmp()
        self.salary=25000

    def Showdata(self):
        self.ShowEmp()
        print(f'salary:{self.salary}')

p=payroll()
p.Getdata()
p.Showdata()            
