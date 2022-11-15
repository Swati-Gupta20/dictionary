'''Q15.Write a Python program to remove a key from a dictionary.
'''
d= {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def remove(x):
    if x in d:
        d.pop(x)
        print(d)
    else:
        print('key not found')
remove(7)
remove(4)