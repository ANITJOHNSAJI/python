a=int(input("enter a number:"))
b=0
d=a
while a>0:
    c=a%10
    b=b*10+c
    a=a//10
if d==b:
    print("palindrome")

else:
    print("Not palindrome")
    