# # 기본 문법
# if True:
#     pass
# elif:
#     pass
# else:
#     pass


# 클럽 입밴
# print("Tell me your age")
# age = input()
#
# if 19 < int(age) < 30:
#     print("Welcome to the club")
# else:
#     print("Sorry you are not accepted")
#
# # 1. 홀수 짝수 계산
# print("Tell me any number")
# num = input()
#
# if int(num) % 2 == 0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")
#
# # 2. 두수를 입력받아 큰 수 찾기
# print("첫번째 숫자")
# num_1 = int(input())
# print("두번째 숫자")
# num_2 = int(input())
#
# if num_1 > num_2:
#     print("더 큰 수는 %d입니다" % num_1)
# elif num_1 == num_2:
#     print("두 수가 같습니다")
# else:
#     print("더 큰 수는 %d입니다" % num_2)
#
# # 3. 양수 음수 판별
# print("첫번째 숫자")
# num_1 = int(input())
# print("두번째 숫자")
# num_2 = int(input())
#
# if num_1 >= 0:
#     print("%d는 양수입니다. " % num_1, end = '')
# else:
#     print("%d는 음수입니다. " % num_1, end = '')
#
# if num_2 >= 0:
#     print("%d는 양수입니다." % num_2, end = '')
# else:
#     print("%d는 음수입니다." % num_2, end = '')


# # 4. 세수를 입력 받아 큰 수 찾기 Version 1
#
# print("첫번째 숫자")
# num_1 = int(input())
# print("두번째 숫자")
# num_2 = int(input())
# print("세번째 숫자")
# num_3 = int(input())
#
# # num_list = [num_1, num_2, num_3]
# # print("가장 큰 숫자는 %d입니다." % max(num_list))
# print("가장 큰 숫자는 %d입니다." % max(num_1, num_2, num_3))


# # 4. 세수를 입력 받아 큰 수 찾기 version 2
# print("첫번째 숫자")
# num_1 = int(input())
# print("두번째 숫자")
# num_2 = int(input())
# print("세번째 숫자")
# num_3 = int(input())
#
# higher_num = 0
#
# if num_1 > num_2:
#     higher_num = num_1
# else:
#     higher_num = num_2
#
# if higher_num > num_3:
#     pass
# else:
#     higher_num = num_3
#
# print("가장 높은 수는 %d입니다" % higher_num)


# # 5. 목욕탕 요금 계산 #1
# # 목욕탕을 7세이하는 요금 5000
# # 7세이상은 성인 요금 7000
# # 60세이상은 어르신 요금 6000
#
# user_input = input("나이를 만으로 입력해주세요.")
# age = int(user_input)
#
# if age < 7:
#     print("어린이 요금 : 5000원 입니다.")
#     # payment = 5000
#
# elif age >= 60 :
#     print("어르신 요금 : 6000원 입니다.")
#     # payment = 6000
#
# else:
#     print("성인 요금 : 7000원 입니다.")
# #     payment = 7000
# #
# # print(f"요금은 {payment} 입니다.")

# # 6. 영어점수 출력
# user_input = input("내 영어점수 입력")
# eng_score = int(user_input)
# result = ""
#
# if eng_score <= 60:
#     result = "혼 좀 나야겠군"
# elif eng_score <= 70:
#     result = "아무일도 없었다."
# elif eng_score <= 80:
#     result = "만화책을 얻었다!"
# elif eng_score <= 90:
#     result = "용돈 10만원을 얻었다!"
# else:
#     result = "노트북을 얻었다!"
#
# print(result)

# # 7. 학생 구분
# user_input = int(input("태어난 연도를 입력하세요"))
#
# age = (2023 - user_input)
# print(age)
# if age < 8:
#     print("학생이 아닙니다.")
# elif age <14:
#     print("초등학생입니다.")
# elif age <17:
#     print("중학생입니다.")
# elif age <20:
#     print("고등학생입니다.")
# elif age <26:
#     print("대학생입니다.")
# else:
#     print("학생이 아닙니다")


# # 8. 주민번호 7자리를 통해 나이, 성별 추출
# id_num = input("주민번호를 7자리를 입력하세요")
# year = 0
# gender = "default"
#
# if id_num[6] == '3' or id_num == '4':
#     year = '20' + id_num[0:2]
#
# else:
#     year = '19' + id_num[0:2]
#
# age = 2023 - int(year)
#
# if int(id_num[6])%2 == 1:
#     gender = "남성"
# else:
#     gender = '여성'
#
# # if id_num[6] == '1' or id_num[6] == '3':
# #     gender = "남성"
# # else:
# #     gender = "여성"
#
# birth_month = int(id_num[2:4])
# birth_day = int(id_num[4:6])
#
# print("나이는 [%d]이고, 성별은 [%s]입니다. 생일은 %d월 %d일 입니다." % (age, gender, birth_month, birth_day))


