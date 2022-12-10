'''Q40. Write a Python program to convert more than one list to nested dictionary. 

Original strings:
['S001', 'S002', 'S003', 'S004']
['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
[85, 98, 89, 92]
Nested dictionary:
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
'''

v=['S001', 'S002', 'S003', 'S004']
a=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
m=[85, 98, 89, 92]
d=d1={}

i=0
while i<len(v):
          d1[a[i]]=m[i]
          d[v[i]]=d1
          i=i+1
print(d)
          
result=[{x:{y:z}} for (x,y,z) in zip(v,a,m)]
print(result)