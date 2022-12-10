# dictionary creation
student=dict(name="rajitha",name2="rajitha2",name3="rajitha3")
print(student)

# accessing dictionary values

dict={"brand":"ford","model":"mustang","year":1964}
print(dict["year"])


# using get method it same result will come
dict={"brand":"ford","model":"mustang","year":1964}
x=dict.get("year")
print(x)


# using keys method
dict={"brand":"ford","model":"mustang","year":1964}
x=dict.keys()
print(x)

dict={"brand":"ford","model":"mustang","year":1964}
dict["color"]="red"
x=dict.keys()
print(x)


# get values method
dict={"brand":"ford","model":"mustang","year":1964}
x=dict.values()
print(x)


# get items method
dict={"brand":"ford","model":"mustang","year":1964}
x=dict.items()
print(x)

# check if key is exist or not
dict={"brand":"ford","model":"mustang","year":1964}
if "model" in dict:
          print("yes")
else:
          print("no")


# change values in dictionary
dict={"brand":"ford","model":"mustang","year":1964}
dict["year"]=2014
print(dict)


# update values in dictionary
dict={"brand":"ford","model":"mustang","year":1964}
dict.update({"year":2016,"rajitha":"radhika"})
print(dict)


# ading items to the dictionary
dict={"brand":"ford","model":"mustang","year":1964}
dict["color"]="black"
print(dict)


# removing items using pop method
dict={"brand":"ford","model":"mustang","year":1964}
dict.pop("model")
print(dict)


# using pop item method removes the last inserted item
dict={"brand":"ford","model":"mustang","year":1964}
dict.popitem()
print(dict)


# using del() keyword removes the items with specified keyname
dict={"brand":"ford","model":"mustang","year":1964}
del dict["model"]
print(dict)

# using del keyword can also delete the dictionary completely
dict={"brand":"ford","model":"mustang","year":1964}
del dict
print(dict)


# the clear method clear all items in the dictionary

dict={"brand":"ford","model":"mustang","year":1964}
dict.clear()
print(dict)


# loop through a dictionary
dict={"brand":"ford","model":"mustang","year":1964}
for x in dict:
          print(x)
for x in dict:
          print(dict[x])
for x in dict.keys():
          print(x)
for x in dict.values():
          print(x)

for x,y in dict.items():
          print(x,y)




