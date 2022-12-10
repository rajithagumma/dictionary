'''Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})

'''
a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
i=0
b={}
for i in a:
          if i["item"] not in b:
                    b[i["item"]]=i["amount"]
          else:
                    b[i["item"]]+=i["amount"]
print(b)