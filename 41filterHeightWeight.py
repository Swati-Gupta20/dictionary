'''Q41.Write a Python program to filter the height and width of students, which are stored in a dictionary. 
Original Dictionary:
{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
Height > 6ft and Weight> 70kg:
{'Cierra Vega': (6.2, 70)}
'''

# d={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# hgt=6
# wgt=70
# for i in d:
#     if d[i][0]>=hgt and d[i][1]>=wgt:
#         print('{'+i+':',d[i],'}')


d={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
hgt=6
wgt=70
d1={}
for i in d:
    if d[i][0]>=hgt and d[i][1]>=wgt:
        d1[i]=d[i]
print(d1)

