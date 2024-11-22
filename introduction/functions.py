def addition():
    print("enter 2 numbers")
    a=int(input())
    b=int(input())
    print(a+b)

def subtraction():
    print("enter 2 numbers")
    a=int(input())
    b=int(input())
    print(a-b)

def multiplication():
    print("enter 2 numbers")
    a=int(input())
    b=int(input())
    print(a*b)

def division():
    print("enter 2 numbers")
    a=int(input())
    b=int(input())
    print(a/b)

print('''
        select
        1.Addition
        2.Subtraction
        3.Multiplication
        4.Division
        5.Exit
        ''')
c=int(input("Enter your choice:"))
if c==1:
        addition()
elif c==2:
        subtraction()
elif c==3:
        multiplication()
elif c==4:
        division()
elif c==5:
        exit()
else:
      print("Invalid Choice")
