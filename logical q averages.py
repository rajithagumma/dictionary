dic={"rajitha":[70,80,90,78,90],"pavani":[56,78,98,54,67],"tamanna":[90,98,78,78,89]}
a=list(dic.values())
i=0
while i<len(a):
    j=0
    count=0
    sum=0
    while j<len(a):
        sum=sum+a[j][i]
        print(a[j][i])
        count+=1
        j=j+1
    avg=sum/count
    print("average is",avg)
    i=i+1

