student_score = {
  "Monty": 91,
  "Aakash": 70,
  "Mohit": 72,
  "Ankit": 51,
  "Panday": 92,
}

student_grade = {}

for student in student_score:
  # print(student)
  score = student_score[student]
  if score > 90:
    student_grade[student] = "Outstanding"
  elif score > 80:
    student_grade[student] = "Exceed exceptions"
  elif score > 70:
    student_grade[student] = "Acceptable"
  else:
    student_grade[student] = "Fail"      
print(student_grade)    



