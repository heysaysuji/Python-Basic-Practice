# a program that you guess the number 


import random

n = random.randint(1,30)   #choose random number between 1 and 30

while True:     #repeat forever
    x = input("Guess the Number!")
    g = int(x)      #change the number to int (for easy-compare)
    if g == n:      #if random number = guessed number, it will be an answer
        print("Correct!")
        break       #if the answer is correct, get out of while repeat using break
    if g < n:
        print("It is too small!")
        
    if g > n:
        print("It is too big!")
