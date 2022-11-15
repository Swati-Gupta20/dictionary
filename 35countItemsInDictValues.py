'''
Q35. Write a Python program to count the number of items in a dictionary value that is a list.
dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
Sample output: 5
'''
d={'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
c=0
for i in d:
    for j in d[i]:
        # print(j)
        c+=1
print(c)