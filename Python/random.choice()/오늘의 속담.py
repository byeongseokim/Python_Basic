### 오늘의 속담 
import random
quotes = []

quotes.append("꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다.")
quotes.append("분노는 바보들의 가슴속에서만 살아간다..")
quotes.append("고생 없이 얻을 수 있는 진실로 귀중한 것은 하나도 없다.")
quotes.append("사람은 사랑할 때 누구나 시인이 된다.")
quotes.append("시작이 반이다.")

print("#         속담 리스트        #")
print(quotes[0])
print(quotes[1])
print(quotes[2])
print(quotes[3])
print(quotes[4])
print("")

dailyQuote = random.choice(quotes)
print("############################")
print("#         오늘의 속담       #")
print("############################")
print("")
print(dailyQuote)
