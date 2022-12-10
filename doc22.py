'''Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd
'''

dic={'1':['a','b'], '2':['c','d']}
r=list(dic.values())
v=r[0]
a=r[-1]
i=0
while i<len(v):
    j=0
    while j<len(v):
        print(v[i]+a[j])
        j=j+1
    i=i+1



# a=["Hello","Take"]
# b=["Dear","sir"]
# i=0
# d=[]
# while i<len(a):
#           j=0
#           while j<len(a):
#                     c=a[i]+b[j]
#                     d.append(c)
#                     j=j+1
#           i=i+1
# print(d)
