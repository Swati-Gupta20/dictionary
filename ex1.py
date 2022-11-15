# person={
# 'name':'jack',
# 'age':20,
# 'gender':'male',
# 4:'organization'
# }

# result = person['age'] 
# x = person.get('gender')
# print(person[4])
# print(x)
# print(result)


# l=['one','two','three','four','five','six']
# l2=['neem','bamboo','banyan','peepal','sheesham','babul']
# d1={}
# d2={}
# i=0
# while(i<len(l)):
#     d1[i+1]=l[i]
#     d2[i+1]=l2[i]
#     i+=1
# print(d1)
# print(d2)

# d={1:50, 2:30, 4:60, 5:60, 6:30}
# # o/p: {50:[1],30:[2,6],60:[5,4]}
# d1={}
# for j in d:
#     l=[]
#     for k in d:
#         if d[k]==d[j]:
#             l.append(k)
#             d1[d[j]]=l
# print(d1)

# for i in d:
#     if d[i] not in d1:
#         d1[d[i]]=[i]
#     else:
#         d1[d[i]].append(i)
# print(d1)
# print(d[0])



# d={'a':[1,2,3],'b':[8,2,4]}
# # o/p:{'a':6,'b':14}
# d1={}

# for i in d:
#     sum=0
#     for j in d[i]:
#         sum+=j
#     d1[i]=sum
# print(d1)    




a='abcdabcefegh'
d={}
i=0
while(i<len(a)):
    b=a.count(a[i])
    if a[i] not in d:
        d[a[i]]=b
    i+=1
# for j in d:
#     if d[j]==1:
#         x=a.index(j)
#         print(x)
#         break
l=[]
for j in d:
    if d[j]==1:
        f=0
        while(f<len(a)):
            if j==a[f]:
                l.append(f)
            f+=1
print(l[0])
        