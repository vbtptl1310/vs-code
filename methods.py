class Abc:
    @staticmethod
    def a():
        print('static method')
        
    def b(self):
        print('instancce method')
        
    def c(abc):
        print('class method')
        
j=Abc()
j.a()
j.b()
j.c()