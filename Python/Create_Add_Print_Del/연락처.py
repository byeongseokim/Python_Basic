phone_book = { }
phone_book["홍길동"] = "010-1234-5678"
print(phone_book)



phone_book = {"홍길동": "010-1234-5678"}   #생성 및 초기화 
phone_book["강감찬"] = "010-1234-5679"  #추가 
phone_book["이순신"] = "010-1234-5680"  #추가
print(phone_book)



phone_book = { }
phone_book["홍길동"] = "010-1234-5678"
phone_book["강감찬"] = "010-1234-5679"
phone_book["이순신"] = "010-1234-5680"
print(phone_book["강감찬"])
phone_book.keys()    #print(phone_book.keys())
phone_book.values() #print(phone_book.values())


dict = {'Name': '홍길동', 'Age': 7, 'Class': '초급'}
print (dict['Name'])
print (dict['Age'])


phone_book = { }
phone_book["홍길동"] = "010-1234-5678"
phone_book["강감찬"] = "010-1234-5679"
phone_book["이순신"] = "010-1234-5680"
for key in sorted(phone_book.keys()):
    print(key, phone_book[key])

del phone_book["홍길동"]
print(phone_book)
