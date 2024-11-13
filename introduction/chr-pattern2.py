#1
# a=65
# for i in range(4):
#     a=a-1
#     print(end=""*a)
#     for j in range(i+1):
#         print(j+1,end="")
#     print()
# 2
# a=65
# for i in range(4):
#     for j in range(i+1):
#         print(chr(a),end=" ")
#         a=a+1
       
#     print()

#3
# a=65
# for i in range(3):
#     for j in range(i+1):
#         print(chr(a-j),end=" ")
#     print()
#     a=a+1

#4
# a=1
# for i in range(3):
#     for j in range(i+1):
#         print(a-j,end=" ")
#     print()
#     a=a+1

#5
a=65
b=1
for i in range(3):
    for j in range(3):
        print(chr(a+j),end=" ")
        print(b+j,end=" ")
    print()
