'''Q38.. Write a Python program to drop empty Items from a given Dictionary. 
Original Dictionary:
{'c1': 'Red', 'c2': 'Green', 'c3': None}
New Dictionary after dropping empty items:
{'c1': 'Red', 'c2': 'Green'}

'''
dic={'c1': 'Red', 'c2': 'Green', 'c3': None}
d={}
for i in dic:
    if dic[i]!=None:
        d[i]=dic[i]
print(d)