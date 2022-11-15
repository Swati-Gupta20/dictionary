''' Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

'''

# count method:-

# string='w3resource'
# d1={}
# for i in string:
#     if i not in d1:
#         d1[i]=string.count(i)
# print(d1)



# without count method:-



# string='w3resource'
# d1={}
# for i in string:
#     c=0
#     for j in string:
#         if i==j:
#             c+=1
#             d1[i]=c
# print(d1)


s='w3resource'
d1={}
i=0
while i<len(s):
    c=0
    j=0
    while j<len(s):
        if s[i]==s[j]:
            c+=1
            d1[s[i]]=c
        j+=1
    i+=1
print(d1)