students = ["Alice", "Bob", "Charlie", "David"]
grades = [85, 90, 78, 92]

for student, grade in zip(students, grades):
    print(f"{student}: {grade}")

print(list(zip(students, grades)))