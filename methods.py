mydata={'name':'swati','age':20,'city':'delhi'}
# x=mydata['age']
# print(x)

# get() method:-

# x=mydata.get('age')
# print(x)

# keys() method:

# x=mydata.keys()
# print(x)

# values()method:

# x=mydata.values()
# print(x)

# items() method:-

# x=mydata.items()
# print(x)    

# adding & updating items:-

# mydata['college']='ignou'
# mydata['city']='bangalore'
# print(mydata)

# key exists or not:-

# if 'city' in mydata:
#     print('yes, city is bangalore')
# else:
#     print('city does not exists')

# removing elements from dictionary:-

# mydata.pop('city')
# mydata.popitem()
del mydata['age']
print(mydata)