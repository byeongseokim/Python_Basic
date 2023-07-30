items = {"커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5 }

print (items)

menu = 1

while menu != 0:
    menu = int(input("메뉴를 선택하세요 [1:변경, 2:추가, 3:삭제, 0:종료] : "))
    
    if menu == 1:
        print("* 재고 변경 *")
        item = input("물건의 이름을 입력하시오: ");
        val = input("물건의 재고 수량을 입력하시오: ");
        items[item] = val
        print(items)
    elif menu == 2:
        print("* 재고 추가 *")
        item = input("물건의 이름을 입력하시오: ");
        val = input("물건의 재고 수량을 입력하시오: ");
        items[item] = val
        print(items)
    elif menu == 3:
        print("* 재고 삭제 *")
        item = input("물건의 이름을 입력하시오: ");
        del items[item]
        print(items)
