#turtlerun2

import turtle as t
import random

score = 0 #save the score
playing = False #check wheter game is now playing or not

te = t.Turtle() #evil turtle(red colour)
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0,200)

ts = t.Turtle() #prey(green colour circle)
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -200)

def turn_right(): #turn right
    t.setheading(0)

def turn_up():
    t.setheading(90)
    #turn up

def turn_left(): #turn left
    t.setheading(180)

def turn_down():
#turn down
    t.setheading(270)

def start(): #start the game
    global playing
    if playing == False:
        playing = True
        t.clear() #remove the message
        play()

def play(): #Play the game
    global score
    global playing
    t.forward(10)
    if random.randint(1,5) == 3: #if number 3 selected between 1 and 5 (20%)
        ang = te.towards(t.pos())
        te.setheading(ang) #devil turtle look at main turtle
    speed = score + 5 # give 5 in score and speed up

    if speed > 15:
        speed = 15 #speed should not be more than 15

    te.forward(speed)
    if t.distance(te) < 12: #distance between devil and main turtle is smaller than 12
        #stop the game

        text = "Score : " + str(score)
        message("Game Over", text)
        playing = False
        score = 0

    if t.distance(ts) < 12: #if distance between main turtle and prey is smaller  than 12
                score = score + 1
                t.write(score) #up 1 in score and display in windows
                star_x = random.randint(-230, 230)
                star_y = random.randint(-230, 230)
                ts.goto(star_x, star_y) #change the location of prey

    if playing:
        t.ontimer(play, 100) #if the game is playing, after 0.1 second execute the play function



def message(m1, m2): #function that displays message
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home()

t.title("Turtle Run")
t.setup(500,500)
t.bgcolor("lightblue")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right,"Right") #if click -> button, execute the turn_right function
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(turn_up, "Up")
t.onkeypress(start, "space")
t.listen()
message("Turtle Run", "[Space]")

