students = {
    '1001': {'name': 'Ali', 'grades': {'math': 85, 'science': 92}},
    '1002': {'name': 'Sara', 'grades': {'math': 78, 'science': 88}},
}

def add_student(student_id, name, grades):
    students[student_id] = {'name': name, 'grades': grades}

def calculate_average(student_id):
    grades = students[student_id]['grades'].values()
    return sum(grades) / len(grades)


def display_student(student_id):
    if student_id in students:
        student = students[student_id]
        print(f"Name: {student['name']}")
        print("Grades:")
        for subject, grade in student['grades'].items():
            print(f"{subject}: {grade}")
        print(f"Average Grade: {calculate_average(student_id):.2f}")
    else:
        print("Student not found.")


def remove_student(student_id):
    if student_id in students:
        del students[student_id]
        print(f"Student with ID {student_id} removed.")
    else:
        print("Student not found.")


add_student('1003', 'Reza', {'math': 90, 'science': 95, 'history': 88})
display_student('1003')
remove_student('1002')
