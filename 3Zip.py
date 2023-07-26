students = ["Alice", "Bob", "Charlie", "David"]
grades = [85, 90, 78, 92]
colors = ['Red', 'Pink', 'Blue', 'Black']

for student, grade, color in zip(students, grades, colors):
    print(f"{student}: {grade}: {color}")

print(list(zip(students, grades, colors)))
