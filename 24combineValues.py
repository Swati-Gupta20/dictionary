'''Q24.
Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})
'''

d= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
d1={}
for i in range(len(d)):
   if d[i]['item'] not in d1:
       d1[d[i]['item']]=d[i]['amount']
   else:
        d1['item1']=d1['item1']+d[i]['amount']  
print(d1)

