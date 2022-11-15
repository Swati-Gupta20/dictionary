n=int(input('enter no. of times:-'))

d={}
for i in range(n):
    k=input('enter key:-')
    v=list(map(str,input().split()))
    d[k]=v
print(d)

d={'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

def combi():
    digit=input('enter no.:-')
    if digit=="" or digit==' ':
        print([])
    elif digit.isalpha():
        print('enter no not alphabet')
        again=combi()
    elif len(digit)==1:
        print(d[digit])
    elif len(digit)==2:
        l=[]
        for i in range(len(d[digit[0]])):
            for j in range(len(d[digit[1]])):
                com=d[digit[0]][i]+d[digit[1]][j]
                l.append(com)
        print(l)
    else:
        print('enter maximum 2 digits')

combi()