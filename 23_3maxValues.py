'''Q23.Write a Python program to find the highest 3 values of corresponding keys in a dictionary.'''



d={'a': 500, 'b': 5874, 'c': 900, 'd': 300, 'e': 5875, 'f':350, 'g': 200, 'h': 64, 'i': 780, 'j': 100}
k1=0
k2=0
k3=0
for i in d:
    if d[i]>k1:
        k1=d[i]
        v=i
for j in d:
    if d[j]>k2 and d[j]!=k1:
        k2=d[j]
        v1=j
for k in d:
    if d[k]>k3 and d[k]!=k1 and d[k]!=k2:
        k3=d[k] 
        v2=k   
print(v,':',k1)
print(v1,':',k2)
print(v2,':',k3)