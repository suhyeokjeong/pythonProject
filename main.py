
# print("hello world")
# print(1+5)
# print(1*5)
#
# # 나누기 연산자
# print(1/5)
# print(1%5)

# # - 연산자가 피연산자를 받는 개수에 따라 2항 연산자, 3항 연산자
#
# # P49
# professor = "Sunghcul Choi"
# print (professor)
#
# professor = "정수혁"
# print (professor)
#
# # 모두 바꾸기 (CTRL + F 검색 후, CTRL+ALT+SHIFT+J)
# num1 = 7
# num2 = 5
# print(num1+num2)
#
# print("num1+num2")
# num1+num2
#
# # * CTRL + D 바로 위에 구문 복사
# print(type(professor))
# print(type(professor))

# a = 1.5
# b = 3.5
# print(a, b)
# print(type(a))
#
# a = "ABC"
# b = "101010"
# print(a, b)
# print(type(a))
#
# a = True
# b = False
# print(a, b)
# print(type(a))

# # 제곱, 나누기, 나머지
# print (2**3)
# # 몫
# print (7 // 2)
# # 나머지
# print (7 % 2)


# a = 1
# print(a)
# a += 1
# print(a)
# a = a + 1
# print(a)
#
# a -= 1
# print(a)
# a = a - 1

# * 타입 확인후 입력

# print("input anything a = ", end ='')
# input_1 = input()
# if input_1.isdigit():
#     input_1 = int(input_1)
# else:
#     try:
#         input_1 = float(input_1)
#     except ValueError:
#         pass
#
# print(input_1, type(input_1))


#
# print("input anything a = ", end ='')
# input_1 = input()
# print("input anything b = ", end ='')
# input_2 = input()
#
# print("더하기", int(input_1) + int(input_2))
# print("빼기", int(input_1) - int(input_2))
# print("곱하기", int(input_1) * int(input_2))
# print("나누기", int(input_1) / int(input_2))
# print("몫", int(input_1) // int(input_2))
# print("나머지", int(input_1) % int(input_2))
# print("제곱", int(input_1) ** int(input_2))
#

# #연습문제 p.68
# 1. 1
# 2. 3
# 3. 4
# 4. 5
# 5. 2
# 6. 1
# 7. 5 (?)
# 8. 4
# 9. 1
# 10. 2
# 11. 1
# 12. 2
# 13. 2
# 14. 1
# 15. 5
# 16. 5
# 17. 동적 타이핑으로 인해
#   a = 1 로 지정해주면 컴퓨터가 알아서 숫자로 인식한다
#   정적인 경우 int a = 1로 입력해줘야한다.
# 18. 파이썬에서 0.1 + 0.2의 값은 얼마일까요?
#   0.3이 나올 것 같지만 실제로는 0.30000000000000004가 나옵니다.
#   파이썬은 실수를 부동소수점 방식으로 표현하는데 부동소수점은 실수를 정확히 표현할 수 없는 문제가 있습니다.

#
# print("본 프로그램은 섭씨온도를 화씨온도로 변환하는 프로그램입니다")
# print("변환하고 싶은 화씨온도르 입력하세요")
# print("입력 => ", end ='')
# celcius = float(input())
# f_celcius = (celcius * 1.8) + 32
#
# print("섭씨온도: ", round(celcius, 3))
# print("화씨온도: ", round(f_celcius, 3))

# colors = ['red', 'blue', 'green']
#
# print(colors[0])
# print(colors[1])
# print(colors[2])
#
# cities = ['서울', '부산', '인천', '대구', '광주', '울산', '수원']
# print (cities[0:5])
# print (cities[5:])
# print (cities[-4:])
#
# color1 = ['red', 'blue', 'green']
# color2 = ['orange', 'black', 'white']
# print(color1 + color2)

# print(len(color1))
# total_color = color1 + color2
# print(total_color)
#
# print('blue' in color2, type('blue' in color2))
#
# # list에 하나만 삽입
# color1.append('white')
# print(color1)

# # list에 여러개 삽입
# color1.extend(['black', 'purple'])
# print(color1)
#
# # 지정해서 넣기
# color1.insert(0, 'purple')
# print(color1)
#
# # index 지우기
# color1.remove(color1[0])
# print(color1)
#
# color1.remove('purple')
# print(color1)

# 인덱스 재할당
# print(color1)
# color1[0] = 'orange'
# print(color1)
#
# del color1[0]
# print(color1)
#
#

# # 패킹과 언패킹
# t = [1, 2, 3]
# a, b, c = t
# print(t, a, b, c)
#
# kor_score = [49, 79, 20, 100, 80]
# math_score = [43, 59, 85, 30, 90]
# eng_score = [49, 79, 48, 60, 100]
#
# midterm_score = [kor_score, math_score, eng_score]
# print(midterm_score)
#
# kor_avg = sum(kor_score)/ len(kor_score)
# math_avg = sum(math_score)/ len(math_score)
# eng_avg = sum(eng_score)/ len(eng_score)
# print(f"한국어 평균은 {kor_avg}입니다")
# print("수학 평균은 {}입니다".format(round(math_avg, 0)))
# print("영어 평균은 %d입니다" % eng_avg)
#
# print("한국어 총합은 %d입니다" % sum(kor_score)) #십진수
# print("수학 총합은 %s입니다" % sum(math_score)) #string 형태
# print("영어 평균은 %0.2f입니다" % sum(eng_score)) #float 형태

