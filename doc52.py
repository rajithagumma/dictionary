'''Q52. Write a Python program to find the specified number of maximum values in a given dictionary.
Original Dictionary:
{'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
1 maximum value(s) in the said dictionary:
['f']
2 maximum value(s) in the said dictionary:
['f', 'i']
5 maximum value(s) in the said dictionary:
['f', 'i', 'g', 'd', 'c']

'''
dic={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
a=list(dic.values())
a.sort(reverse=True)
d=[]
user=int(input("enter how many max numbers:"))
i=0
while i<user:
    for j in dic:
        if dic[j]==a[i]:
            if j not in d:
                d.append(j)
    i=i+1
print(d)

