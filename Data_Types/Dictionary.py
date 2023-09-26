student_attendance = {"Pari":78,"parjeri":67,"pooja":45}

for student in student_attendance:
    print(f"{student}:{student_attendance[student]}")

# 2nd approach
for student,attendance in student_attendance.items():
    print(f"{student}:{attendance}")


#another example
attendance_value = student_attendance.values()
print(sum(attendance_value)/len(attendance_value))