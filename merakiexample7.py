test_list=[{"first":"1"}, {"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
res = list(set(val for dic in test_list for val in dic.values()))
print("The unique values in list are : " + str(res))


# own method
dict=[{"first":"1"}, {"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
l1=[]
for i in dict:
          for j in i.values():
                    if j not in l1:
                              l1.append(j)
print(l1)

    
