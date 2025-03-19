#1 write a program to store seven friitts in a listentered by the user 
#2 write a program to accept marks of 6 students and display them in a sorted manner
#3 check that a tuple type cannot be changed in a python
#4 write a program to sum a list with 4 numbers
#5 write a program to count the number of zeroes in the following tuple
    # a=(7,0,8,0,0,9)



#1
fruits=[]
f1=input("Enter fruit name:")
fruits.append(f1)
f2=input("Enter fruit name:")
fruits.append(f2)
f3=input("Enter fruit name:")
fruits.append(f3)
f4=input("Enter fruit name:")
fruits.append(f4)
f5=input("Enter fruit name:")
fruits.append(f5)
print(fruits)


#2
sortedmarks=[]
st1=input("science:")
sortedmarks.append(st1)
st2=input("mathematics:")
sortedmarks.append(st2)
st3=input("EVS:")
sortedmarks.append(st3)
st4=input("English:")
sortedmarks.append(st4)
st5=input("Hindi:")
sortedmarks.append(st5)
sortedmarks.sort()
print(sortedmarks)

# sometimes it doesnt work becuse there are strings so we need to use in(input)


#3
a=("jay",34,19)
a[2]="boy"



#4
a=[23,456,657,768]
print(sum(a))
# sum is a built in function


#5
a=(7,0,8,0,0,9)
total=a.count(0)
total=("The number of zeroes in the list is: ")
print(total)