# 인터페이스 출력 함수
def interface():
    print("""
    ***************************************
    *         김    밥    천   국           *
    ***************************************
    """)
    print(" 1. 메뉴고르기")
    print(" 2. 결제하기")
    print(" 3. 총 매출(관리자 전용)")
    print(" Z. 프로그램 종료")
    print("-" * 50)


# user_input을 받을 때 "선택지를 골라주세요"를 자주 사용하여 함수화
def get_user_input():
    user_input = input(" 선택지를 골라주세요 >> ")
    print("-" * 50)
    return user_input


# 주문내역을 출력 함수
# selected_menu_list을 받아 출력
# 함수가 select_menu, show_payment에서 사용됨
def print_selected_menu(selected_menu_list):
    print("\n\n [주문내역]")
    count = 1
    for i in selected_menu_list:
        print(f"{count}. {i}", end=' | ')
        count += 1
    print("")
    print("")


# 메뉴 선택 함수
# 메뉴판 출력
# 메뉴 추가 및 삭제
def select_menu(food_dict, selected_menu_list):
    while True:
        # 1.  메뉴판 출력
        # !!문자열 정렬 방법 찾는중
        # count를 활용하여 한 줄에 5개의 메뉴가 나오도록함

        count = 0
        print()
        print("%50s" % "[메뉴판]")
        for k, v in food_dict.items():
            print(f"{k}. {v[0]}:{v[1]}", end=' ')
            count += 1
            if count == 5:
                print()
                count = 0

        # 2. 선택된 메뉴 출력
        print_selected_menu(selected_menu_list)

        # 3, 선택지 입력
        #  메뉴 번호 입력, M. 메뉴 삭제, Z. 뒤로가기
        print("메뉴 번호를 입력하세요 (M. 메뉴삭제, Z. 뒤로가기)")

        user_input = get_user_input()

        # 4. 주문내역 저장
        # input()이 메뉴판의 key값에 있는 경우에만
        # value값을 selected_menu_list에 append
        # !!input이 food_dict의 key값에 있는 경우에만 *향후 코드 수정시 문제가 있을지도?
        # 없는 key값을 입력한 경우에는 while문을 통해 메뉴판부터 다시 출력됨
        if user_input in [str(i + 1) for i in range(len(food_dict) + 1)]:
            selected_menu_list.append(food_dict[user_input])

        # 5. 주문내역 삭제
        # selected_menu_list에서 index number를 받아 del로 삭제
        # -1은 selected_menu가 1부터 시작하기에
        # 예외 처리?
        elif user_input.upper() == 'M':
            print("삭제를 원하는 메뉴의 번호(주문내역에서)를 입력하세요")
            menu_delete_num = get_user_input()
            del selected_menu_list[int(menu_delete_num) - 1]

        # 6. 뒤로가기
        elif user_input.upper() == 'Z':
            break


# 결제 메뉴
# 주문내역 출력
# selected_menu_list를 통해 주문 총액 계산
# 포장, 매장, 배달 선택
# selected_menu_list에 메뉴 개수에 따라 할인율 적용

def show_payment(selected_menu_list, payment_list):
    while True:
        # 1. 주문내역 출력
        print_selected_menu(selected_menu_list)

        # 2. 주문한 음식의 총액 계산
        total = 0
        for i in range(len(selected_menu_list)):
            total += selected_menu_list[i][1]

        # 3. 결제 선택지
        # 최초 place_cost = 0
        # 포장 : 10퍼 할인
        # 매장 : 그대로 (pass활용)
        # 배달 : +8900

        print(" [결제하기]")
        print(" [1] 포장 (10%할인) [2] 매장  [3] 배달 (배달비:8900) [Z] 뒤로가기")
        place_to_eat = get_user_input()
        place_cost = 0

        if place_to_eat == '1':
            place_cost = int(total * (-0.1))
        elif place_to_eat == '2':
            pass
        elif place_to_eat == '3':
            place_cost = 8900
        elif place_to_eat == 'z':
            break
        else:
            print(" 잘못입력하셨습니다. 다시 선택지를 골라주세요. \n ")
            continue

        # 4. 할인율 적용
        # 최초 sale_price = 0
        # 나머지는 메뉴 개수에 따라 반영
        sale_price = 0

        if len(selected_menu_list) == 2:
            sale_price = int(total * 0.2)
        elif len(selected_menu_list) == 3:
            sale_price = int(total * 0.25)
        elif len(selected_menu_list) >= 4:
            sale_price = int(total * 0.4)
        else:
            pass

        # 5. 최종 결제 금액 출력
        final_price = total + place_cost - sale_price

        print("주문표")

        print(f"총 주문액 : {total}")
        print("-" * 30)
        print(f"장소 비용 : {place_cost}")
        print(f"할인 금액 : {-sale_price}")
        print("-" * 30)
        print(f"최종 금액 : {final_price}")

        # 6. 결제확인
        # Y를 입력한 경우
        # payment_list에 매출액 append()
        # 주문내역 초기화
        # N을 입력한 경우
        # 초기화면으로 돌아감

        print("결제하시겠습니까? (Y/N)")
        payment_check = get_user_input()
        if payment_check.upper() == 'Y':
            print(" 결제완료 \n\n")
            payment_list.append(final_price)
            selected_menu_list.clear()
            break

        elif payment_check.upper() == 'N':
            print(" 초기화면으로 돌아갑니다. \n\n")
            break
        else:
            print(" 잘못입력하셨습니다. 다시 선택지를 골라주세요. \n ")
            continue


