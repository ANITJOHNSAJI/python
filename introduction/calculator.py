i="y"
while i=="y":
    
    a=int(input("enter a number:"))
    b=int(input("enter another number:"))
    print('''
        select
        1.Addition
        2.Substraction
        3.Multiplication
        4.Division
        5.Exit
        ''')
    c=int(input("Enter your choice:"))
    if c==1:
        print("answer:",a+b)
    elif c==2:
        print("answer:",a-b)
    elif c==3:
        print("answer:",a*b)
    elif c==4:
        print("answer:",a/b)
    elif c==5:
        exit()
    else:
        print("Invalid Choice")
    i=input("Do you want to continue y/n :")