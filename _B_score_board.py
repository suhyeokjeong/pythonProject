# 학생 이름, 번호, 성적
student_1 = ['정다진', '010-0000-2264', []]
student_2 = ['이준영', '010-0000-8851', []]
student_3 = ['황윤정', '010-0000-1300', []]
student_4 = ['이수민', '010-0000-2084', []]
student_5 = ['최수연', '010-0000-0820', []]

# 학생 list, 과목 list 생성
student = [student_1, student_2, student_3, student_4, student_5]
subject = ['국어', '영어', '수학', '파이썬']

# 1. for문을 통해 학생별 성적 입력
for student_num in range(len(student)):
    for subject_name in range(len(subject) - 1):  # 파이썬 성적은 자동으로 받아옴으로 -1
        print("[%s] 학생의 [%s] 성적을 입력하세요" % (student[student_num][0], subject[subject_name]), end=" => ")
        student[student_num][2].append(input())

    # 전화번호에서 파이썬 점수 추출
    python_score = student[student_num][1][-2:]

    # 전화번호 00 확인 후 100점으로 변경
    if student[student_num][1][-2:] == '00':
        python_score = '100'
    student[student_num][2].append(python_score)  # 학생 파이썬 점수 입력
    print("-" * 45)
    print("파이썬 성적은 전화번호 마지막 두자리로 자동 입력됨")

    # 학생 과목별 평균 * map 활용
    student_avg = sum(map(float, student[student_num][2])) / len(student[student_num][2])
    student[student_num][2].append(student_avg)

    print("-" * 45)

# 2. 과목별 평균 subject_avg에 삽입
subject_avg = []

for subject_num in range(len(subject)):  # 2중 포문에서 +=을 통해 과목별 평균 계산
    sum_score_by_subject = 0

    for student_num in range(len(student)):
        sum_score_by_subject += float(student[student_num][2][subject_num])

    subject_avg.append(sum_score_by_subject / len(student))

# 3. 출력구문
print("")

print("%17s" % "성", "%3s" % "적", "%3s" % "표")
print("-" * 45)
print("%10s" % "국어", "%5s" % "영어", "%5s" % "수학", "%6s" % "파이썬", "%4s" % "평균")
print("%s" % student[0][0], "%4s" % student[0][2][0], "%7s" % student[0][2][1], "%7s" % student[0][2][2],
      "%8s" % student[0][2][3], "%8.2f" % student[0][2][4])
print("%s" % student[1][0], "%4s" % student[1][2][0], "%7s" % student[1][2][1], "%7s" % student[1][2][2],
      "%8s" % student[1][2][3], "%8.2f" % student[1][2][4])
print("%s" % student[2][0], "%4s" % student[2][2][0], "%7s" % student[2][2][1], "%7s" % student[2][2][2],
      "%8s" % student[2][2][3], "%8.2f" % student[2][2][4])
print("%s" % student[3][0], "%4s" % student[3][2][0], "%7s" % student[3][2][1], "%7s" % student[3][2][2],
      "%8s" % student[3][2][3], "%8.2f" % student[3][2][4])
print("%s" % student[4][0], "%4s" % student[4][2][0], "%7s" % student[4][2][1], "%7s" % student[4][2][2],
      "%8s" % student[4][2][3], "%8.2f" % student[4][2][4])
print(" 평균 ", "%5.2f" % subject_avg[0], "%7.2f" % subject_avg[1], "%7.2f" % subject_avg[2], "%8.2f" % subject_avg[3])
print("-" * 45)