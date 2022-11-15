'''Q36.Write a Python program to match key values in two dictionaries. 
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y
'''

d={'key1': 1, 'key2': 3, 'key3': 2}
d1= {'key1': 1, 'key2': 2}
for i in d:
    if i in d1:
        if d1[i]==d[i]:
            print(i+':',d[i])