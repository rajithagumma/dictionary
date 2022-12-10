'''Write a Python program to sum all the items in a dictionary.'''
dict={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
sum=0
for i in dict:
          sum=sum+dict[i]
print(sum)
