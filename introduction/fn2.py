a=[1,2,3,4,5,6,7,8,9,10]
b=[]
c=[]
def even(a):
    for i in  a:
        if i%2==0:
            b.append(i)
    return b
def odd(a):
    for i in a:
        if i%2!=0:
            c.append(i)
    return c
print(odd(a))
print(even(a))
   
    