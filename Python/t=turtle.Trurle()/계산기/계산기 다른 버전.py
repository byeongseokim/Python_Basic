import turtle

# 터틀 그래픽 초기 설정
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

# 더하기 함수
def add(a, b):
    result = a + b
    return result

# 빼기 함수
def subtract(a, b):
    result = a - b
    return result

# 곱하기 함수
def multiply(a, b):
    result = a * b
    return result

# 나누기 함수
def divide(a, b):
    result = a / b
    return result

# 계산 결과를 그래픽으로 표시하는 함수
def display_result(result):
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.write("계산 결과: " + str(result), align="center", font=("Arial", 16, "normal"))

# 계산기 메인 함수
def main():
    a = int(input("첫 번째 숫자를 입력하세요: "))
    operator = input("연산자를 입력하세요 (+, -, *, /): ")
    b = int(input("두 번째 숫자를 입력하세요: "))

    result = 0
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = subtract(a, b)
    elif operator == '*':
        result = multiply(a, b)
    elif operator == '/':
        result = divide(a, b)
    else:
        print("잘못된 연산자입니다. +, -, *, / 중에서 선택하세요.")
        return

    display_result(result)

    turtle.done()

# 계산기 실행
main()
"""
이 코드는 사용자로부터 두 개의 숫자와 연산자를 입력받아 계산한 뒤, 터틀 그래픽으로 계산 결과를 출력합니다. 사용자는 첫 번째 숫자, 연산자, 두 번째 숫자를 차례로 입력하여 계산기를 사용할 수 있습니다. 계산 결과는 그래픽 창의 상단에 출력됩니다.
"""






