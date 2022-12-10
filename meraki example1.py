'''Write a program such that the below given dictionaries are into a single dictionary 
lland add the values having same key.'''

dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dicn={}
a=list(dic1.keys())
b=list(dic2.keys())
c=list(dic3.keys())
d=a+b+c
g=[]
for i in d:
    if i not in g:
        g.append(i)
    if (i in dic1 ) and (i in dic2):
        dicn[i]=dic1[i]+dic2[i]
    elif (i in dic1) and (i in dic3):
        dicn[i]=dic1[i]+dic3[i]
    else:
        if i in dic1:
            dicn[i]=dic1[i]
        elif i in dic2:
            dicn[i]=dic2[i]
        elif i in dic3:
            dicn[i]=dic3[i]
print(dicn)


# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dicn={}
# i=0
# while i<len(dic1):
#           if keys in dic2:
#                     dicn[keys]=dic1[keys]+dic2[keys]
#           elif keys in dic3:
#                     dicn[keys]=dic1[keys]+dic3[keys]
#           else:
#                     dicn[keys]=dic1[keys]
                    

# print(dicn)



dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
x={}
for i in dic1:
    for j in dic2:
        for k in dic3:
            x[i]=dic1[i]+dic2[j]+dic3[k]
        x[j]=dic2[j]
        x[k]=dic3[k]
print(x)