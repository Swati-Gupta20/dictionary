'''Q27.Write a Python program to count the values associated with key in a dictionary.
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]

Sample input if key is id: then 6
'''

d=[{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]

key=input("enter key:-")
sum=0
for i in d:
    if key =='id':
        sum+=i[key]
    elif key=='success':
        print(i[key])
    elif key=='name':
        print(i[key])
if key=='id':
    print(sum)