# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

a=[]
b=[]
n=[]
c=int(input("enter a list range:"))
for i in range(c):
    b=int(input())
    a.append(b)
# print(a)
d=int(input("enter your target:"))
e=len(a)
for i in range(e):
    for j in range(e):
        t=a[i]+a[j]
        if t==d:
            if i in n and j in n:
                pass
            else:
                print(i,j)
                n.append(i)
                n.append(j)
     
     
      
