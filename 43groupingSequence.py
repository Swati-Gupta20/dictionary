'''Q43.Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists. 
Original list:
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
Grouping a sequence of key-value pairs into a dictionary of lists:
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
'''
l=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d={}
for i in l:
    l1=[]
    if i[0] not in d:
        d[i[0]]=l1
        d[i[0]].append(i[1])    
    else:
        d[i[0]].append(i[1])
print(d)