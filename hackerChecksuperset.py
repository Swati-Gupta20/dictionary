'''https://www.hackerrank.com/challenges/py-check-strict-superset/problem?h_r=next-challenge&h_v=zen'''
'''
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
'''

A=set(map(int,input().split()))
n=int(input())
l=[]
for i in range(n):
    s=set(map(int,input().split()))
    c=0
    for j in A:
        if j not in s:
            c+=1
    if c==0:
        l.append(True)
    else:
        l.append(False)
len=len(l)
p=0
for x in l:
    if x==True:
        p+=1
if p==len:
    print(True)
else:
    print(False)

