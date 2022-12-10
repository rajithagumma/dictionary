''' Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

'''
a="w3resource"
dict={}
b=[]
i=0
while i<len(a):
	c=a.count(a[i])
	if a[i] not in b:
		b.append(a[i])
		dict[a[i]]=c
	i=i+1
print(dict)