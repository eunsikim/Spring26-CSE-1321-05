# Create a function that takes in a list of floats.
# The function should calculate the average of the 
# numbers in the list and return the average.
def average(grades_list):
    grade_sum = 0

    for grade in grades_list:
        grade_sum += grade
    
    grade_average = grade_sum / len(grades_list)

    return grade_average

def main():
    quizzes = [80, 90, 30, 55, 100]
    quiz_avg = average(quizzes)

    print(f"The average Quiz grade is: {quiz_avg}")

if __name__ == "__main__":
    main()