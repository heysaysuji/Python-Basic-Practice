import turtle as t

def turn_right(): #function that moves to the right side #오른쪽으로 이동하는 함수
    t.setheading(0) # = t.seth(0)
    
    t.forward(10) # = t.fd(10)


def turn_up(): #function that moves to the upper side #위로 이동하는 함수
    t.setheading(90)
    t.forward(10)


def turn_left(): #function that moves to the left side #왼쪽으로 이동하는 함수
    t.setheading(180)
    t.forward(10)

def turn_down(): #function that moves to the down side #아랫쪽으로 이동하는 함수
    t.setheading(270)
    t.forward(10)

def blank(): #function that erases the windows
    t.clear()

t.shape("turtle") #shape is turtle
t.speed(0) #the fastest speed
t.onkeypress(turn_right, "Right") #if i press the key --> , turn_right function will be initiated)
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank, "Escape") #when click the ESC, blank function will be initiated
t.listen() #turtle graphic window get input from the keyboard
