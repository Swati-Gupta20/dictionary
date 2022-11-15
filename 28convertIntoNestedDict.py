'''Q28.Write a Python program to convert a list into a nested dictionary of keys.
num_list = [1, 2, 3, 4]
Sample output:
{1: {2: {3: {4: {}}}}}
'''
l= [1, 2, 3, 4]
d1=d={}
for i in l:
    d[i]={}
    d=d[i]
print(d1)

