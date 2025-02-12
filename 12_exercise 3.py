#1  write a python program to display a user entered name followed by good afternoon using input function
#2 wriite a letter program to fill a letter template given below  
    #  with name and date 
'''    
      letter =||| Dear <|NAME>,
                         you are selected !
                         <|DATE|>
        '''
#3 write a program to detect double spaces in string
#4 replace the double spaces in problem 3 with string spaces 
#5 write a program to print the following using escape sequence characters

#  letter ="Dear teacher, this python course is nice"

#1
a=input("my name is:")
print(a)
b=(input("good afteroon"))
print(a,b)

# or

a=input("My father name: ")
print(f"You are a very hard working noble man {a}")


#2
letter =''' Dear <|NAME>,
             you are selected !
             <|DATE|>
        '''
print(letter.replace("<|NAME>","jay").replace("<|DATE|>","19 feb 2025"))



#3
a=("jay is a  good boy")
print(a.find("  "))


#4
a=("jay is a  good boy")
print(a.replace("  ",""))

#5
letter ="Dear teacher,\n\tthis python course is nice"
print(letter)
