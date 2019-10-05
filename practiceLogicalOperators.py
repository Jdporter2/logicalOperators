'''
Created on Oct 5, 2019

@author: ITAUser
'''

print(4==4 and 6==6)
print(4==4 and 6==5)
print(4==4 and (6==5 or 2<5) or 25<9)

a = False
b = 20 > 9
c = 1==1
print(a and b and c)
print(b and (a or c))