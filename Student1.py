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
    def __init__(self, name, student_id, grade, major):
        super().__init__(name, student_id, grade)
        self.major = major

    def calculate_grade(self):
        if self.grade >= 70:
            return "First Class"
        if self.grade >= 60:
            return "Upper Second Class"
        if self.grade >= 50:
            return "Lower Second Class" 
        if self.grade >= 40:
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
            return "Distinction"
        if self.grade >= 60:
            return "Merit"
        if self.grade >= 50:
            return "Pass"
        else:
            return "Fail"

    def display_info(self):
        super().display_info()
        print("Program Title:", self.program_title)
        print("Graduate Student")

student1 = Student("Mohamed Ahmed", "MH2500510", 100)
undergrad_student = UndergraduateStudent("Ali Hassan", "AH2500511", 95, "Computer Science")
grad_student = GraduateStudent("Fatima Ali", "FA2500512", 85, "Artificial Intelligence")

student1.display_info()
print()
undergrad_student.display_info()
print()
grad_student.display_info()