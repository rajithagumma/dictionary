'''Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

'''
a={'a':100,'b':200,'c':300}
b={'a':300,'b':200,'d':400}
i=0
x=list(a)
y=list(b)
z={}
while i<len(a):
    if x[i] in y[i]:
        z[x[i]]=a[x[i]]+b[y[i]]
    else:
        z[x[i]]=x[i]=a[x[i]]
        z[y[i]]=y[i]=b[y[i]]
    i=i+1
print(z)