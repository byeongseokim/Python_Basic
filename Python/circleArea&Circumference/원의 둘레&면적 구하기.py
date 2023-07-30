PI = 3.14159265358979   

def circleArea(radius):
    return PI*radius*radius    

def circleCircumference(radius):
    return 2*PI*radius         

def main():
    print('반지름이 5인 원의 면적:', circleArea(5))
    print('반지름이 5인 원의 둘레:', circleCircumference(5))

main()
