
class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  # Syntax - lambda arg:exp
  return sorted_students


# Example usage:
students = [
    Student("Madhu","B678", 9.8),
    Student("Anushka", "B524", 7.9),
    Student("Mahalakshmi", "B755", 7.1),
    Student("Vasantha", "B726", 8.4),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name:", student.name, "Roll Number:", student.roll_number, "CGPA:",
        student.cgpa)

 






