'''Q8.
Write a Python program to check whether a given key already exists in a dictionary.
'''
d={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
def checkKey(x):
    if x in d:
        print('yes',x,'named key is present')
    else:
        print(x,'named key is not present')
checkKey(5)