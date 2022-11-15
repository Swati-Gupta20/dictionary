'''Q33.Python: Print a dictionary line by line
students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
Sample Output:

Aex                                                                                                           
class : V                                                                                                     
rolld_id : 2                                                                                                  
Puja                                                                                                          
class : V                                                                                                     
roll_id : 3
'''

d={'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
for i in d:
    print(i)
    for j in d[i]:
        print(j,':',d[i][j])