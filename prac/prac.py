#19
grades = [[85, 90, 78], [92, 76, 88], [70, 95, 83]]

for i in range(0, len(grades)):
    for j in range(0, len(grades[i])):
        print(f"{grades[i][j]}", end=", ")
    print()

sum_grade_1, sum_grade_2, sum_grade_3 = 0, 0, 0
for i in range(0, len(grades)):
    sum_grade = 0
    for j in range(0, len(grades[i])):
        sum_grade += grades[i][j]
        if i == 0:
            sum_grade_1 += grades[i][j]
        elif i == 1:
            sum_grade_2 += grades[i][j]
        else:
            sum_grade_3 += grades[i][j]
    print(f"{i+1}번째 학생의 평균 점수: {sum_grade / len(grades[i])}")

print(f"국어 평균 점수: {sum_grade_1 / len(grades)}")
print(f"영어 평균 점수: {sum_grade_2 / len(grades)}")
print(f"수학 평균 점수: {sum_grade_3 / len(grades)}")

for i in range(0, len(grades)):
    for j in range(0, len(grades[i])):
        if grades[i][j] >= 90:
            print(f"{i+1}번째 학생의 {j+1}번째 과목 점수: {grades[i][j]}")

ls = [[grade + 5 if grade + 5 <= 100 else 100 for grade in student] for student in grades]
for i in range(0, len(ls)):
    for j in range(0, len(ls[i])):
        print(f"{ls[i][j]}", end=", ")
    print()
