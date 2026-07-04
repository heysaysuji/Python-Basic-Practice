#Functions that draw  polygon


import turtle as t

def polygon(n):
    for x in range(n): #repeat n times n번 반복합니다
        t.forward(50)
        t.left(360/n)

def polygon2(n,a):
    for x in range(n): #repeat n times n번 반복합니다
        t.forward(a)
        t.left(360/n)

polygon(3)  #draw a triangle 삼각형 그리기
polygon(5) #draw a pentagon 오각형 그리기


#move turtle by 100 without drawing
#그림을 그리지 않고 거북이를 100만큼 이동

t.up()
t.forward(100)
t.down()

polygon2(3,75) #draw a triangle with a side length of 75 #한 변의 길이가 75인 삼각형 그리기
polygon2(5,100) #draw a pentagon with a side length of 100 #한 변의 길이가 100인 오각형 그리