# 총 매출 출력 함수, **비밀번호 확인**
# 비밀번호가 맞는 경우 [매출] 출력
# 아닌경우 함수 종료
# password는 실행문의 변수로 설정
# profit_sum은 payment_list에 입력된 매출 정보를 sum을 통해 계산됨
def show_profit(password, profit_sum):
    print("[매출현황] \n 비밀번호를 입력하세요: ", end='')
    password_input = input()
    if password_input == password:
        print(f" 총 매출 : {profit_sum} ")
        print()
    else:
        print(" 비밀번호가 틀렸습니다. \n")
        print()


# ------------------------------------------------------------

# 변수
password = '1234'
payment_list = []
selected_menu_list = []

food_dict = {'1': ['김밥', 2500],
             '2': ['참치김밥', 3000],
             '3': ['돈가스김밥', 3500],
             '4': ['고추참치김밥', 3500],
             '5': ['소고기김밥', 4500],
             '7': ['치즈김밥', 3000],
             '8': ['셀러드김밥', 2500],
             '9': ['꼬마김밥', 1200],
             '10': ['충무김밥', 20000],
             '11': ['꽈리김밥', 3500],
             '12': ['진미김밥', 3700],
             '13': ['라면', 4000],
             '14': ['치즈라면', 4500],
             '15': ['된장라면', 4700],
             '16': ['떡라면', 4800],
             '17': ['만두라면', 4500],
             '18': ['떡만두라면', 5000],
             '19': ['카레라면', 4500],
             '20': ['해물라면', 5500],
             '21': ['짜장라면', 4200],
             '22': ['비빔라면', 4200],
             '23': ['돈가스', 8000],
             '24': ['치즈돈가스', 9000],
             '25': ['고치돈', 10000],
             '26': ['등심돈가스', 7500],
             '27': ['안심돈가스', 7500],
             '28': ['피캬츄돈가스', 500],
             '29': ['새우돈가스', 7500],
             '30': ['대왕돈가스', 12000],
             '31': ['치킨돈가스', 6000],
             '32': ['함박스테이크', 9500],
             '33': ['제육덮밥', 7000],
             '34': ['오무라이스', 7000],
             '35': ['하이라이스', 7000],
             '36': ['오징어덮밥', 7500],
             '37': ['짜장덮밥', 6500],
             '38': ['소고기덮밥', 8000],
             '39': ['카레덮밥', 6500],
             '40': ['돌솥비빔밥', 7000],
             '41': ['김치덮밥', 6500],
             '42': ['김치찌개', 6500],
             '43': ['된자찌개', 6500],
             '44': ['순두부찌개', 6500],
             '45': ['내장찌개', 6500],
             '46': ['해물된장찌개', 8500],
             '47': ['부대찌개', 7800],
             '48': ['떡볶이', 3000],
             '49': ['치즈떡볶이', 4500],
             '50': ['라볶이', 5000],
             '51': ['마약떡볶이', 99900],
             '52': ['컵떡볶이', 500],
             '53': ['우동', 3000],
             '54': ['튀김우동', 4500],
             '55': ['김치우동', 4500],
             '56': ['유뷰우동', 4500],
             '57': ['육개장', 6000],
             '58': ['알탕', 7500],
             '59': ['갈비탕', 8000],
             '60': ['황태해장국', 7000],
             '61': ['순대국밥', 5500],
             '62': ['명태국밥', 7000],
             '63': ['공기밥', 1000]
             }

# ------------------------------------------------------------

# 실제 실행구문

while True:
    # interface 출력
    interface()

    # 선택지 1, 2, 3, z 중에 선택지를 받음, 잘못된 선택지를 입력한 경우 continue를 통해 while문 반복
    user_input = get_user_input()

    # 1. 메뉴 선택
    if user_input == '1':
        select_menu(food_dict, selected_menu_list)
        # food_dict : 메뉴판 출력
        # selected_menu_list
        #   - 최초 비어있는 list
        #   - select_menu 함수에서 append를 통해 메뉴가 저장됨

    # 2. 결제
    elif user_input == '2':
        # 주문한 메뉴가 없는 경우 continue
        if selected_menu_list == []:
            print("선택된 메뉴가 없습니다.")
            continue

        show_payment(selected_menu_list, payment_list)

    # 3. 매출 확인
    elif user_input == '3':
        show_profit(password, sum(payment_list))
        # password : 변수로 저장되어 있고 값은 1234
        # sum(payment_list)
        #   - 최초 비어있는 list
        #   - 결제를 한 경우 payment_list에 해당 주문의 최종액이 append됨

    # 4. 프로그램 종료, break를 통해 while문 탈출
    elif user_input.lower() == 'z':
        break

    # 기타. 오 선택지 확인
    else:
        print("잘못입력하셨습니다. 다시 선택지를 골라주세요. \n ")
        continue
        # continue 활용