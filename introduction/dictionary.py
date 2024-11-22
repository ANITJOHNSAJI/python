# thisdict={"name":"anit","age":21}
# print(thisdict)

# car={
    # "brand":"ford","model":"mustang"
# }
# print(car["brand"])

# car={
    # "brand":"ford","model":"mustang","brand":"susuki"
# }
# print(car)
# print(len(car))


# car={
    # "brand":"ford","model":"mustang","brand":"susuki","elec":False
# }
# print(car)
# print(type(car))

# h1=dict(name="anit",age=21)
# print(h1)


# car={
    # "brand":"ford","model":"mustang","brand":"susuki","elec":False
# }
# x=car["model"]
# print(x)



# car={
#     "brand":"ford","model":"mustang","brand":"susuki","elec":False
# }
# x=car.get("brand")
# print(x)


# car={
#     "brand":"ford","model":"mustang","brand":"susuki","elec":False
# }
# x=car.keys()
# print(x)

# car={
#     "brand":"ford","model":"mustang","brand":"susuki","elec":False
# }
# x=car.values()
# print(x)


# car={
#     "brand":"ford","model":"mustang","brand":"susuki","elec":False
# }
# x=car.items()
# print(x)


# car={
#     "brand":"ford","model":"mustang","brand":"susuki","elec":False
# }

# if "value" in car:
#     print("present")
# else:
#     print("not present" )

#value change cheyyan
# car={
#     "brand":"ford","model":"mustang","elec":False
# }
# car["model"]="ecosport"
# print(car)

#update cheyyan
# car={
#     "brand":"ford","model":"mustang","elec":False
# }
# car.update({"model":"hybrid"})
# print(car)

# car={
#     "brand":"ford","model":"mustang","elec":False
# }
# car.update({"color":"black"})
# print(car)
#or
# car["color"]="black"

# car={
#     "brand":"ford","model":"mustang","elec":False
# }

#Remove cheyyan
# 1.pop()
# 2.popitem()
# 3.del
# 4.clear()


# car={

# "brand":"ford","model":"mustang","elec":False
# }
# car.pop("elec")
# print(car)

# car={   "brand":"ford","model":"mustang","elec":False  }
# car.popitem()
# print(car)

#del

# car={   "brand":"ford","model":"mustang","elec":False  }
# del car["elec"]
# print(car)

# car={   "brand":"ford","model":"mustang","elec":False  }
# del car
# print(car)

#clear
# car={   "brand":"ford","model":"mustang","elec":False  }
# car.clear()
# print(car)

#copy
# car={   "brand":"ford","model":"mustang","elec":False  }
# newcar=car.copy()
# print(newcar)

#dict
# car={   "brand":"ford","model":"mustang","elec":False  }
# car2=dict(car)
# print(car2)

# #nested dictionary
# myfamily={"child1":{
#     "name":"Yamal"
    
# },
#     "child2":{
#         "name":"Anu"
        
#     }
#     }
# # print(myfamily)
# print(myfamily["child2"]["name"])

