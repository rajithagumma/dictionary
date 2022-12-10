'''Write a program to print 'exists' if entered key already exists in the dictionary and print 'not exists'
 if the entered key does not exist.'''

dict1={"name":"Raju","marks":56}
a=input ("enter the key:")
if a in dict1:
          print("exists")
          print(dict1[a])

else:
          print("not exists")


# dict1={"name":"Raju","marks":56}
# a=input ("enter the value=")
# if (a=="name"):
#   print (dict1["name"])
# elif(a=="marks"):
#   print(dict1["marks"])
# else:
#   print ("invalid input")