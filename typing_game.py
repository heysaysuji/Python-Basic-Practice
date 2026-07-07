
# typing game

import random
import time

#word list

w = ["cat", "dog", "fox", "momkey", "mouse", "panda", "frog", "snake", "wolf"]

n = 1 #number of question

print("typing game! click enter when you are ready!")
input() #wait until user press enter
start = time.time() #rercord the starting time

q = random.choice(w) #chcoose anything from the word list
while n <=5:
    print("*question", n)
    print(q) #print the question
    x = input() #receive the input friom the user
    if q == x: #if user wrote correclty
        print("success!")
        n = n+1 #add one in the number
        q = random.choice(w) #print the new question
    else:
        print("Wrong! one more chance!")

end = time.time() #record the finishing time
et = end = start #calculate the time used in game
et = format(et, ".2f") #mark up to the second decimal place
print("typing time:", et, "seconds")

