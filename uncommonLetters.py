'''
checking the uncommon letters from two string.
eg: 
s="scream"
s2="phone"
o/p => achmnops  (sorted)
explaination: only one letter (e) is common in both string so the other uncommon letters will be collected 
eg2:
s="heart"
s2="earth"
o/p= -1
explaination: all the letters are common in both string, so the output will be -1
'''

# s="scream"
# s2="phone"
s=input("enter 1st word:-")
s2=input("enter 2nd word:-")
o=''
for i in s:
    for j in s2:
        if j not in s and j not in o:
            o+=j
    if i not in s2 and i not in o:
        o+=i
if o=="":
    print('-1')
x=sorted(o)
m=''
for p in x:
    m+=p
print(m)