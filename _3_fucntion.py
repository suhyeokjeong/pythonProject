from math import *

# # 1. 사각형 넓이
# def calculate_rectangle_area(x, y):
#     result = x * y
#     print(result)
#     return result
#
# calculate_rectangle_area(3, 5)

# # ---------------------------------------------------------------------

# # 2. 직각삼각형 빗변
# def side(x, y):
#     result = sqrt(x**2 + y**2)
#     print(result)
#     return result
#
# side(3,4)

# # ---------------------------------------------------------------------

# # 3. 리스트, 총합, 평균
# random_list = [6, 2, 3]
#
# def sum_calculator_1(list):
#     result = 0
#     # for num in range(len(list)):
#     #     result += list[num]
#     for num in list:
#         if type(num) is not int: continue
#         result += num
#
#     return result
# random_list = [6, 2, 3]#
# print(sum_calculator_1(random_list))
#
#
# def sum_calculator_2(list):
#     result = sum(list)
#     return result

# random_list = [6, 2, 3]
# print(sum_calculator_2(random_list))
# #
#
# def avg_calculator_1_with_round(list, round_num):
#     sum_result = sum(list)
#     average = sum_result / len(list)
#     return round(average, round_num)
#
# random_list = [6, 2, 3]
# print(avg_calculator_1_with_round(random_list, 3))
#
# def avg_calculator_2_with_round(list, round_num):
#     sum_result = 0
#     for num in range(len(list)):
#         sum_result += list[num]
#     average = sum_result / len(list)
#     return round(average, round_num)
#
# random_list = [6, 2, 3]
# print(avg_calculator_2_with_round(random_list, 3))

# # ---------------------------------------------------------------------

# # 4. 펙토리얼 계산, 재귀함수, for문, 일반 함수
# factorial
# def factorial(number):
#     result = 1
#     for i in range(1, number + 1):
#         result *= i
#     return result
#
# print(factorial(3))
#

# # 제귀함수, return을 if else문 안에 넣을 수 있다.
# def factorial(number):
#     if number == 1:
#         return 1
#     else:
#         return number * factorial(number - 1)
#
# number_input = int(input("숫자를 입력해주세요.>> "))
# print(factorial(number_input))

# number = 5
# factorial = 1
#
# for i in range(1, number+1):
#     factorial *= i
#
# print(factorial)

# # ---------------------------------------------------------------------

# # 5. default 인수, asterisk * 이용 (변수가 몇개인지 불확실 할 때), kwargs ** (dictionary 이용)
# def default_test(yourname, yourTeam = "KEPCO Digital Boot Camp B반"):
#     print(f"이름은 : {yourname}, 소속은 {yourTeam}입니다.")
#
# default_test("정수혁", "전남대학교")
# default_test("정수혁")
# default_test(yourTeam = "금옥중학교", yourname = "김철수")
#
# def asterisk_1(a, b, *args):
#     return a + b + sum(args)
#
# print(asterisk_1(1, 2, 3, 4, 5))
#
# def asterisk_2(a, b, *args):
#     print(args)
#
# print(asterisk_2(1, 2, 3, 4, 5))
#
# def asterisk_3(a, b, *args):
#     a, b, *c = args
#     return a, b, c
# print(asterisk_3(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
#
# ## **kwargs
# def kwargs_test(**kwargs):
#     print(kwargs)
#     print("First value is {first}".format(**kwargs))
#     print("Second value is {second}".format(**kwargs))
#     print("Third value is {third}".format(**kwargs))
#
# kwargs_test(first = 3, second = 4, third = 5)
#

# # ---------------------------------------------------------------------


# # 성적표 만들기 with function
# # 학생 이름, 번호, 성적
# student_1 = ['정다진', '010-0000-2264', [10, 20, 30, 40]]
# student_2 = ['이준영', '010-0000-8851', [20, 30, 40, 50]]
# student_3 = ['황윤정', '010-0000-1300', [30, 40, 50, 60]]
# student_4 = ['이수민', '010-0000-2084', [60, 70, 80, 90]]
# student_5 = ['최수연', '010-0000-0820', [70, 80, 90, 100]]
#
#
# # 학생 list, 과목 list 생성
# student = [student_1, student_2, student_3, student_4, student_5]
# subject = ['국어', '영어', '수학', '파이썬']
#
# def avg_by_student (student_list, subject_list):
#     for num in range(len(subject_list)):
#         total_grade = sum(map(int, student_list[num][2]))
#         average = total_grade / len(subject_list)
#         student_list[num].append(average)
#
# def make_a_list_of_avg_by_subject (student_list, subject_list):
#     subject_avg = []
#     for i in range(len(subject_list)):
#         total_grade = 0
#
#         for j in range(len(student_list)):
#             total_grade += student_list[j][i]
#
#         avg_grade = total_grade / len(student_list)
#         subject_avg.append(avg_grade)
#
#     return subject_avg
#
# print(student)
# avg_by_student(student, subject)
# print(student)

# # -----------------------------------------------------
# # tuple, array 차이, dictionary

# # # 6. 근 구하기
# def return_root(a, b, c):
#     result = []
#     root_detector = b**2  - 4 * a * c
#     if root_detector < 0:
#         return "허수의 근이 있습니다."
#     else:
#         result.append((-b + sqrt(root_detector))/(2 * a))
#         result.append((-b - sqrt(root_detector))/(2 * a))
#         return result
#
# print("[a] x^2 + [b] x + [c]의 근을 계산합니다. a, b, c를 입력해주세요.")
# a = int(input("[a] >> "))
# b = int(input("[b] >> "))
# c = int(input("[c] >> "))
#
# print(return_root(a, b, c))
