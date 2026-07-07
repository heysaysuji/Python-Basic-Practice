#toss the turtle game

import turtle as t
import random

def turn_up(): #function when press the up key
    t.left(2) #거북이를 왼쪽으로 2도 돌립니다

def turn_down(): #function when press the down key
    t.right(2) #거북이를 오른쪽으로 2도 돌립니다

def fire(): #shoot the fire when click the enter
    ang = t.heading() #현재 거북이가 바라보는 각도를 기억합니다 remember the angle which turtle is looking now
    while t.ycor() > 0: #거북이가 땅 위에 있는 동안 반복합니다 repeat when the turtle is on the ground
        t.forward(15) #move 15 forward 앞으로 15만큼 이동합니다
        t.right(5) #오른쪽으로 5도 회전합니다
        
    #while 반복문을 빠져나오면 거북이가 땅에 닿은 상태이니다.
    #when it is outsisde of while, it means turtle is on the ground

    d = t.distance(target, 0) #거북이와 목표 지점과의 거리를 구합니다. calcaulte the distance between target and turtle
    t.sety(random.randint(10,100)) #성공 또는 실패를 표시할 위치를 지정합니다. set the location where to put the result(success or fail)
    if d<25: #if the distance different is lower than 25, it is success
        t.color("blue")
        t.write("Good!", False, "center", ("", 15))

    else: #if not, it is fail
        t.color("red")
        t.write("Bad!", False, "center", ("", 15))
        
    t.color("black") #change the colour to black again
    t.goto(-200,10) #거북이를 처음 발사시킨곳으로 되돌림 move the turtle to the first place where the first tossing occured. 
    t.setheading(ang) #각도도 처음 기억해 둔 각도로 되돌림 change the angle to the first angle
    

#draw land
t.goto(-300, 0)
t.down()
t.goto(300,0)

#목표 지점을 설정하고 그립니다
#set the target and draw

target = random.randint(50, 150) #set the target between 50 to 150
t.pensize(3)
t.color("green")
t.up()
t.goto(target - 25, 2)
t.down()
t.goto(target + 25, 2)

#change the colour of turtle black and go back to the prior location

t.color("black")
t.up()
t.goto(-200, 10)
t.setheading(20)

#make the setting that used for the turtle

t.onkeypress(turn_up, "Up") #when press the Up key, it execute
t.onkeypress(turn_down, "Down") #when press the Down key, it execute
t.onkeypress(fire, "space") #when press the SpaceBar, fire function executes

t.listen() #turtle get inputs from keyboard
    
