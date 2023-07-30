import turtle

colors = ["red", "purple", "blue", "green", "yellow", "orange"] #빨강 보라 파랑 초록 노랑 주황 색
t = turtle.Turtle()

turtle.bgcolor("black") #배경색
t.speed(0) #거북이 속도 (숫자가 커질수록 느려짐 0이 최고 속도)
t.width(3) #두께
length = 10 #길이 초기값 설정

while length < 500: #반복문 (길이가 500보다 작은 동안)
    t.forward(length)#길이만큼 앞으로 이동
    t.pencolor(colors[length%6]) #선의 색상을 colors 에서 선택 길이를 6으로 나눈
    t.right (89) #오른쪽으로 89도 회전하란 뜻
    length += 5 #선길이 5만큼 증가 시킴
