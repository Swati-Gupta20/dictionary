# states_capitals = {
#   'Gujarat' : 'Gandhinagar',
#   'Maharashtra' : 'Mumbai',
#   'Rajasthan' : 'Jaipur',
#   'Bihar' : 'Patna'
#   }
# # iterate over keys:-
# for state in states_capitals:
#   print(state)

# # iterate over values:-
# for state in states_capitals:
#   print(states_capitals[state])

'''3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika'''


# n = int(input())
# student_marks = {}
# for _ in range(n):
#   name, *line = input().split()
#   scores = list(map(float, line))
#   student_marks[name] = scores
# query_name = input()
# sum=0
# c=0
# for i in student_marks[query_name]:
#     sum+=i
#     c+=1
# ave=sum/c
# # print(ave)
# print(format(ave,'.2f'))


# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d={}
# d.update(d1)
# d.update(d2)
# print(d)

# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# d={}
# for i in dic1:
#   if i not in d:
#     d[i]=dic1[i]
#   else:
#     d[i]=d[i]+dic1[i]
# for i in dic2:
#   if i not in d:
#     d[i]=dic2[i]
#   else:
#     d[i]=d[i]+dic2[i]
# for i in dic3:
#   if i not in d:
#     d[i]=dic3[i]
#   else:
#     d[i]=d[i]+dic3[i]

# print(d)




# a='this is a string'
# n=a.split()
# p='-'.join(n)
# print(p)   


T=int(input())
for i in range(T):
    num=int(input())
    sum=0
    for j in str(num):
        sum+=int(j)
    print(sum)
