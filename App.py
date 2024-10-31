
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = int(age)
        self.address = address 

    def display_person_info(self): 
        return f"""
        Name: {self.name}
        Age: {self.age}
        Address: {self.address}"""
    

class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {} # """{ "subject_name" : "Grades" }"""
        self.enrolled_courses = []   # [DS,ALGO]

    def add_grade(self, course_name, grade):
        pass
        

    def enroll_course(self, course_name):
        pass


    def display_student_info(self):
        pass