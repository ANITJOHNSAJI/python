class Vehicle:
    def work():
        print("Move")
class Two(Vehicle):
    def rule1():
        print("wear helmet")
class Four(Vehicle):
    def rule2():
        print("wear seatbelt")
obj1=Two
obj2=Four
obj1.work()
obj2.work()
obj1.rule1()
obj2.rule2()