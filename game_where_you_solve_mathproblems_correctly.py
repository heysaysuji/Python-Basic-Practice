import random

def make_question():
    a = random.randint(1,40) #put random number from 1 to 40 in a
    b = random.randint(1,20) #put random number from 1 to 20 in b
    op = random.randint(1,3) #put random number from 1 to 3 in  op

    #make question at first string variable Q
    #save first number at q

    q = str(a) # change result of a(integer) to string and the save

    # add operator

    if op == 1:
        q = q + "+"

    if op == 2:
        q = q + "-"

    if op == 3:
        q = q + "*"

    # save second number at q

    q = q + str(b)
    #change result of b(intger) to string and then add at q

    #return the question
    return q

#reet sc1 and sc2 to 0, which saves the number how manyh correct/incorrect answers are.

sc1 = 0
sc2 = 0

for x in range(5): #five questions
    q = make_question() #make queston
    print(q) #print question
    ans = input("=")#receive answers from user
    r = int(ans) #change answer to the integer

    #compare the result with computers'(eval(q)) and users'
    if eval(q) == r:
        print("Correct!")
        sc = sc1 + 1

    else:
        print("incorrect!")
        sc2 = sc2 + 1

print("correct answers: ", sc1, "wrong answers: ", sc2)
if sc2 == 0:
    print("you are a genius!")
