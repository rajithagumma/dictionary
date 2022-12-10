# '''Q49.Python: Access dictionary key’s element by index
# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# physics
# math
# chemistry
# '''
# num = {'physics': "80", 'math': "90", 'chemistry': "86"}
# # for i in num:
# #           print(i)
# # print(len(num))
# i=0
# while i<len(num):
#           print(num[i])
#           i=i+1

a=[2,3,4]
i=0
s=0
c=[]
while i<len(a):
          s=s+a[i]
          c.append(s)
          i=i+1
print(c)