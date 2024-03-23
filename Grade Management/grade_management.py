import csv
import numpy as np


class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_grade(self):
        avg_score = np.mean(self.scores)
        if avg_score >= 90:
            return 'A'
        elif avg_score >= 80:
            return 'B'
        elif avg_score >= 70:
            return 'C'
        elif avg_score >= 60:
            return 'D'
        else:
            return 'F'


class GradeManager:
    @staticmethod
    def load_students_from_csv(filename):
        students = []
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            for row in reader:
                name = row[0]
                scores = [int(score) for score in row[1:]]
                students.append(Student(name, scores))
        return students
