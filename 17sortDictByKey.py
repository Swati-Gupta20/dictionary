'''Q17.Write a Python program to sort a dictionary by key.
'''
d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# x=sorted(d)
# d1={}
# for i in x:
#     if i in d:
#         d1[i]=d[i]
# print(d1)



x=sorted(d.items(),key=lambda a:a[0])
print(x)