class Vehicle:
    def twowheeler():
        print("wear helmet")
    

class Road(Vehicle):
    def twowheeler():
        print("2 person only")
obj1=Vehicle
obj2=Road
obj1.twowheeler()
obj2.twowheeler()
        