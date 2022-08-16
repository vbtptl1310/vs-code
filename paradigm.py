Class A:
    num=None
    __age=None #private
    name=None

    def __init__(self,num,__age,name):#parametarized
        self.num=num
        self.__age=age             ##private
        self.name=name

    def displayage(self):
        print("name:",self.name) 
        
c= A(19,23,'xyz') 
print(c.name)    
print(c.num)   
print(c.__age)    

