'''Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
for i in dic2:
          dic1[i]=dic2[i]
for j in dic3:
          dic1[j]=dic3[j]
print(dic1)




dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
newd={}
newd.update(dic1)
newd.update(dic2)
newd.update(dic3)
print(newd)

