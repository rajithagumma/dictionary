'''Q53.
Write a Python program to convert a given list of lists to a dictionary. 
Original list of lists:
[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
Convert the said list of lists to a dictionary:
{1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}

'''
a=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'],
 [5, 'Zachary Simon', 'VII']]
i=0
d={}
while i<len(a):
          b=a[i]
          d[a[i][0]]=a[i][1:3]
          i=i+1
print(d)
