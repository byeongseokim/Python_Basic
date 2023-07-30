"""
import turtle 
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def draw_line():
    t.forward(100)
    t.backward(100)

for x in range(12):
	t.right(30)
	draw_line()

def happyBirthday(person):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + person)
    print("Happy Birthday to you!")

happyBirthday("홍길동")

def sumProblem(x, y):
    sum = x + y
    sentence = "정수" + str(x) + "+"+str(y)+"의 합은?"
    print(sentence)

def main():
    a = int(input("첫 번째 정수: "))
    b = int(input("두 번째 정수: "))
    sumProblem(a, b)

main()

PI = 3.14159265358979   

def circleArea(radius):
    return PI*radius*radius    

def circleCircumference(radius):
    return 2*PI*radius         

def main():
    print('반지름이 5인 원의 면적:', circleArea(5))
    print('반지름이 5인 원의 둘레:', circleCircumference(5))

main()
"""
def add(a, b):
    print( "(%d + %d)" % (a, b), end=" ")
    return a + b

def subtract(a, b):
    print ("(%d - %d)" % (a, b), end=" ")
    return a - b

def multiply(a, b):
    print ("(%d * %d)" % (a, b), end=" ")
    return a * b

def divide(a, b):
    print ("(%d / %d)" % (a, b), end=" ")
    return a / b


what = multiply(20, 10)
print("= ", what)

