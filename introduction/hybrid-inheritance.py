class A1:
    def a11():
        print("A1")
class B1(A1):
    def b11():
        print("B1")
class C1(B1):
    def c11():
        print("C1")
class D1(B1):
    def d11():
        print("D1")
class E1(D1):
    def e11():
        print("E1")
class F1(C1,D1):
    def f11():
        print("F1")
obj1=F1
obj2=E1
obj1.a11()
obj1.b11()
obj1.c11()
obj1.d11()
obj1.f11()
obj2.a11()
obj2.b11()
obj2.d11()
obj2.e11()        