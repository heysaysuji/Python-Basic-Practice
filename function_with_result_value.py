def square(a):      #a의 제곱(a*a)를 구하는 함수. #A function that finds the square (a*a) of a.
    c = a * a
    return c


def triangle(a, h): #밑변이 a이고 높이가 h인 삼각형의 넓이를 구하는 함수  #a function of finding the area of a triangle with base a and height h 
    c = a * h / 2
    return c


s1 = 4
s2 = square(s1)     #s1(4)의 제곱을 구하는 함수를 호출해 결과를 s2에 저장합니다. #Call the function to find the square of s1(4) and save the result to s2.
print(s1, s2)

print(triangle(3,4)) #밑변이 3이고 높이가 4인 삼각형의 넓이를 호출. #Call the area of a triangle with base 3 and height 4.

