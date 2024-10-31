import json
students = []
courses = []


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
        flag = False
        for c_name in self.enrolled_courses:
            if c_name == course_name:
                flag = True
                break
        
        if flag:
            self.grades[course_name] = grade
            print(f"\nGrade {grade} added for {self.name} in {course_name}.\n")
            pass
        else:
            print(f"\n{self.name} is not enrolled in {course_name}.\n")
            pass
        

    def enroll_course(self, course_name):
        already_enrolled = False
        for c_name in self.enrolled_courses:
            if c_name == course_name:
                already_enrolled = True
        
        if not already_enrolled:
            self.enrolled_courses.append(course_name)
            return True
        else:
            return False


    def display_student_info(self):
        print(self.display_person_info())
        print(f"""\tStudent ID: {self.student_id}
        Grades: {self.grades}
        Enrolled Courses: {self.enrolled_courses}""")
        pass


class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.course_students = []
    
    def add_student(self, student,data_loaded = True): # pass it as a object (student's)
        no_duplicate = True
        S_id = student.student_id
        S_name = student.name
        C_Code = self.course_code
        C_name = self.course_name
        



        for s in self.course_students:
            if s.student_id == S_id:
                no_duplicate == False
                break   
        if no_duplicate:
            self.course_students.append(student)
            if data_loaded:
                print(f"\nStudent {S_name} (ID: {S_id}) enrolled in {C_name} (Code: {C_Code}).")
                pass
        else:
            if data_loaded:
                print(f"\nStudent {S_name} (ID: {S_id} already enrolled in {C_name} (Code{C_Code}.")
                pass


    def display_course_info(self):
        print(f"""
        Course Name: {self.course_name}
        Code: {self.course_code}
        Instructor: {self.instructor}
        Enrolled Students: {[student.name for student in self.course_students]}""")

def save_data():
    
    unique_students = {student.student_id: student for student in students}.values()
    unique_courses = {course.course_code: course for course in courses}.values()


    
    
    data = {
        "students": [
            {
                "name": student.name,
                "age": student.age,
                "address": student.address,
                "student_id": student.student_id,
                "grades": student.grades,
                "enrolled_courses": student.enrolled_courses
            }
            for student in unique_students
        ],
        "courses": [
            {
                "course_name": course.course_name,
                "course_code": course.course_code,
                "instructor": course.instructor,
                "course_students": [s.student_id for s in course.course_students]
            }
            for course in unique_courses
        ]
    }
    with open("students_data.json", "w") as file:
        json.dump(data, file, indent=4)
    print("\n\tData saved successfully.\n")


def load_data(data_loaded=False):
    try:
        with open("students_data.json", "r") as file:
            data = json.load(file) # { "Key" : "Value"}

            # student
            existing_student_ids =set()
            for student in students:
                existing_student_ids.add(student.student_id)
            
            for s_data in data["students"]:
                if s_data["student_id"] not in existing_student_ids:

                    t_name = s_data["name"]
                    t_age =  s_data["age"]
                    t_address = s_data["address"]
                    t_student_id = s_data["student_id"]
                    t_grades = s_data["grades"]
                    t_enrolled_courses = s_data["enrolled_courses"]

                    student = Student(t_name,t_age,t_address,t_student_id)
                    student.grades =t_grades
                    student.enrolled_courses = t_enrolled_courses

                    students.append(student)
                    # track load
                    existing_student_ids.add(s_data["student_id"])


            # course
            existing_course_codes = set()
            for course in courses:
                existing_course_codes.add(course.course_code)


            for c_data in data["courses"]:
                if c_data["course_code"] not in existing_course_codes:

                    t_course_name =c_data["course_name"]
                    t_course_code = c_data["course_code"]
                    t_instructor = c_data["instructor"]
                    course = Course(t_course_name,t_course_code,t_instructor)


                    
                    for student_id in c_data["course_students"]:
                        
                        student = None
                        for s in students:
                             if s.student_id == student_id:
                                 student = s
                                 break
                        
                        if student:
                            course.add_student(student,data_loaded=False)
                    
                    courses.append(course)
                    # track load
                    existing_course_codes.add(c_data["course_code"])

        if data_loaded:
            print("\n\tData loaded successfully.\n")

    
    except FileNotFoundError:
        if data_loaded:
            print(f"\n\tNo file found {FileNotFoundError}\n")



