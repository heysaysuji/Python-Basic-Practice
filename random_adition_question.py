import random

a = random.randint(1,30)    #Store any number between 1 and 30 in a.a에 1~30 사이의 임의의 수를 저장합니다.
b = random.randint(1,30)       #Store any number between 1 and 30 in b. b에 1~30 사이의 임의의 수를 저장합니다.

print(a, "+", b, "=")           #Print the question 문제를 출력합니다
x = input()                 #Take the answer and save it to x (saved as a string) 답을 입력받아 x에 저장합니다 (문자열로 저장됩니다)
c=int(x)                  #Replace the string with an integer for comparison. 비교를 위해 문자열을 정수로 바꿉니다.


if a + b == c:
    print("천재!")
else:
    print("바보!")
