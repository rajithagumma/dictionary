'''Q31.. Write a Python program to get the top three items in a shop. Go to the editor
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
Expected Output:
item4 55
item1 45.5
item3 41.3

'''

data={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
x=list(data.values())
dic={}
x.sort(reverse=True)
x=x[:3]
for i in x:
          for j in data.keys():
                    if data[j]==i:
                              print(str(j)+":"+str(data[j]))
                              