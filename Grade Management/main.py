from grade_analysis import GradeAnalyzer
from grade_calculation import GradeCalculator
from grade_management import GradeManager
from grade_notifications import GradeNotifier
from report_generation import ReportGenerator


def main():
    # Load students from CSV
    filename = 'students.csv'
    students = GradeManager.load_students_from_csv(filename)

    # Grade analysis
    grade_dist, avg_score, top_performers = GradeAnalyzer.analyze_grades(students)

    # Print analysis results
    print("Grade distribution:")
    for grade, count in grade_dist.items():
        print(f"{grade}: {count}")

    print(f"\nAverage score: {avg_score:.2f}")
    print(f"Top performers (above 85%): {', '.join(top_performers)}")

    # Report generation
    report_gen = ReportGenerator()
    for student in students:
        report_gen.add_student(student.name)
        for assignment, grade in student.scores.items():
            report_gen.add_grade_for_student(student.name, assignment, grade)

    # Generate reports
    report_gen.generate_class_report()
    for student in students:
        report_gen.generate_student_report(student.name)

    # Grade calculation
    grades_data = {student.name: student.scores for student in students}
    calculator = GradeCalculator(grades_data)

    # Calculate overall grades based on weighted averages
    weights = [0.2, 0.2, 0.2, 0.2, 0.2]  # Equal weights for each assignment
    overall_grades_weighted = calculator.calculate_overall_grades_weighted(weights)
    print("\nOverall Grades (Weighted Average):")
    for student, grade in overall_grades_weighted.items():
        print(f"{student}: {grade:.2f}")

    # Calculate overall grades based on custom grading criteria
    custom_criteria = [0.1, 0.2, 0.3, 0.2, 0.2]  # Custom criteria for each assignment
    overall_grades_custom = calculator.calculate_overall_grades_custom(custom_criteria)
    print("\nOverall Grades (Custom Criteria):")
    for student, grade in overall_grades_custom.items():
        print(f"{student}: {grade:.2f}")

    # Notify students
    notifier = GradeNotifier(grades_data)
    student_name = "John"  # Example student name for notifications
    upcoming_assignments = ["Math Assignment", "Science Project"]
    missing_assignments = ["History Essay"]
    low_grade_threshold = 70

    notifier.notify_upcoming_assignments(student_name, upcoming_assignments)
    notifier.notify_missing_assignments(student_name, missing_assignments)
    notifier.notify_low_grades(student_name, low_grade_threshold)


if __name__ == "__main__":
    main()
