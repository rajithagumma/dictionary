'''.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample input ( n = 5) :
Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.
'''
n=int(input("enter the number:"))
i=1
dict={}
while i<=n:
	dict[i]=i*i
	i=i+1
print(dict)