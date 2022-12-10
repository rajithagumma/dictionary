'''Q43.Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists. 
Original list:
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
Grouping a sequence of key-value pairs into a dictionary of lists:
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
'''
a=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
i=0
d={}
while i<len(a):
    b=a[i][0]
    print(b)
    j=i+1
    c=[]
    while j<len(a):
        if b==a[j][0]:
            # v=a[i][1],a[j][1]
            c.append(a[i][1])
            c.append(a[j][1])
        else:
            c.append(a[i][1])
        j=j+1
    d[a[i][0]]=c
    i=i+1
print(d)