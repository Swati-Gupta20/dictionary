
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
#     w1=a[i]
#     for j in range(len(a)):
#         if w1!=a[j] and len(w1)==len(a[j]):
#             c=0
#             for x in a[j]:
#                 if x in w1 and w1 not in l:
#                     c+=1
#             if c==len(a[j]):
#                 l.append(a[j])
# print(l)

a=["anagrams", "typhon","scripts","argnamas", "python","scrotch"]
l=[]
for i in range(len(a)):
    w1=a[i]
    for j in range(len(a)):
        if w1!=a[j] and len(w1)==len(a[j]):
            c=0
            for x in w1:
                if x in a[j] and a[j] not in l:
                    c+=1
            if c==len(a[j]):
                l.append(w1)
print(l)