# # 공백지정
# print("%10s" % "hi") # 공백주기
# print("%-10sjane" % "0123456789") # 공백주기

#
# a = ['정다진', '010-3424-2264', []]
# b = ['이준영', '010-5955-8851', []]
# c = ['황윤정', '010-4163-1300', []]
# d = ['이수민', '010-2679-2084', []]
# e = ['최수연', '010-2827-0820', []]
#
# student = [a, b, c, d, e]
# subject = ['국어', '영어', '수학', '파이썬']
#
# # a학생
# print("%s 학생의 %s 성적을 입력하세요" % (student[0][0], subject[0]), end = " => ")
# student[0][2].append(input())
# print("%s 학생의 %s 성적을 입력하세요" % (student[0][0], subject[1]), end = " => ")
# student[0][2].append(input())
# print("%s 학생의 %s 성적을 입력하세요" % (student[0][0], subject[2]), end = " => ")
# student[0][2].append(input())
#
# python_score = student[0][1][-2:]
# if student[0][1][-2:] == '00':
#     python_score = '100'
# student[0][2].append(python_score) # a 학생 파이썬 점수 입력
#
# student_avg = (int(student[0][2][0]) + int(student[0][2][1]) + int(student[0][2][2]) + int(student[0][2][3])) / len(student[0][2])
# student[0][2].append(student_avg)
#
# # b학생
# print("%s 학생의 %s 성적을 입력하세요" % (student[1][0], subject[0]), end = " => ")
# student[1][2].append(input())
# print("%s 학생의 %s 성적을 입력하세요" % (student[1][0], subject[1]), end = " => ")
# student[1][2].append(input())
# print("%s 학생의 %s 성적을 입력하세요" % (student[1][0], subject[2]), end = " => ")
# student[1][2].append(input())
#
# python_score = student[1][1][-2:]
# if student[1][1][-2:] == '00':
#     python_score = '100'
# student[1][2].append(python_score) # a 학생 파이썬 점수 입력
#
# student_avg = (int(student[1][2][0]) + int(student[1][2][1]) + int(student[1][2][2]) + int(student[1][2][3])) / len(student[1][2])
# student[1][2].append(student_avg)
#
#
#
# # c학생
# print("%s 학생의 %s 성적을 입력하세요" % (student[2][0], subject[0]), end = " => ")
# student[2][2].append(input())
# print("%s 학생의 %s 성적을 입력하세요" % (student[2][0], subject[1]), end = " => ")
# student[2][2].append(input())
# print("%s 학생의 %s 성적을 입력하세요" % (student[2][0], subject[2]), end = " => ")
# student[2][2].append(input())
#
# python_score = student[2][1][-2:]
# if student[2][1][-2:] == '00':
#     python_score = '100'
# student[2][2].append(python_score) # a 학생 파이썬 점수 입력
#
# student_avg = (int(student[2][2][0]) + int(student[2][2][1]) + int(student[2][2][2]) + int(student[2][2][3])) / len(student[2][2])
# student[2][2].append(student_avg)
#
# # d학생
# print("%s 학생의 %s 성적을 입력하세요" % (student[3][0], subject[0]), end = " => ")
# student[3][2].append(input())
# print("%s 학생의 %s 성적을 입력하세요" % (student[3][0], subject[1]), end = " => ")
# student[3][2].append(input())
# print("%s 학생의 %s 성적을 입력하세요" % (student[3][0], subject[2]), end = " => ")
# student[3][2].append(input())
#
# python_score = student[3][1][-2:]
# if student[3][1][-2:] == '00':
#     python_score = '100'
# student[3][2].append(python_score) # a 학생 파이썬 점수 입력
#
#
# student_avg = (int(student[3][2][0]) + int(student[3][2][1]) + int(student[3][2][2]) + int(student[3][2][3])) / len(student[3][2])
# student[3][2].append(student_avg)
#
# # e학생
# print("%s 학생의 %s 성적을 입력하세요" % (student[4][0], subject[0]), end = " => ")
# student[4][2].append(input())
# print("%s 학생의 %s 성적을 입력하세요" % (student[4][0], subject[1]), end = " => ")
# student[4][2].append(input())
# print("%s 학생의 %s 성적을 입력하세요" % (student[4][0], subject[2]), end = " => ")
# student[4][2].append(input())
#
# python_score = student[4][1][-2:]
# if student[4][1][-2:] == '00':
#     python_score = '100'
# student[4][2].append(python_score) # a 학생 파이썬 점수 입력
#
#
# student_avg = (int(student[4][2][0]) + int(student[4][2][1]) + int(student[4][2][2]) + int(student[4][2][3])) / len(student[4][2])
# student[4][2].append(student_avg)
#
# print("%17s" %"성", "%3s" %"적","%3s" %"표")
# print("_"*45)
# print("%10s" %"국어", "%5s" %"영어", "%5s" %"수학", "%5s" %"파이썬", "%5s" %"평균")
# print("%s" % student[0][0], "%5s" % student[0][2][0], "%5s" % student[0][2][1], "%6s" % student[0][2][2],  "%7s" % student[0][2][3], "%9s" % student[0][2][4])
# print("%s" % student[1][0], "%5s" % student[1][2][0], "%5s" % student[1][2][1], "%6s" % student[1][2][2],  "%7s" % student[1][2][3], "%9s" % student[1][2][4])
# print("%s" % student[2][0], "%5s" % student[2][2][0], "%5s" % student[2][2][1], "%6s" % student[2][2][2],  "%7s" % student[2][2][3], "%9s" % student[2][2][4])
# print("%s" % student[3][0], "%5s" % student[3][2][0], "%5s" % student[3][2][1], "%6s" % student[3][2][2],  "%7s" % student[3][2][3], "%9s" % student[3][2][4])
# print("%s" % student[4][0], "%5s" % student[4][2][0], "%5s" % student[4][2][1], "%6s" % student[4][2][2],  "%7s" % student[4][2][3], "%9s" % student[4][2][4])
#

