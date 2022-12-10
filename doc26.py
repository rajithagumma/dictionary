'''Write a Python program to print a dictionary in table format.
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

Sample Output:

C1 C2 C3                                                                                                      
1 5 9                                                                                                         
2 6 10                                                                                                        
3 7 11
'''
dic={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for i in dic:
          print(i,end=" ")
print()
d=[]
for j in dic:
          v=dic[j]
          d.append(v)
k=0
while k<len(d):
          a=0
          while a<len(d):
                    print(d[a][k],end=" ")
                    a=a+1
          k=k+1
          print()


          

