class GradeCalculator:
    def _init_(self, students_data):
        self.students_data = students_data

    def calculate_overall_grades_weighted(self, weights):
        overall_grades = {}
        for student, grades in self.students_data.items():
            if len(grades) != len(weights):
                raise ValueError("Number of grades and weights must be equal")

            weighted_sum = sum(grade * weight for grade, weight in zip(grades, weights))
            total_weight = sum(weights)
            overall_grade = weighted_sum / total_weight
            overall_grades[student] = overall_grade
        return overall_grades

    def calculate_overall_grades_custom(self, custom_criteria):
        overall_grades = {}
        for student, grades in self.students_data.items():
            if len(grades) != len(custom_criteria):
                raise ValueError("Number of grades and custom criteria must be equal")

            overall_grade = sum(grade * criteria for grade, criteria in zip(grades, custom_criteria))
            overall_grades[student] = overall_grade
        return overall_grades
