# dict={}
# for x in range(1,16):
#           dict[x]=x**2
# print(dict)


# a = 2
# b = 330
# print("A") if a > b else print("B")

# a=(((45+90/3*6)*2)/1/2)+5
# print(a)
dic={"a":20,"b":45,"c":67,"d":98,"e":23,"f":4}
a=list(dic.values())
a.sort(reverse=True)
a=a[0:3]
print(a)