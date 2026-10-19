class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def calculate_grade(self):
        return self.grade

    def display_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.student_id)
        print("Grade:", self.calculate_grade())

class UndergraduateStudent(Student):
    def calculate_grade(self):
        if self.grade >= 70:
            return "First Class"
        elif self.grade >= 60:
            return "Upper Second Class"
        elif self.grade >= 50:
            return "Lower Second Class"
        elif self.grade >= 40:
            return "Third Class" 
        else:
            return "Fail"

class GraduateStudent(Student):
    def calculate_grade(self):
        if self.grade >= 70:
            return "Distinction"
        elif self.grade >= 60:
            return "Merit"
        elif self.grade >= 50:
            return "Pass"
        else:
            return "Fail"


student1 = UndergraduateStudent("Mohamed Ahmed", "MH2500510", 100)
student2 = GraduateStudent("Fatima Hassan", "FH2500511", 85)

print("Undergraduate Student:")
student1.display_info()

print()

print("Graduate Student:")
student2.display_info()