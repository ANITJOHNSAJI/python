class Vehicle:
    def work():
        print("Move")
class Car(Vehicle):
    def wheels():
        print("four wheeler")
class Alto(Car):
    def mileage():
        print("18")
obj1=Alto
obj1.work()
obj1.mileage()
