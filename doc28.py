'''Q28.Write a Python program to convert a list into a nested dictionary of keys.
num_list = [1, 2, 3, 4]
Sample output:
{1: {2: {3: {4: {}}}}}
'''
num=[1, 2, 3, 4]
new=dic={}
for i in num:
          dic[i]={}
          dic=dic[i]
print(new)