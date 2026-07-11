# make a turtle run

import turtle as t
import random

te = t.Turtle() #bad turtle evil turtle
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0,200)

ts = t.Turtle() #prey (green circle)
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -200)

def turn_right(): #turn right
    t.setheading(0)

def turn_up(): #turn up
    t.setheading(90)

def turn_left(): #turn left
    t.setheading(180)

def turn_down(): #turn down
    t.setheading(270)

def play(): #function that execute games
    t.forward(10)
    ang = te.towards(t.pos()) #main turtle moves forward 10
    te.setheading(ang) #evil turtle look at the main turtle
    te.forward(9) #evil turtle move forward 9
    if t.distance(ts) < 12: #if the main turtle and the pray's distance is smaller than 12(close)
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        ts.goto(star_x, star_y) #change the location of the pray

    if t.distance(te) >= 12: #if the distance between evil turtle and main turtle is more than 12(far)
        t.ontimer(play, 100) #execute the play function after 0.1 second (game continue)


t.setup(500,500)
t.bgcolor("pink")
t.shape("turtle") #use the turtle shape cursor

t.speed(0) #the fastest turtle speed
t.up()
t.color("white")
t.onkeypress(turn_right, "Right") #execute turn_right when press --> button
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen() #turtle graffic windows receives the  input from the keyboard
play() #execute play function to start the game
        
