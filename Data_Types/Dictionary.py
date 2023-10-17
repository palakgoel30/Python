student_attendance = {"Pari":78,"parjeri":67,"pooja":45}

for student in student_attendance:
    print(f"{student}:{student_attendance[student]}")

# 2nd approach
for student,attendance in student_attendance.items():
    print(f"{student}:{attendance}")
print('t'*3)

#another example
attendance_value = student_attendance.values()
print(sum(attendance_value)/len(attendance_value))

my_dict = { 'num6': 6, 'num3': 3, 'num2': 10, 'num4': 4, 'num1': 1, 'num5': 5}
sortedDict = sorted(my_dict.items(),key=lambda x:x[1])
print(sortedDict)

