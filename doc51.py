'''Q51.Write a Python program to filter even numbers from a given dictionary values. 
Original Dictionary:
{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
Filter even numbers from said dictionary values:
{'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
Original Dictionary:
{'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
Filter even numbers from said dictionary values:
{'V': [], 'VI': [], 'VII': [2]}

'''
# dic={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
dic={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}

v={}
for i in dic:
    b=dic[i]
    a=[]
    j=0
    while j<len(b):
        if b[j]%2==0:
            a.append(b[j])
        j=j+1
    v[i]=a
print(v)


