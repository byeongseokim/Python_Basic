import turtle

def tree(length):
    if length > 5:			# length가 5보다 크면 순환호출을 한다. 
        t.forward(length)		# 거북이가 length 만큼 선을 그린다. 
        t.right(20)			# 오른쪽으로 20도 회전한다. 
        tree(length-15)		# (length-15)를 인수로 tree()를 순환 호출한다. 
        t.left(40)			# 왼쪽으로 40도 회전한다. 
        tree(length-15)		# (length-15)를 인수로 tree()를 순환 호출한다. 
        t.right(20)			# 오른쪽으로 20도 회전한다. 
        t.backward(length)		# length만큼 뒤로 간다. 제자리로 돌아온다. 

t = turtle.Turtle()
t.left(90)				# 거북이가 위쪽을 향하게 한다. \


t.color("green")				# 선의 색을 녹색으로 한다. 
t.speed(1)				# 속도를 제일 느리게 한다.
tree(90)				# 길이 90으로 tree()를 호출한다. 
