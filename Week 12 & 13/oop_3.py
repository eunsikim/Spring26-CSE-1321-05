class section:
    def __init__(self, section_number):
        self.students = []
        self.section_number = section_number

        # Data Entry
        while True:
            name = input("Enter student name or -1 to stop: ")

            if name == "-1":
                break

            assignments_str = input("Assignments: ").split(", ")

            assignments_float = []
            for val in assignments_str:
                assignments_float.append(float(val))

            labs_str = input("Labs: ").split(", ")

            labs_float = []
            for val in labs_str:
                labs_float.append(float(val))

            exams_str = input("Exams: ").split(", ")

            exams_float = []
            for val in exams_str:
                exams_float.append(float(val))

            self.students.append(student(name, assignments_float, labs_float, exams_float))

    def get_class_avg(self):
        class_sum = 0

        for st in self.students:
            class_sum += st.get_final_grade()

        return class_sum / len(self.students)
    
    def print_final_grades(self):
        for st in self.students:
            print(f"{st.name} has a final grade of {st.get_final_grade():.2f}")
    
    def print_class_avg(self):
        print(f"CSE 1321L Section {self.section_number} has an avg. grade of {self.get_class_avg():.2f}")


class student:
    def __init__(self, name, assignments, labs, exams):
        self.name = name
        self.assignments = assignments
        self.labs = labs
        self.exams = exams
    
    def get_average(self, grade_list):
        grade_sum = 0

        for grade in grade_list:
            grade_sum += grade
        
        grade_avg = grade_sum / len(grade_list)

        return grade_avg
    
    def get_final_grade(self):
        lab_avg = self.get_average(self.labs)
        assignment_avg = self.get_average(self.assignments)
        midterm_exam = self.exams[0]
        final_exam = self.exams[1]

        final_grade = lab_avg * 0.1 + assignment_avg * 0.4 + midterm_exam * 0.2 + final_exam * 0.3

        return final_grade

def main():

    my_sections = []

    my_sections.append(section("05"))
    my_sections.append(section("51"))

    print()
    my_sections[0].print_class_avg()
    my_sections[0].print_final_grades()
    print()
    my_sections[1].print_class_avg()
    my_sections[1].print_final_grades()

    

if __name__ == "__main__":
    main()

        
        

        