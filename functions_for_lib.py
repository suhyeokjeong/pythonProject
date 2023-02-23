import cx_Oracle
from datetime import *
# _________________________________ 함수 구현 _________________________________________

# 오라클에서 TEST_TABLE 불러오는 함수 (V)
def return_result_from_Oracle():
    conn = cx_Oracle.connect('lib_db/lib_db@localhost:1521/xe')
    cursor = conn.cursor()
    sql = """select ID, 등록번호, 도서명, 저자, 소장도서관명, 출판사, 출판연도, 청구기호, 대여시작일, 반납예정일자  from  test_table ORDER BY ID """ 

    cursor.execute(sql)
    result = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()   

    return result

# 1. 회원가입 함수 (V)
def sign_in():
    # 1. 아이디 input() 받기
    new_id = input("사용하고 싶은 아이디를 입력하세요. >> ")

    # 2. 데이터베이스 접속
    conn = cx_Oracle.connect('lib_db/lib_db@localhost:1521/xe')
    cursor = conn.cursor()

    sql = '''
    select ID
        from USER_table
        where ID like :1
    '''

    cursor.execute(sql, (new_id,))

    result = cursor.fetchall()


    # 3. 없는 아이디인지 확인
    if len(result) == 0:
        # && 페스워드 해쉬화

        # 비밀번호 확인 절차
        pass_input = input("사용하고싶은 비밀번호를 입력하세요. >>")
        pass_check = input("비밀번호 확인(직전에 친 비밀번호 재입력) >> ")

        # 아이디 비밀번호 DB USER_TABLE에 입력
        if pass_input == pass_check:
            sql2 = '''
            INSERT INTO USER_TABLE (ID, PW)
            VALUES (:1, :2)
            '''            
            cursor.execute(sql2, (new_id, pass_input))

            print(f"{new_id} 아이디 생성완료")
            

        else:
            print("비밀번호가 서로 다릅니다.")
        
    # 있는 아이디인 경우
    else:
        print("이미 존재하는 아이디입니다.")

    
    # DB 접속 해제
    conn.commit()

    cursor.close()
    conn.close()

# 2. 로그인 -> 메인페이지 이동 가능하도록 활성화  (V)
def log_in():
    # 1. 아이디 입력
    id_input = input("ID : ")
    pw_input = input("PW : ")

    # 2. 데이터베이스 접속
    conn = cx_Oracle.connect('lib_db/lib_db@localhost:1521/xe')
    cursor = conn.cursor()

    sql = '''
    select ID, PW
        from USER_TABLE
        where ID like :1 and PW like :2
    '''
    cursor.execute(sql, (id_input, pw_input, ))
    result = cursor.fetchall()

    conn.commit()

    cursor.close()
    conn.close()

    if len(result) == 0:
        print("아이디나 비밀번호가 틀렸습니다.")
        return [False, id_input]
    else:
        print(f"\n{id_input} 로그인 완료\n")
        return [True, id_input]

# 3. 책 찾기 - &&
def search_book(book_to_rent):
    while True:
                # 장바구니 보여줌
        print("-"*10, "장바구니 목록", "-"*10)
        for i, book_data in enumerate(book_to_rent):
            print((i+1), book_data[1:-1])
            user_cart_book_num = i + 1
        print("-"*50)

        print("1. 도서명 검색")
        print("2. 도서 위치 찾기") # 본인 도서관 어디에 소장되어 있는지, 타 도서관에 있는지
        print("0. 뒤로가기")

        num_input = input("\n번호를 입력하세요 >>")

        # 1. 도서명 (예외처리)
            # - 책을 찾아 장바구니에 담기

        if num_input == '1': 
            bookname_input = input("도서명 검색 >> ")
            print()

            count = 1
            abc = []
            true_false_check = True

            # 검색한 도서가 대여가능한지 확인                               
            for row_1 in return_result_from_Oracle():
                if row_1[2] == bookname_input:
                    if row_1[0] == None:
                        print(f"{count}. 대여가능 : {row_1[1:-1]}")
                        abc.append((count, row_1))
                        count += 1
                        true_false_check = False

                    else:
                        print(f"대여중 : {row_1[1:-1]}")
                        true_false_check = False

            # && 수정함            
            # 이름이 같은 책이 있는 경우 선택 가능하게끔 구현 - 예외처리 완료                               
            if abc != []:
                book_number_input = input("장바구니에 담을 책의 번호를 입력하세요. (나가려면 0 입력) >> ")

                if book_number_input == "0":
                    pass
                elif book_number_input.isdigit():
                    if int(book_number_input) <= len(abc): 
                        book_to_rent.append(abc[int(book_number_input) - 1][1])
                        abc = []
                        # && 체크하기
                    else:
                        print("오류 : 잘못입력하셨습니다.")
                else:
                    print("오류 : 잘못입력하셨습니다.")

            # 보유하지 않은 책인 경우    
            if true_false_check:
                print(f"[{bookname_input}]은 보유하지 않는 책입니다")
                
        elif num_input == '2':
            location_data = input("도서명으로 도서 위치 찾기\n    도서명 입력 >>")
            for row in return_result_from_Oracle():
                if row[2] == location_data:
                    print(f"[{location_data}]은/는 [{row[4]}]에 위치하고 있습니다.")
            print()

        # 뒤로가기
        elif num_input.upper() == '0':       
            break

        else:
            print("오류 : 잘못입력하셨습니다.")

