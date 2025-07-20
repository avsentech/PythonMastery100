# Code #65: Create an Employee Attendance Tracker Class
"""
    🧠 Why This Matters?
    Used in:
    - 🏢 HR and payroll systems
    - 📅 Attendance dashboards
    - 📋 Time tracking for teams or freelancer
"""
# Tier: Intermediate
# Goal: Build a class to trakc employee attendance and status

# Python Code
class Employee:
    def __init__(self, name):
        self.name = name
        self.attendance = [] # Stores dates attended

    def mark_attendance(self, date):
        if date not in self.attendance:
            self.attendance.append(date)
            print(f"{self.name} marked presenton {date}.")
        else:
            print(f"{self.name} already marked for {date}.")

    def has_attended(self, date):
        return date in self.attendance
    

    def total_days_present(self):
        return len(self.attendance)
        
# Sample Usage
e1 = Employee("Sena")
e1.mark_attendance("2025-07-20")
e1.mark_attendance("2025-07-21")
print(f"Has attended on 2025-07-21: {e1.has_attended('2025-07-21')}")
print(f"Total Days Preset: {e1.total_days_present()}")

# Sample Output
"""
    Sena marked presenton 2025-07-20.
    Sena marked presenton 2025-07-21.
    Has attended on 2025-07-21: True
    Total Days Preset: 2 
"""

# Concept Breakdown
"""
    Concept                 Description
    ------------------------------------
    attendance list         Stores marked dates
    mark_attendance(date)   Adds date to list if not already present
    has_attended(date)      Checks if date exists in list
    total_days_present()    Returns count of present days
"""
# Extendable with: leave requests, login times, attendance reports, or file export featues.

# Real-World Connection
"""
    - HR systems and biometric check-ins
    - Freelance trackers with timestamps
    - Employee KPI dashboards
"""