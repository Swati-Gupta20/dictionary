'''Q14.Write a Python program to multiply all the items in a dictionary.
'''
d= {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
pro=1
for i in d:
    pro*=d[i]
print(pro)