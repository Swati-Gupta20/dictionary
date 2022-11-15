'''Q22. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd
'''
d={'1':['a','b'], '2':['c','d']}
l=[]
for i in d:
    l.append(d[i])
for j in l[0]:
    for k in l[1]:
        print(j+k)