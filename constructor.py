#class person:
#    def __init__(self):
 #       print('calling constructor')

#p=person()        



#class person:
 #   def __init__(self,m):
  #      print('parameterised constructor')

#p=person(52)  

#class person:
 #   name=None
  #  def __init__(self,m):#parametarized
   #     self.name=m

#p=person('abd')
#print(p.name)


class person:
    name=None

    #costructor
    def __init__(self,m):#parametarized
        self.name=m

    #destructor
    def __del__(self):
        print('calling destructor')    

p=person('abd')
print(p.name)
p2=person('xyz')
print(p2.name)  