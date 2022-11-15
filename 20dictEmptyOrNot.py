'''Q20.Write a Python program to check a dictionary is empty or not.
'''
d= {'a': 100, 'b': 200, 'c':300}
# d={}
def check(x):
    if len(x)>0:
        print('dictionary is not empty')
    else:
        print('dictionary is empty')
check(d)

