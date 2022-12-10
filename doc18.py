'''Write a Python program to get the maximum and minimum value in a dictionary.
'''

dic1={"rajitha":19,"tamanna":18,"gangothri":20,"lakshmi":21}
a=list(dic1.values())
a.sort()
print("maximum value is",a[-1])
print("minimum value is",a[0])