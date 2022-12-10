city_population = {"NewYorkCity":8550405,"LosAngeles":3971883, "Toronto":2731571, "Chicago":2720546, "Houston":2296224}
print(city_population["NewYorkCity"])
print(city_population)
print(type(city_population))

Dict = {'ball' : 'green','Ball': 'red'}
print(Dict['ball'])
print(Dict['Ball'])
# print(Dict['bat'])

person={'name':'jack','age':20,'gender':'male',4:'organization'}
result = person['age'] 
x = person.get('gender')
print(person[4])
print(x)
print(result)

person= {'1': 'RAM', '2': 17,}
person[3] = 'male'
print(person)


d1 = {"john":40, "peter":45}
d2 = {"john":466, "peter":45}
print(d1 != d2)

dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)