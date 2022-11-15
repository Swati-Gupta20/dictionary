'''Q1.Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
'''

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}
# for i in d1:
#     if i not in d2:
#         d3[i]=d1[i]
#     else:
#         d3[i]=(d1[i]+d2[i])
#     for j in d2:
#         if j not in d3:
#             d3[j]=d2[j]
# print(d3)
a=list(d1)
b=list(d2)
# i=0
# while i<len(a):
#     if a[i] not in d3:
#         d3[a[i]]=d1[a[i]]
#     else:
#         d3[a[i]]=d3[a[i]]+d1[a[i]]
#     i+=1
# j=0
# while j<len(b):
#     if b[j] not in d3:
#         d3[b[j]]=d2[b[j]]
#     else:
#         d3[b[j]]=d3[b[j]]+d2[b[j]]
#     j+=1   

i=0
while i<len(a):
    if a[i] not in d3:
        d3[a[i]]=d1[a[i]]
    if b[i] not in a:
        d3[b[i]]=d2[b[i]]
    else:
        d3[b[i]]=d3[b[i]]+d2[b[i]]

    i+=1
print(d3)

