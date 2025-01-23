# 1 Write va program to print Twinkle twinkle lithe Star poem in python
# 2 Use REPL. and print the table of 5 using it
# 3 Install an external module and use it to perform an operation of your interest 
# 4 Write a python program to print the contents a directory using 05 module. Search online for the function which does that. of 5 2 3
#  Label the program written in Problem 4 with comments 

#1
print ("Twinkle, twinkle, little star\n how i wonder what you are\n up above the world so high \n like a diamond in the sky")


#2
import pyttsx3
engine = pyttsx3.init()
engine.say(" ooooooooooooooits a new dawn its a new day its a new life for me and i am feeling good")
engine.runAndWait()


#3
import os

directory_path = 'C:/Users'
contents= os.listdir(directory_path)
print(contents)


#4
 

