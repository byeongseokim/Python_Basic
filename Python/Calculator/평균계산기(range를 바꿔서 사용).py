alist = []
sum = 0

for i in range(5):
    i = int(input("정수를 입력하시오: "))
    alist.append(i)

for i in alist:
    sum += i
avg = sum/len(alist)
print("평균=", avg)