# 4. 책 빌리기
def rent_book(book_to_rent, log_in_ID):
    while True:      
        # && 유저의 빌린책 목록 출력
        count = 1
        print("-"*10, f"[{log_in_ID}]의 빌린 책 목록", "-"*10)
        print("최대로 빌릴 수 있는 책의 수 : 5권")
        for row in return_result_from_Oracle():
            # 아이디 입력받아와야함
            if row[0] == log_in_ID:
                print((count), row[1:])
                count += 1
        user_rent_book_num = count - 1
        count = 0
        print("-"*50)
      
        # 장바구니 보여줌
        print("-"*10, "장바구니 목록", "-"*10)
        for i, book_data in enumerate(book_to_rent):
            print((i+1), book_data[1:-1])
            user_cart_book_num = i + 1
        print("-"*50)
        
        print("1. 장바구니 삭제")
        print("2. 장바구니 목록 대여 하기")
        print("0. 뒤로가기")

        num_input = input("\n 번호를 입력하세요")

        #  && 1. 장바구니에서 삭제
        if num_input == '1':
            if len(book_to_rent) == 0:
                print("장바구니가 비었습니다.")
            else:            
                delete_book_num = input("\n 삭제를 원하는 책의 번호를 입력하세요 - 뒤로가려면 0입력")
                if delete_book_num.upper() == '0':
                    pass
                elif delete_book_num.isdigit():
                    if int(delete_book_num) <= len(book_to_rent):
                        book_to_rent.pop((int(delete_book_num)-1))
                        print("삭제 완료되었습니다.")
                    else:
                        print("오류 - 잘못입력하였습니다.")
                else:
                    print("오류 - 잘못입력하였습니다.")

        # 2. 빌린 책 DB에 넣기
        elif num_input == '2': # 
            # # 책 5권 이상 체크
            print(user_rent_book_num, type(user_rent_book_num))
            print(user_cart_book_num, type(user_rent_book_num))
           
            if len(book_to_rent) == 0:
                print("장바구니가 비었습니다.")
            elif (user_rent_book_num + user_cart_book_num) > 5:
                print(user_rent_book_num, user_cart_book_num)
                print("오류 : 한번에 최대한 빌릴 수 있는 책의 수는 5권입니다.")
                print(f"현재 빌린 책의 수 : {user_rent_book_num}")
                print(f"현재 카드 책의 수 : {user_cart_book_num}")
                print("[ 장바구니를 비워주세요 ]")
            else:
                for row in book_to_rent:
                    conn = cx_Oracle.connect('lib_db/lib_db@localhost:1521/xe')
                    cursor = conn.cursor()

                    # # 반납일자 넣으려고 했는데 안됨.
                    # # BOOK_TALBE에 ID값 등록번호와 비교해서 넣어주기

                    # sql2 = '''
                    # UPDATE test_table
                    # set ID = :1, 대여시작일 = :3, 반납예정일자 = :4
                    # where 등록번호 like :2
                    # '''            
                    # # cursor.execute(sql2, (log_in_ID, row[1], datetime.now().date(), (datetime.now() + timedelta(days=5)).date()))
                    # cursor.execute(sql2, (log_in_ID, row[1], '2023-02-23', '2023-02-28'))


                    sql2 = '''
                    UPDATE test_table
                    set ID = :1
                    where 등록번호 like :2
                    '''            
                    cursor.execute(sql2, (log_in_ID, row[1]))

                    conn.commit()

                    cursor.close()
                    conn.close()
                
                book_to_rent.clear()
                
            # 장바구니 비우기    
            

        # 3. 뒤로가기
        elif num_input.upper() == '0':
            break

        # 예외처리
        else:
            print("오류 : 잘못 입력하셨습니다.")

        user_cart_book_num = 0

def return_book(log_in_ID):
    while True:

        print("-"*10, f"[{log_in_ID}] 의 빌린 책 목록", "-"*10)
        count = 1
        for row in return_result_from_Oracle():
            # 아이디 입력받아와야함
            if row[0] == log_in_ID:
                print(count, row[1:])
                count += 1
        count = 0

        print("1. 책 반납하기")
        print("0. 뒤로가기")

        user_input = input("원하는 번호 선택하기 >> ")

        # 1. 책 반납
        if user_input == '1':


            print("-"*50)

            book_number = input("반납을 원하는 책의 [등록번호]를 입력하세요 >> 뒤로가려면 0 입력")

            if book_number.upper() == '0':
                pass
            else:
                # 책 None으로 지우기
                conn = cx_Oracle.connect('lib_db/lib_db@localhost:1521/xe')
                cursor = conn.cursor()

                sql2 = '''
                UPDATE TEST_TABLE
                set ID  = :1
                where 등록번호 like :2
                '''            
                cursor.execute(sql2, (None, book_number))
                
                conn.commit()

                cursor.close()
                conn.close()
                
        # 2. 뒤로가기
        elif user_input.upper() == '0':
            break

        # 예외처리
        else:
            print("오류 : 잘못입력하셨습니다.")



        