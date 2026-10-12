class student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name}, Student ID: {self.student_id}, Grade: {self.grade}"

student1 = student("Mohamed Ahmed", "MH2500510", "100")
print(student1.display_info())