class ReportGenerator:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = {}

    def add_grade_for_student(self, student_name, assignment, grade):
        if student_name in self.students:
            if assignment not in self.students[student_name]:
                self.students[student_name][assignment] = grade
            else:
                print(f"Assignment '{assignment}' already exists for student '{student_name}'.")
        else:
            print(f"Student '{student_name}' not found.")

    def generate_student_report(self, student_name):
        if student_name in self.students:
            print(f"Report for {student_name}:")
            grades = self.students[student_name]
            total_points = sum(grades.values())
            total_assignments = len(grades)
            overall_grade = total_points / total_assignments if total_assignments > 0 else 0
            for assignment, grade in grades.items():
                print(f"{assignment}: {grade}")
            print(f"Overall grade: {overall_grade:.2f}")
        else:
            print(f"Student '{student_name}' not found.")

    def generate_class_report(self):
        print("Class Report:")
        for student_name, grades in self.students.items():
            print(f"Student: {student_name}")
            for assignment, grade in grades.items():
                print(f"{assignment}: {grade}")
