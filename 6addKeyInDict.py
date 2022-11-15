'''Q6.
Write a Python script to add a key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
'''
d={0: 10, 1: 20}
k=int(input('enter key:-'))
v=int(input('enter value:-'))
d[k]=v
print(d)