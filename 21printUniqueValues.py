'''
Q21.Write a Python program to print all unique values in a dictionary. 

Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''

d=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
d1=[]
i=0
while i<len(d):
    for j in d[i]:
        if d[i][j] not in d1:
            d1.append(d[i][j])
    i+=1
print(set(d1))