# # 학생 이름, 번호, 성적
# student_1 = ['정다진', '010-0000-2264', []]
# student_2 = ['이준영', '010-0000-8851', []]
# student_3 = ['황윤정', '010-0000-1300', []]
# student_4 = ['이수민', '010-0000-2084', []]
# student_5 = ['최수연', '010-0000-0820', []]
#
# # 학생 list, 과목 list 생성
# student = [student_1, student_2, student_3, student_4, student_5]
# subject = ['국어', '영어', '수학', '파이썬']
#
# # 1. for문을 통해 학생별 성적 입력
# for student_num in range(len(student)):
#     for subject_name in range(len(subject) - 1):  # 파이썬 성적은 자동으로 받아옴으로 -1
#         print("[%s] 학생의 [%s] 성적을 입력하세요" % (student[student_num][0], subject[subject_name]), end=" => ")
#         student[student_num][2].append(input())
#
#     # 전화번호에서 파이썬 점수 추출
#     python_score = student[student_num][1][-2:]
#
#     # 전화번호 00 확인 후 100점으로 변경
#     if student[student_num][1][-2:] == '00':
#         python_score = '100'
#     student[student_num][2].append(python_score)  # 학생 파이썬 점수 입력
#     print("-" * 45)
#     print("파이썬 성적은 전화번호 마지막 두자리로 자동 입력됨")
#
#     # 학생 과목별 평균 * map 활용
#     student_avg = sum(map(float, student[student_num][2])) / len(student[student_num][2])
#     student[student_num][2].append(student_avg)
#
#     print("-" * 45)
#
# # 2. 과목별 평균 subject_avg에 삽입
# subject_avg = []
#
# for subject_num in range(len(subject)):  # 2중 포문에서 +=을 통해 과목별 평균 계산
#     sum_score_by_subject = 0
#
#     for student_num in range(len(student)):
#         sum_score_by_subject += float(student[student_num][2][subject_num])
#
#     subject_avg.append(sum_score_by_subject / len(student))
#
# # 3. 출력구문
# print("")
#
# print("%17s" % "성", "%3s" % "적", "%3s" % "표")
# print("-" * 45)
# print("%10s" % "국어", "%5s" % "영어", "%5s" % "수학", "%6s" % "파이썬", "%4s" % "평균")
# print("%s" % student[0][0], "%4s" % student[0][2][0], "%7s" % student[0][2][1], "%7s" % student[0][2][2],
#       "%8s" % student[0][2][3], "%8.2f" % student[0][2][4])
# print("%s" % student[1][0], "%4s" % student[1][2][0], "%7s" % student[1][2][1], "%7s" % student[1][2][2],
#       "%8s" % student[1][2][3], "%8.2f" % student[1][2][4])
# print("%s" % student[2][0], "%4s" % student[2][2][0], "%7s" % student[2][2][1], "%7s" % student[2][2][2],
#       "%8s" % student[2][2][3], "%8.2f" % student[2][2][4])
# print("%s" % student[3][0], "%4s" % student[3][2][0], "%7s" % student[3][2][1], "%7s" % student[3][2][2],
#       "%8s" % student[3][2][3], "%8.2f" % student[3][2][4])
# print("%s" % student[4][0], "%4s" % student[4][2][0], "%7s" % student[4][2][1], "%7s" % student[4][2][2],
#       "%8s" % student[4][2][3], "%8.2f" % student[4][2][4])
# print(" 평균 ", "%5.2f" % subject_avg[0], "%7.2f" % subject_avg[1], "%7.2f" % subject_avg[2], "%8.2f" % subject_avg[3])
# print("-" * 45)  `