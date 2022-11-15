'''Q44.Write a Python program to split a given dictionary of lists into list of dictionaries.
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
'''

d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
l=[]
l1=[]
l2=[]
for i in d:
    l.append(i)
    l1.append(d[i])
for j in range(len(d)*2):
    d1={}
    for k in range(len(l)):
        d1[l[k]]=l1[k][j]
    l2.append(d1)
print(l2)