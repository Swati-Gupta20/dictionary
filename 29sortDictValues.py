'''Q29.Write a Python program to sort a list alphabetically in a dictionary.
'''

# d={'g':'swati','k':'archana','a':'dolly','x':'tamanna','n':'sneha','e':'aditya'}
d= {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# for i in d:
#     j=0
#     while j<len(d[i]):
#         k=0
#         while k<len(d[i]):
#             if d[i][k]>d[i][j]:
#                 d[i][k],d[i][j]=d[i][j],d[i][k]
#             k+=1
#         j+=1
# print(d)
    
for i in d:
    for j in range(len(d[i])):
        for k in range(len(d[i])):
            if d[i][k]>d[i][j]:
                d[i][k],d[i][j]=d[i][j],d[i][k]
print(d)
