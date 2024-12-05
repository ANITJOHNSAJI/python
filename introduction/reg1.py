import re
p=input("Enter a password:")
a=len(p)
# x=re.search('\s\d',p)
if re.findall("[a-zA-Z ]",p)==True:
    if re.findall("\d",p)==True:
        if a>8:
            print("password entered successfully")
else:
    print("Weak Password")
    
