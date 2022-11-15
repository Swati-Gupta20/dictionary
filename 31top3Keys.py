'''
Q31.. Write a Python program to get the top three items in a shop. Go to the editor
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
Expected Output:
item4 55
item1 45.5
item3 41.3
'''

d={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
max=0
smax=0
tmax=0
for i in d:
    if d[i]>max:
        k1=i
        max=d[i]
for j in d:
    if d[j]>smax and d[j]!=max:
        k2=j
        smax=d[j]
for k in d:
    if d[k]>tmax and d[k]!=max and d[k]!=smax:
        k3=k
        tmax=d[k]
print(k1,max,)
print(k2,smax)
print(k3,tmax)
