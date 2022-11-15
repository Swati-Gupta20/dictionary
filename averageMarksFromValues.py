''' Sample Input
5 3
89 90 78 93 80
90 91 85 88 86 
91 92 83 89 90.5 

Sample Output
90.0 
91.0 
82.0 
90.0 
85.5        

Marks obtained by student 1: 89,90,91
Average marks of student 1:270/3 =90.0
'''

n=int(input("no of studends:-"))
n1=int(input("no of subjects:-"))
d={}
for i in range(n):
    name=input('enter name:-')
    marks=list(map(float,input().split()))
    d[name]=marks
# d={'swati': [89.0, 90.0, 78.0, 93.0, 80.0], 'prem': [90.0, 91.0, 85.0, 88.0, 86.0], 'uma': [91.0, 92.0, 83.0, 89.0, 90.5]}
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
