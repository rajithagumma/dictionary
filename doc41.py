'''Q41.Write a Python program to filter the height and width of students, which are stored in a dictionary. 
Original Dictionary:
{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
Height > 6ft and Weight> 70kg:
{'Cierra Vega': (6.2, 70)}
'''

dic={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
v={}
for i in dic:
    a=dic[i]
    if a[0]>=6 and a[1]>=70:
        v[i]=dic[i]
print(v)

