def get_grade(subject):
    grade = 0
    while True:
        try:
            grade = float(input(f"Enter {subject} grade: "))
            break
        except ValueError:
            print("Wrong input")
    return grade


def get_student_name():
    name = 0
    while True:
        try:
            name = input(f"Enter student's name: ")
            if len(name) == 0:
                raise ValueError()
            break
        except ValueError:
            print("Wrong input")
    return name


def get_student_info():
    name = get_student_name()
    english_grade = get_grade("English")
    math_grade = get_grade("Math")
    return{
        "Name" : name,
        "English" : english_grade,
        "Math" : math_grade
    }


def get_number_of_students():
    students = 0
    while True:
        try:
            students = int(input(f"Enter number of students: "))
            break
        except ValueError:
            print("Wrong input")
    return students


def print_student_info(students):
    print("Student Information:")
    for student in students:
        best_grade = student['Math'] if student['Math'] > student['English'] else student['English']
        average_grade = (student['Math'] + student['English']) / 2
        print(f"Student: {student['Name']}, Best Grade: {best_grade}, Average Grade: {average_grade}")


def calculate_average_grades(students):
    math_sum = 0
    english_sum = 0
    for student in students:
        math_sum += student['Math']
        english_sum += student['English']
    math_average = math_sum / len(students)
    english_average = english_sum / len(students)
    overall_average = (math_average + english_average) / 2
    return {'Math': math_average, 'English': english_average}, overall_average


def main():
    students_num = get_number_of_students()
    print()
    students = []
    for i in range(students_num):
        print(f"Enter details for student {i + 1}:")
        students.append(get_student_info())
        print()
    print_student_info(students)
    average_grades_per_subject, overall_average_grade = calculate_average_grades(students)
    print("\nAverage grades per subject:")
    for subject, average_grade in average_grades_per_subject.items():
        print(f"{subject}: {average_grade:.2f}")

    print(f"\nOverall average grade across all subjects: {overall_average_grade:.2f}")


if __name__ == '__main__':
    main()