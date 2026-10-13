class student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Grade: {self.grade}")

student1 = student("Mohamed Ahmed", "MH2500510", "100")
student1.display_info()