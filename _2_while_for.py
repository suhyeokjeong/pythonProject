# # 기본 문법
# while True:
#     if True: continue # while문에서 예외하고 진행
#     if True: break # While문 탈출

#
# # 1. 구구단 계산
# print("구구단 몇단을 계산하고 싶어?")
# user_input = input()
# int_input = int(user_input)
#
# for i in range(1, 10):
#     print(int_input, 'x', i, '=', int_input * i)


# # # 2. ATM UI
# # ** """ """ 으로 문자열 space있게 사용 가능
# promt = """
# 1. 이체
# 2. 통장잔고
# 3. 입금
# 4. 종료
#
# Enter number:
# """
# num = 0
# while num != 4:
#     print(promt)
#     num = int(input())

# # range 사용
# # range(1, 10), range (10), range(len(리스트)), for num in num_list

# for i in range(1, 10):
#     print(i)

# # list같은 순서가 있는 자료구조에서 요소를 꺼내면서 반복
# num_list = [1,2,3,4,5,6,7,8,9]
#
# for i in range(len(num_list)):
#     print(num_list[i], end = ' ')
#
# print('\n')
#
# for num in num_list:
#     print(num, end = ' ')
#
# print('\n')
#

# # 평균 계산
# num_list = [1,2,3,4,5,6,7,8,9]
# sum = 0
# i = 1
# for num in num_list:
#     sum += num
#     average = sum / i
#     print(i, ' : ', sum, average)
#     i += 1
#
# print(sum, sum/len(num_list))


# # ** for문에도 for문이 종료되고 난 후 else를 활용할 수 있다.
# for i in range(10):
#     print(i)
# else:
#     print("END")
# break를 만나면 else는 출력되지 않는다.

# student_list = ['수혁', '다진', '준영', '수연', '진영']
#
# print("학생이름을 입력하세요")
# student_input = input()
#
# for student in student_list:
#     if student == student_input:
#         print(f"{student_input}을 찾았습니다.")
#         break
# else:
#     print(f"{student_input}는 없습니다")

# sum = 0
#
# for i in range(101):
#     if i%2 == 0: continue
#     sum += i
#
# print(sum)

# # 3. 1~100사이 숫자 추측
# from random import *
#
# random_num = randint(1, 100)
# print(random_num)
#
# life = int(input("숫자 맞추기 게임입니다. 몇번만에 숫자를 맞출건지 숫자를 적어주세요."))
# count = 0
#
# # user_input = int(input("숫자를 입력하세요"))
# # while user_input is not random_num:
# #     if user_input > random_num:
# #         print("숫자가 너무 큽니다.", end = ' ')
# #     else:
# #         print(f"숫자가 너무 작습니다.", end = ' ')
# #
# #     print(f"{life - count}번의 기회가 남았습니다.")
# #     user_input = int(input("숫자를 입력하세요"))
# #     count += 1
# # else:
# #     if count == life:
# #         print(f"{count}번의 기회를 모두 소진하였습니다.")
# #     else:
# #         print(f"정답입니다. {count}번만에 정답을 맞추셨습니다.")
#
# while True:
#     user_input = int(input(f"{life - count}: 숫자를 입력하세요."))
#     if count == life - 1:
#         print(f"{life}번의 기회를 모두 소진하였습니다. 정답은 {random_num}입니다.")
#         break
#
#     count += 1
#
#     if random_num > user_input:
#         print(f"땡! {life - count}번의 기회가 남았습니다. {user_input}보다 큰 숫자입니다.")
#     elif random_num < user_input:
#         print(f"땡! {life - count}번의 기회가 남았습니다. {user_input}보다 작은 숫자입니다.")
#     else:
#         print(f"정답입니다. {user_input}이 맞습니다. {count}번만에 정답을 맞췃습니다.")
#         break

# # 이중 리스트, 이중 포문 호출
# student_list = [['연화', '남호', '민지', '상훈', '소연'],
#                 ['수민', '수성', '영호', '재현', '준영'],
#                 ['창훈', '태진', '현수', '세원', '진영']]
#
# count = 1
# for list_num in student_list:
#     for student_name in list_num:
#         print(f"{count}. {student_name}", end = ' | ')
#         count += 1

# # 4. 2중 for문을 통해 평균 계산 ?
# kor_score = [49, 79, 20, 100, 80]
# math_score = [43, 59, 85, 30, 90]
# eng_score = [49, 79, 48, 60, 100]
#
# score_list = [kor_score, math_score, eng_score]
#
# subject_avg = []
#
# # 과목 별 평균
# for subject in score_list:
#     sum = 0
#
#     for score in subject:
#         sum += score
#     subject_avg.append(sum/len(subject))
#
# print(f"국어 평균 : {subject_avg[0]}, 수학 평균 : {subject_avg[1]},  영어 평균 : {subject_avg[2]}")
#
# # 학생별 평균
# for num_2 in range(len(score_list[0])): # [ ]여기다가 숫자를 넣어야만 함
#     sum = 0
#     for num_1 in range(len(score_list)):
#         sum += score_list[num_1][num_2]
#
#     print(f"{num_2 + 1}. {round(sum/len(score_list), 1)}", end = ' | ')
# #
# subject_avg = [0,0,0,0,0]

