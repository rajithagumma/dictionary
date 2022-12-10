# a="mississipi"
# c=a.split()
# b=[]
# d={}
# i=0
# while i<len(c):
#           f=c[i]
#           j=0
#           while j<len(f):
#                     count=f.count(f[j])
#                     if c[i] not in b:
#                               b.append(f[i])
#                               d[f[i]]=count
#                     j=j+1
#           i=i+1
# print(d)

# a="mississippi"
# i=0
# d={}
# b=[]
# v=0
# while i<len(a):
#           count=a.count(a[i])
#           if a[i] not in b:
#                     b.append(a[i])
#                     d[v]=count
#                     v=v+1
#           i=i+1
# print(d)

user=input("enter the time:")
if user[-2:]=="AM" or user[-2:]=="am":
    if user[:2]=="12":
        print("00"+user[2:8])
    else:
        print(user[:8])
else:
    v=int(user[:2])
    if v<12:
        v=v+12
        print(str(v)+user[2:8])
