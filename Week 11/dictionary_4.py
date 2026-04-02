def avg(grades):
    sum_grade = 0

    for grade in grades:
        sum_grade += grade

    return sum_grade / len(grades)

def get_final_grade(students, student):
    lab_avg = avg(students[student]["Labs"])
    assignment_avg = avg(students[student]["Assignments"])
    midterm_exam = students[student]["Midterm Exam"]
    final_exam = students[student]["Final Exam"]

    return lab_avg * 0.1 + assignment_avg * .4 + midterm_exam * .2 + final_exam * .3

def main():
    students = {
        "John":{
            "Labs":[44, 66, 32, 16, 73, 49, 20, 63, 99, 5, 97, 92, 61],
            "Assignments": [8, 7, 37, 68, 85, 35, 86],
            "Midterm Exam": 89,
            "Final Exam": 90
        },
        "Daniel":{
            "Labs":[41, 18, 3, 28, 51, 70, 68, 73, 98, 89, 92, 6, 36],
            "Assignments": [40, 34, 24, 80, 77, 89, 58],
            "Midterm Exam": 70,
            "Final Exam": 61
        }
    }

    for student in students:
        print(f"{student} has a final grade of {get_final_grade(students, student)}")

if __name__ == "__main__":
    main()