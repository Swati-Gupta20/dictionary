'''https://www.hackerrank.com/challenges/py-check-subset/problem'''

'''
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2'''
# t=int(input())
# for i in range(t):
#     eA=int(input('no. of elements in A:-'))
#     A=set(map(int,input().split()))
#     eB=int(input('no. of elements in B:-'))
#     B=set(map(int,input().split()))
#     print(A.issubset(B))


t=int(input())
for i in range(t):
    eA=int(input('no. of elements in A:-'))
    A=set(map(int,input().split()))
    eB=int(input('no. of elements in B:-'))
    B=set(map(int,input().split()))
    c=0
    for j in A:
        if j not in B:
            c+=1
    if c==0:
        print(True)
    else:
        print(False)
