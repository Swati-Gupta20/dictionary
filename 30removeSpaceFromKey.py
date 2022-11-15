'''
Q30.Write a Python program to remove spaces from dictionary keys.
Original dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}
'''


d={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
d1={}
for i in d:         
    if ' ' in i:
        b=i.replace(' ','')
        d1[b]=d[i]
print(d1)
        
        