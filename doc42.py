'''Write a Python program to check all values are same in a dictionary. Go to the editor
Original Dictionary:
{'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
Check all are 12 in the dictionary.
True
Check all are 10 in the dictionary.
False
'''
dic={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
user=int(input("enter the value:"))
result=True
for i in dic:
    if dic[i]!=user:
        result=False
        break
print(result)
          