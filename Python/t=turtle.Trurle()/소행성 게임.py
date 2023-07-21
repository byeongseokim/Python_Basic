### 소행성 게임(애스터로이드 게림)



import turtle
import random 
import math

player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)
screen = player.getscreen()

asteroids = []				# 공백 리스트를 생성한다. 
for i in range(10):			# 10개의 터틀을 생성한다. 
        a1 = turtle.Turtle()
        a1.color("red")
        a1.shape("circle")   #square, triangle, classic, turtle
        a1.penup()
        a1.speed(0)
        a1.goto(random.randint(-300, 300), random.randint(-300, 300))
        asteroids.append(a1)		# 생성된 터틀을 리스트에 추가한다. 

def turnleft():
	player.left(30)	# 왼쪽으로 30도 회전한다. 
	
def turnright():
	player.right(30)	# 오른쪽으로 30도 회전한다. 
	
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.listen()

def play():
        player.forward(2)			# 2픽셀 전진
        for a in asteroids:			# 리스트에 저장된 모든 터틀에 대하여
                a.right(random.randint(-180, 180))
                a.forward(2)
        screen.ontimer(play, 10)		# 10ms가 지나면 play()를 다시 호출
screen.ontimer(play, 10)
