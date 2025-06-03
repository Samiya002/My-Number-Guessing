from random import randint
guessnum= randint(1,101)
a=0
i=1
for i in range(1,11):
    b= int(input("Enter the number from 1 to 100:"))
    a+=1
    if(b== guessnum):
        print("Correct")
        break
    elif(b<guessnum):
        print("Too low!")
    elif(b>guessnum):
        print("Too high!")
print("Attempts Made:",a)
print("Attempts Left:",10-a)
print("Number is",guessnum)