'''Q26.
Write a Python program to print a dictionary in table format.
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

Sample Output:

C1 C2 C3                                                                                                      
1 5 9                                                                                                         
2 6 10                                                                                                        
3 7 11
'''
d={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
l=[]
for i in d:
    print(i,end=" ")
    l.append(d[i])
print()
j=0
while j<len(l):
    k=0
    while k<len(l):
        print(l[k][j],end='  ')
        k+=1
    j+=1
    print()

# print(l)

