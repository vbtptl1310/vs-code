#declaration
#class employee:
 #   id=345
  #  name='vibhuti'

#object of class
#e=employee()    
#print(e.id)
#print(e.name)

class employee:
    id=None   #static/class attribute
    name=None
    def getdata(self):
        self.id=int(input('enter id:'))
        self.name=input('enter name:')
    def showdata(self):
        print(f'ID:{self.id}')   
        print(f'Name:{self.name}')

#object of class
e=employee()    
e.getdata()
e.showdata()