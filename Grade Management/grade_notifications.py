class GradeNotifier:
    def __init__(self, students_data):
        self.students_data = students_data

    def notify_upcoming_assignments(self, student_name, upcoming_assignments):
        if student_name in self.students_data:
            print(f"Notifying {student_name} of upcoming assignments:")
            for assignment in upcoming_assignments:
                print(f"- {assignment}")
        else:
            print(f"Student '{student_name}' not found.")

    def notify_missing_assignments(self, student_name, missing_assignments):
        if student_name in self.students_data:
            if missing_assignments:
                print(f"Notifying {student_name} of missing assignments:")
                for assignment in missing_assignments:
                    print(f"- {assignment}")
            else:
                print(f"No missing assignments for {student_name}.")
        else:
            print(f"Student '{student_name}' not found.")

    def notify_low_grades(self, student_name, low_grade_threshold):
        if student_name in self.students_data:
            student_grades = self.students_data[student_name]
            low_grades = [assignment for assignment, grade in student_grades.items() if grade < low_grade_threshold]
            if low_grades:
                print(f"Notifying {student_name} of low grades:")
                for assignment in low_grades:
                    print(f"- {assignment}")
            else:
                print(f"No low grades for {student_name}.")
        else:
            print(f"Student '{student_name}' not found.")
