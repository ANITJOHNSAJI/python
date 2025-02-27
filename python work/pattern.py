# for i in range(5):
#     print(i*'*')


# for i in range(7):
#     print('*'*[4,2,5,3,1,3,4][i])


# for i in range(1, 101):
    
#     if i % 5 == 0 and i % 3 == 0:
#         print('fizzbuzz')
    

#     elif i % 3 == 0:
#         print('fizz')

#     elif i % 5 == 0:
#         print('buzz')

    
#     else:
#         print(i)


while True:
    a=[]
    print(
     'choices are'   
    '1.addtodo'
    '2.displaytodo'
    '3.edittodo'
    '4.exit')
    choice=int(input("enter your choice"))
    if choice==1:
        todo=input("enter your todo")
        a.append(todo)
    elif choice==2:
        print(a)
    elif choice==3:
        todo=input("enter your todo")
        a.remove(todo)
    else :
        break


