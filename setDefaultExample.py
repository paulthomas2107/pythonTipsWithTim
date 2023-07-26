student_grades = {}

maths_grades = student_grades.get('Alice', {})
maths_grades['math'] = 90
print(student_grades)

english_grades = student_grades.setdefault('Alice', {})
english_grades['english'] = 85
print(student_grades)