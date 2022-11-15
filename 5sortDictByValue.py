'''Q5.
Write a Python program to sort (ascending and descending) a dictionary by value.

Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
'''
# d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# x=sorted(d.items(),key=lambda x:x[1])    
# x=sorted(d.items(),key=lambda x:x[0])  
# x=sorted(d.items(),key=lambda x:x[1],reverse=True)      
# x=sorted(d.items(),key=lambda x:x[0],reverse=True)      

# print(x)




d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
d1={}
l=[]
for i in d:
    l.append(d[i])
l.sort()
k=0
while(k<len(l)):
    for j in d.keys():
        if d[j]==l[k]:
            d1[j]=d[j]
    k+=1
print(d1)
print(list(d1.items()))
