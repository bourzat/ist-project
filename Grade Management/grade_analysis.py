import numpy as np


class GradeAnalyzer:
    @staticmethod
    def analyze_grades(students):
        grade_dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
        total_score = 0
        top_performers = []

        for student in students:
            grade = student.calculate_grade()
            grade_dist[grade] += 1
            total_score += np.mean(student.scores)
            if np.mean(student.scores) >= 85:
                top_performers.append(student.name)

        avg_score = total_score / len(students)

        return grade_dist, avg_score, top_performers
