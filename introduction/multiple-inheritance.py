class Two:
    def seat():
        print(2)
class Four:
    def person():
        print(5)
class Three(Two,Four):
    def member():
        print(3)
obj1=Three
obj1.seat()
obj1.person()
obj1.member()