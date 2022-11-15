''' output:-
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}
{1: 'neem', 2: 'bamboo', 3: 'banyan', 4: 'peepal', 5: 'sheesham', 6: 'babul'}
'''
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


'''
o/p: {50:[1],30:[2,6],60:[5,4]}
'''
# d={1:50, 2:30, 4:60, 5:60, 6:30}
# d1={}
# for j in d:
#     l=[]
#     for k in d:
#         if d[k]==d[j]:
#             l.append(k)
#             d1[d[j]]=l
# print(d1)

# single loop:-

# for i in d:
#     if d[i] not in d1:
#         d1[d[i]]=[i]
#     else:
#         d1[d[i]].append(i)
# print(d1)


# t=int(input('enter no of times:-'))
# d={}
# for i in range(t):
#     name=input('enter name:-')
#     age=int(input('enter age:-'))
#     d[name]=age
# print(d)
# maxAge=0
# for j in d:
#     if d[j]>maxAge:
#         maxAge=d[j]
# print(maxAge)
# d1={maxAge:[]}
# for k in d:
#     if d[k]==maxAge:
#         d1[maxAge].append(k)
# print(d1)


'''
anagrams: a word, phrase, or name formed by rearranging the letters of another.
arr=["anagrams", "typhon","scripts","argnamas", "python","scrotch"]
check whether the array consist anagrams or not
output = ['anagrams','typhon']
if there are pairs of anagrams, store the first apperance only in the list

'''

# a=["anagrams", "typhon","scripts","argnamas", "python","scrotch"]
# l=[]

# for i in range(len(a)):
#     d={}
#     for j in a[i]:
#         if j not in d:
#             c=a[i].count(j)
#             d[j]=c
#         # print
#         l.append(d)

# print(l)



# n=int(input("no of studends:-"))
# n1=int(input("no of subjects:-"))
# d={}
# for i in range(n):
#     name=input('enter name:-')
#     marks=list(map(float,input().split()))
#     d[name]=marks
# # print(d)


n=int(input("no of studends:-"))
n1=int(input("no of subjects:-"))
# # d={}
# # for i in range(n):
# #     name=input('enter name:-')
# #     marks=list(map(float,input().split()))
# #     d[name]=marks
d={'swati': [89.0, 90.0, 78.0, 93.0, 80.0], 'prem': [90.0, 91.0, 85.0, 88.0, 86.0], 'uma': [91.0, 92.0, 83.0, 89.0, 90.5]}
def ave(k,d):    
    sum=0
    for j in d:
        sum+=d[j][k]
    average=sum/n
    print(average)

def iterate(k):
    for k in range(n1):
        q=ave(k,d)
    
iterate(0)


         


