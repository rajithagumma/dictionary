'''Q30.Write a Python program to remove spaces from dictionary keys.
Original dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 
'''
dic={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
a={}
for i in dic:
    j=0
    v=""
    while j<len(i):
        if i[j]!=" ":
            v=v+i[j]
        j=j+1
    a[v]=dic[i] 
print(a)  