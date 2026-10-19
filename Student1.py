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
        print("Grade:", self.grade)

class UndergraduateStudent(Student):
    def __init__(self, name, student_id, grade, major):
        super().__init__(name, student_id, grade)
        self.major = major

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

    def display_info(self):
        super().display_info()
        print("Major:", self.major)
        print("Undergraduate Student")

class GraduateStudent(Student):
    def __init__(self, name, student_id, grade, program_title):
        super().__init__(name, student_id, grade)
        self.program_title = program_title

    def calculate_grade(self):
        if self.grade >= 70:
            return "Pass with Distinction"
        elif self.grade >= 60:
            return "Pass with Merit"
        elif self.grade >= 50:
            return "Pass"
        else:
            return "Fail"

    def display_info(self):
        super().display_info()
        print("Program Title:", self.program_title)
        print("Graduate Student")


undergraduate_student1 = UndergraduateStudent("Ali Hassan", "AH2500511", 95, "Computer Science")
graduate_student1 = GraduateStudent("Fatima Ali", "FA2500512", 85, "Master of Science in Computer Science")

undergraduate_student1.display_info()
print()

graduate_student1.display_info()
print()