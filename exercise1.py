# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:32:35 2018

@author: jasin
"""

# 1. Iterate over a list
lst = [0,1,2,3,4,5,6,7,8,9]

lst = list(range(1, 10))
type(lst)


lst.reverse()
lst
for i in lst:
    print(i," bottles of beer on the wall", i ," bottles of beer.")


lst2 = 'ACTG' *3 + 'TTATT' * 5
lst2

print(lst2)

suffix = lst2[1:]

for i in range(len(lst2)):
    print(lst2[i+1:]) #needs +1 otherwise it takes first position as well
    



for i in range(len(lst2)-2): #needs to stop on time!
    print(lst2[i:i+3])
    i = i+1


results = []
for i in range(len(lst2)-2): #needs to stop on time!
    #print(lst2[i:i+3])
    results.append(lst2[i:i+3])
    i = i+1
print(results)    


print(list(set(results)))

#OR

myset = set({})
type(myset)
for i in range(len(lst2)-2): #needs to stop on time!
    #print(lst2[i:i+3])
    myset.add(lst2[i:i+3])
    i = i+1
print(myset)    

#question 3 #%3 == 0 meqns is divisible by 3
for number in range(101):
    if number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 3 == 0 & number % 5 == 0:
        print('FizzBuzz')
    else:    
        print(number)
 
# 4. Combining lists
l1 = list(range(101))
l2 = list(range(101))
l1
l2
for x, y in zip(l1, l2):
    print(x, y)
    
#5 dictionaries
d = {}
for number in range(101):
    if math.sqrt(number) :
        d.update({number:'Fizz') 