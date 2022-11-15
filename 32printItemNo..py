'''
Q32.Write a Python program to get the key, value and item in a dictionary.
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
Sample Output:

key  value  count                                                                                             
1     10      1                                                                                               
2     20      2                                                                                               
3     30      3                                                                                               
4     40      4                                                                                               
5     50      5                                                                                               
6     60      6
'''

d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
c=0
print('key','value','count')
for i in d:
    c+=1

    print(i,' ',d[i],'  ',c)