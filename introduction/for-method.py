# for i in range(1,6):
#     print("*"*i)

# for i in range(5,0,-1):
#     print("*"*i)


# k=0
# for i in range(5):
#     for j in range(i+1):
#         k=k+1
#         print(k,end="")
#     print()


a=6
for i in range(6):
    a=a-1
    print(end=" "*a)
    for j in range(i+1):
         print(j+1,end=" ")
    print("")