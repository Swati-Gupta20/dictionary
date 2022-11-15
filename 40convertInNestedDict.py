'''Q40. Write a Python program to convert more than one list to nested dictionary. 

Original strings:
['S001', 'S002', 'S003', 'S004']
['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
[85, 98, 89, 92]
Nested dictionary:
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
'''
l=['S001', 'S002', 'S003', 'S004']
l1=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
l2=[85, 98, 89, 92]
nl=[]
for i in range(len(l1)):
    d={}
    d2={}
    d[l1[i]]=l2[i]
    d2[l[i]]=d
    nl.append(d2)
print(nl)
