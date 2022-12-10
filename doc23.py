'''Write a Python program to find the highest 3 values of corresponding keys in a dictionary'''
dic={"a":20,"b":45,"c":67,"d":98,"e":23,"f":4}
a=list(dic.values())
a.sort(reverse=True)
a=a[0:3]
print(a)