'''Q11.Write a Python script to merge two Python dictionaries
'''
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'d': 300, 'e': 200, 'f':400}
d3={}
for i in d1,d2:
    d3.update(i)
print(d3)