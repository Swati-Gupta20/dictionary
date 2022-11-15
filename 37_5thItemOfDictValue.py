'''Q37.Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.
{'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
15
25
35
'''
l=[[11, 12, 13, 14, 15, 16, 17, 18, 19],[21, 22, 23, 24, 25, 26, 27, 28, 29],[31, 32, 33, 34, 35, 36, 37, 38, 39]]
k=['x','y','z']
d={}
p=0
for i in k:
    d[i]=l[p]
    p+=1
for j in d:
    print(d[j][5-1])