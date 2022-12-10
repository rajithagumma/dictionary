'''Write a Python program to sort (ascending and descending) a dictionary by value.

Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
'''
dict={1:2,3:4,4:3,2:1,0:0}
a=list(dict.keys())
i=0
newd={}
while i<len(a)-1:
          if dict[a[i]]>=dict(a[i+1]):
                    newd[a[i+1]]=dict[a[i]]
          i=i+1
print(newd)



