'''Q35. Write a Python program to count the number of items in a dictionary value that is a list.
dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
Sample output: 5
'''
dic= {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count=0
for i in dic:
    v=dic[i]
    for j in v:
        count+=1
print(count)