if __name__ == '__main__':
    data_loaded = False
    load_data(data_loaded)
    data_loaded = True
    while True:
        print("\n==== Student Management System ====\n")
        print("""
        1. Add New Student
        2. Add New Course
        3. Enroll Student in Course
        4. Add Grade for Student
        5. Display Student Details
        6. Display Course Details
        7. Save Data to File
        8. Load Data from File
        0. Exit    
        """)
        option = input("Select Option: ")

        if option =="":
            print("\n\tplease choose a option\n")
            continue

        if option == "1":  
            try :
                name = input("Enter Name: ")
                age = input("Enter Age: ")
                address = input("Enter Address: ")
                student_id_t = input("Enter Student ID: ")

                
                if not name or not age or not address or not student_id_t:
                    print("\n\tInput Value Missing!!!\n")
                    continue
                
                already_exists = False
                for student in students:
                    if  student.student_id == student_id_t:
                        already_exists = True
                        break

                if already_exists:
                    print(f"\nStudent {name} ID {student_id_t} already exists.\n")
                    pass
                else:
                    student_obj = Student(name,age,address,student_id_t)
                    students.append(student_obj)
                    print(f"\nStudent {name} (ID: {student_id_t}) added successfully.\n")

            except Exception as error:
                print(f"\nInvalid {error}")
                print('\tPlease try again\t\n')

        elif option == "2":  
            try:
                course_name_t = input("Enter Course Name: ")
                course_code_t = input("Enter Course Code: ")
                instructor_t= input("Enter Instructor Name: ")

                if not course_name_t or not course_code_t or not instructor_t:
                    print("\n\tInput Value Missing!!!\n")
                    continue
                
                already_exists = False
                for course in courses:
                    if course.course_code == course_code_t:
                        already_exists = True
                        break

                if not already_exists:
                    course_obj =Course(course_name_t,course_code_t,instructor_t) 
                    courses.append(course_obj)
                    print(f"\nCourse {course_name_t} (Code: {course_code_t}) created with instructor {instructor_t}.\n")
                else:
                    print(f"\nCourse {course_name_t} Code {course_code_t} already exists.\n")
            except Exception as error:
                print(f"\nInvalid, {error}")
                print('\n\tPlease try again\n')


        elif option == "3":   # IT has a bug , it add same person or course multiple time, doesn't restrict
            try:

                S_id = input("Enter Student ID: ")
                C_code = input("Enter Course Code: ")

                if not S_id or not C_code :
                    print("\n\tInput Value Missing!!!\n")
                    continue

                student_obj = None
                for student in students:
                    if student.student_id == S_id:
                        student_obj = student
                        break

                course_obj = None
                for course in courses:
                    if course.course_code == C_code:
                        course_obj = course
                        break
                if student_obj is None:
                    print(f"\n\tStudent {S_id} doesn't exists.\n")
                    continue
                elif course_obj is None:
                    print(f"\n\tCourse {C_code} doesn't exists.\n")
                    continue



                if student and course:
                    re = student.enroll_course(course.course_name)
                    if not re:
                        print("\n\tInvalid Student ID or Course Code.\n")
                    else:
                        course.add_student(student)
                else:
                    print("\n\tInvalid Student ID or Course Code.\n")
            except Exception as error:
                print(f"\nInvalid, {error}")
                print('\tPlease try again')

        elif option == "4":
            try:
                S_id = input("Enter Student ID: ")
                C_code = input("Enter Course Code: ")
                grade = input("Enter Grade: ")

                if not S_id or not C_code or not grade:
                    print("\n\tInput Value Missing!!!\n")
                    continue

                student_obj = None
                student_exists = False
                for student in students:  
                    if S_id == student.student_id:
                        student_obj = student
                        student_exists = True
                        break

                course_obj = None
                course_exists = False

                for course in courses:
                    if C_code == course.course_code:
                        course_obj = course
                        course_exists = True
                        break

                
                if not student_exists:
                    print("\n\tStudent doesn't exists!!!\n")
                    continue
                elif not course_exists:
                    print("\n\tCourse doesn't exists!!!\n")
                    continue
                
                student_has_course = course_obj.course_name in student_obj.enrolled_courses



                if student_has_course:
                    student.add_grade(course.course_name,grade)
                else:
                    print("\n\tInvalid Operation!!!\n")
                
            except Exception as error:
                print(f"\nInvalid, {error}")
                print('\n\tPlease try again\n')

        elif option == "5": 
            try:

                S_id = input("Enter Student ID: ")

                if not S_id:
                    print("\n\tInput Value Missing!!!\n")
                    continue

                student_obj = None

                for student in students:
                    if student.student_id == S_id:
                        student_obj = student
                        break

                if student:
                    student.display_student_info()
                else:
                    print("\n\tStudent not found!!!\n")
            except Exception as error:
                print(f"Invalid, {error}")
                print('Please try again')


        
        elif option == "6":  
            try:

                C_code = input("Enter Course Code: ")

                if not C_code :
                    print("\n\tInput Value Missing!!!\n")
                    continue

                course_obj = None
                for course in courses:
                    if course.course_code == C_code:
                        course_obj = course
                        break
                
                if course:
                    course.display_course_info()
                else:
                    print("Course not found.")
            except Exception as error:
                print(f"Invalid, {error}")
                print('Please try again')

        elif option == "7":  

            try:
                save_data()
            except Exception as error:
                print(f"Invalid, {error}")
                print('Please try again')
            pass

        elif option == "8":  
            try:
                load_data(data_loaded=True)
            except Exception as error:
                print(f"Invalid, {error}")
                print('Please try again')
            pass

        elif option == "0":
            print("\n\tExiting Student Management System. Goodbye!\n")
            break
        else:
            print("\nInvalid Input")
            print("Please Choose an correct Option\n")
            