# # ???
# i = 0
# for subject in score_list:
#     for score in subject:
#         subject_avg[i] += score
#         i += 1
#     i = 0
#
# for i in range(len(subject_avg)):
#     print(round(subject_avg[i]/len(score_list), 1))

# # 6. 구구단 출력
# for i in range(1, 10):
#     for j in range(1, 10):
#         print("%d x %d = %2d" % (i, j, i*j), end = ' | ')
#     print("")

# # -------------------------------------------------------------------
# # 과제 별찍기
# #
# # 1
# #
# # 1 - 기본
# # print("O" * 0, "*" * 1)
# # print("O" * 1, "*" * 1)
# # print("O" * 2, "*" * 1)
# # print("O" * 3, "*" * 1)
# # print("O" * 4, "*" * 1)
# #
# #
# # 1 - while문
# i = 0
# line = 5
# while i != line:
#     print("O" * i, end = '')
#     print("*")
#
#     i += 1
#
# # 1 - 이중 포문
# line = 5
# for i in range(line):
#     for j in range(0, i):
#         print("O", end = '')
#     print("*")
#
#
# 2
#
# # 기본 틀
# print("*" * 5)
# print("*" * 4)
# print("*" * 3)
# print("*" * 2)
# print("*" * 1)
#
# # while문
# i = 0
# line = 5
# while i != line:
#     print("*"* (line-i))
#     i += 1
#
# print("-"*15)
#
# # 2중 for문
#
# line = 5
# for i in range(line):
#     for j in range(line - i - 1, 0, -1):
#         print("*", end = '')
#     print("*")
#
#
# 3
# #
# print(" " * 4, "*" * 1)
# print(" " * 3, "*" * 3)
# print(" " * 2, "*" * 5)
# print(" " * 1, "*" * 7)
# print(" " * 0, "*" * 9)
# #
# # while문
# i = 0
# line = 5
# while i != line:
#     i += 1
#     print(" "* (line-i), "*" * (2 * i - 1))
#
# # 2중 for문
#
# line = 5
# for i in range(line):
#     for j in range(line - i - 1, 0, -1):
#         print(" ", end = '')
#     for j in range(0, i * 2):
#         if j % 2 == 0:
#             continue
#         print("*" * 2, end = '')
#     print("*")
#
#
#
# # 5
#
# print(" " * 0, "*" * 9)
# print(" " * 1, "*" * 7)
# print(" " * 2, "*" * 5)
# print(" " * 3, "*" * 3)
# print(" " * 4, "*" * 1)
#
# i = 0
# line = 5
# while i != line:
#     print(" " * i, end = ' ')
#     print("*" * (2 * (line - i) - 1), end = ' ')
#     print()
#     i += 1
#
#
# line = 5
# for i in range(line):
#     for j in range(0, i):
#         print(" ", end = '')
#     for j in range(line - i - 1, 0, -1):
#         print("*" * 2, end = '')
#     print("*")
#
#
#
#
#
# # 5
# i = 5
# while i != 0:
#     print(" "* (5-i), "*" * (2 * i - 1))
#     i -= 1
#
# print("-"*15)
#
#
#
# # 6
# i = 0
# while i != 5:
#     print(" "* (4-i), "*" * (2 * i + 1))
#     i += 1
#
# i = 4
# while i != 0:
#     print(" "* (5-i), "*" * (2 * i - 1))
#     i -= 1
#
# line = 5
# for i in range(line - 1):
#     for j in range(line - i - 1, 0, -1):
#         print(" ", end = '')
#     for j in range(0, i * 2):
#         if j % 2 == 0:
#             continue
#         print("*" * 2, end = '')
#     print("*")
#
# for i in range(line):
#     for j in range(0, i):
#         print(" ", end = '')
#     for j in range(line - i - 1, 0, -1):
#         print("*" * 2, end = '')
#     print("*")
#
# print("-"*15)
#
# #
# # # 7
# # i = 7
# # while i != 0:
# #     print(" "* (7-i), "*" * (2 * i - 1))
# #     i -= 1
# #
# # while i != 7:
# #     print(" "* (6-i), "*" * (2 * i + 1))
# #     i += 1
# #
# # print("-"*15)
# #
# line = 7
# #
# for i in range(line):
#     for j in range(0, i):
#         print(" ", end = '')
#     for j in range(line - i - 1, 0, -1):
#         print("*" * 2, end = '')
#     print("*")
#
# for i in range(line):
#     for j in range(line - i - 1, 0, -1):
#         print(" ", end = '')
#     for j in range(0, i * 2):
#         if j % 2 == 0:
#             continue
#         print("*" * 2, end = '')
#     print("*")
# #
# print("-"*15)