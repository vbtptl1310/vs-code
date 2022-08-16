class A:
    def a(self):
        print('calling from A')

class B:
    def b(self):
        print('calling from B')

class C(A,B):
    def c(self):
        self.a()
        self.b()
        print('calling from C')

obj=C()
obj.c()