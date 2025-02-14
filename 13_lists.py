# Lists are basicallly nothing but container whuich can contain any type of value of any dataype
'''
In lists we basically use square bracets[]
'''#And unlike strings lists are mutable that is we can change the values of it

fruits=["apple","grapes","mango","banana"]
print(fruits[0])
'''here the o/p will be apple beacuse we chose the index 0 
'''
print(fruits[3])
'''here the o/p is banana because it is present in 3 index
'''

'''As we know thats lists are mutable (that is their values can be changed ) unlike strings which
 are immutable '''
# lets say
fruits[2]="papaya"
print(fruits)
print(fruits[3]) #prints o/p present in index 3

# we can even use list slicing here aswell
# lets say
print(fruits[1:3])