dict1={'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count=0
for i in dict1.values():
          for j in i:
                    count+=1
print(count)
