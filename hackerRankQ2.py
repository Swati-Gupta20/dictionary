'''https://www.hackerrank.com/challenges/py-the-captains-room/problem?h_r=internal-search'''
'''
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
'''

k=int(input())
l=list(map(int,input().split()))
rl=set(l)
for i in rl:
    l.remove(i)
    if i not in l:
        print(i)
