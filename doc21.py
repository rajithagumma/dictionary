d1=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
l1=[]
for i in d1:
     for j in i.values():
          if j not in l1:
                    l1.append(j)
print(l1)