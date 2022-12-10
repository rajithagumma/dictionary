# dt={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}

# sorted_dt = {key: value for key, value in sorted(dt.items(), key=lambda item: item[1])}
# print(sorted_dt)
# sorted_dt = {key: value for key, value in reversed(sorted(dt.items(), key=lambda item: item[1]))}
# print(sorted_dt)

# a = {(1,2):1,(2,3):2}
# print(a[1,2])



# l1=[1,2,3,4,5,6]
# l2=l1[0:-1]
# print(l2)


a=[[10,9,5],[5,7,600,77,],[6,4,2],[10,12,15,200]]
i=0
max=0
c=[]
while i<len(a):
    b=a[i]
    j=0
    max1=0
    while j<len(b):
        if b[j]>=max1:
            max1=b[j]
        j=j+1
    c.append(max1)
    i=i+1
k=0
while k<len(c):
    if c[k]>=max:
        max=c[k]
    k=k+1
print(c)
print(max)


def a(list):
    i=0
    b=[]
    max=0
    while i<len(list):
        j=0
        while j<len(list[i]):
            if list[i][j]>max:
                max=list[i][j]
                b.append(max)
            j+=1
        i+=1
        print(b)
a([[10,9,5],[5,7,600,77],[6,4,2],[10,12,15,200]])

                    
          