# Code #62: Create a Class for Student with Marks and Grade Calculation
"""
    🧠 Why This Matters?
    Used in:
    - 🎓 Academic platforms and report generators
    - 📊 Grade analytics in LMS systems
    - 🧾 Exam simulation tools for trainin
"""
# Tier: Intermediate
# Goal: Build a class to store student name, subject marks, and compute final grade

# Python Code
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks # Dictionary of subject: score

    def calculate_total(self):
        return sum(self.marks.values())
    
    def calculate_average(self):
        return self.calculate_total() / len(self.marks)
    
    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return 'A+'
        elif avg >= 80:
            return 'A'
        elif avg >= 70:
            return 'B'
        elif avg >= 60:
            return 'C'
        else:
            return 'F'
        
    def report(self):
        print(f"Studen: {self.name}")
        print(f"Total Marks: {self.calculate_total()}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Grade: {self.calculate_grade()}")

# Sample Usage

data = {'Math': 85, 'Science': 90, 'English': 88}
student = Student("Sena",data)
student.report()

# Concept Breakdown
"""
    Concept             Description
    ---------------------------------
    __init__()          Initializes name & marks dictionary
    marks.values()      Accesses scores from dictionary
    sum()               Adds all subject scores
    Conditional logic   Converts average into grade
    report()            Presents a formatted output
"""
# You can extend this class with methods for rank assignment, subject-wsie analysis, or exporting to files

# Real-World Connection
"""
    - LMS dashboards for instructors
    - Automated performance alerts
    - Student profiling apps and grade predictors
"""