grades = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    grades.append([name, score])

sorted_grade = sorted(set([x[1] for x in grades]))
for student in sorted(x[0] for x in grades if x[1] == sorted_grade[1]):
    print(student)
