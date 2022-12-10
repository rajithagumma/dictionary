'''Q36.Write a Python program to match key values in two dictionaries. 
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y
'''

x={'key1': 1, 'key2': 3, 'key3': 2}
y={'key1': 1, 'key2': 2}
for i in x:
    for j in y:
        if i == j and x[i] == y[j]:
            print(i,":",x[i],"is present in both x and y")
