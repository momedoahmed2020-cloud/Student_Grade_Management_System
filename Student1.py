class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.__grade = [grade]

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade.append(grade)

    def calculate_average(self):
        if len(self.__grade) == 0:
            return 0
        return sum(self.__grade) / len(self.__grade)

    def calculate_grade(self):
        return self.calculate_average()

    def display_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.student_id)
        print("Grade:", self.__grade)
        print("Average Grade:", self.calculate_average())


student1 = Student("Mohamed Ahmed", "MH2500510", 100)

student1.set_grade(95)
student1.set_grade(90)

print("Grades:", student1.get_grade())
print("Average Grade:", student1.calculate_average())   
print("Calculated Grade:", student1.calculate_grade())

student1.display_info()