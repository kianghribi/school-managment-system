import json
import emoji
from colorama import Fore , Back , Style , init
init(autoreset=True)
class Course:
    id:int=0
    name:str=""
    units:int=0
    score:float=0.0
    def __init__(self,id,name,units):
        self.id=id
        self.name=name
        self.units=units
    def __eq__(self,other):
        if isinstance(other,Course):
            return self.id==other.id
        return False
    def __str__(self):
        return f"id:{self.id}, name:{self.name}, units:{self.units}"
class Student:
    id:int=0
    name:str=""
    family:str=""
    courses:list[Course]=[]
    def __init__(self,id,name,family):
        self.id=id
        self.name=name
        self.family=family
        self.courses=[]
    def __eq__(self,other):
        if isinstance(other,Student):
            return self.id==other.id
        return False
    def __str__(self):
        return f"id:{self.id}, name:{self.name}, family:{self.family}"
    def print_info(self):
            print(f"id:{self.id}")
            print(f"name:{self.name}")
            print(f"family:{self.family}")
            print("courses:")
            print("\tID\tName\tUnits\tScore")
            for course in self.courses:
                print(f"\t{course.id}\t{course.name}\t{course.units}\t{course.score}")
    def add_course(self, course: Course):
        if course in self.courses:
            print(Fore.RED + emoji.emojize("This course is already added.:thumbs_down:") + Style.RESET_ALL)
            return
        new_course = Course(course.id, course.name, course.units)
        self.courses.append(new_course)
        print(Fore.GREEN + emoji.emojize (f"Course '{new_course.name}' added successfully.:check_mark:") + Style.RESET_ALL)

    def remove_course(self, course_id: int):
        course = Course(course_id, "", 0)
        if course in self.courses:
            self.courses.remove(course)
            print(Fore.GREEN + emoji.emojize("Course removed successfully.:cross_mark:") + Style.RESET_ALL)
        else:
            print(Fore.RED + emoji.emojize("The course doesn't exist.:check_mark:") + Style.RESET_ALL)
    def set_score(self, course_id: int, score: float):
        course = Course(course_id, "", 0)
        if course not in self.courses:
            print(Fore.RED + emoji.emojize("Course not found :cross_mark:") + Style.RESET_ALL)
            return
        index = self.courses.index(course)
        self.courses[index].score = score
        print(Fore.GREEN + emoji.emojize(f"Score of '{self.courses[index].name}' set to {score}.:thumbs_up:") + Style.RESET_ALL)
class Teacher:
    id:int=0
    name:str=""
    family:str=""
    grade:str=""
    courses:list[Course]=[]
    def __init__(self,id,name,family,grade):
        self.id=id
        self.name=name
        self.family=family
        self.grade=grade
        self.courses=[]
    def __eq__(self,other):
        if isinstance(other,Teacher):
            return self.id==other.id
        return False
    def __str__(self):
        return f"id:{self.id}, name:{self.name}, family:{self.family}, grade:{self.grade}"
    def print_info(self):
        print(f"id:{self.id}")
        print(f"name:{self.name}")
        print(f"family:{self.family}")
        print(f"grade:{self.grade}")
        print("courses:")
        print("\tID\tName\tUnits\tScore")
        for course in self.courses:
            print(f"\t{course.id}\t{course.name}\t{course.units}\t{course.score}")
    def add_course(self, course: Course):
        if course in self.courses:
            print(Fore.RED + emoji.emojize("This course is already added.:check_mark:")+ Style.RESET_ALL)
            return
        new_course = Course(course.id, course.name, course.units)
        self.courses.append(new_course)
        print(Fore.GREEN + emoji.emojize(f"Course '{new_course.name}' added successfully.:check_mark:")+ Style.RESET_ALL)
    def remove_course(self, course_id: int):
        course = Course(course_id, "", 0)
        if course in self.courses:
            self.courses.remove(course)
            print(Fore.GREEN + emoji.emojize("Course removed successfully.:cross_mark:")+ Style.RESET_ALL)
        else:
            print(Fore.RED + emoji.emojize("The course doesn't exist")+ Style.RESET_ALL)
            
class Classroom:
    id:int=0
    name:str=""
    course:Course
    teacher:Teacher
    students:list[Student]=[]
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __eq__(self,other):
        if isinstance(other,Classroom):
            return self.id==other.id
        return False
    def __str__(self):
        return f"id:{self.id}, name:{self.name}"
    
    def print_info(self):
        print(f"id:{self.id}")
        print(f"name:{self.name}")
        print("classrooms:")
        print("\tID\tClass\t\tCourse\t\tTeacher\t\tstudents")
        print(f"\t{self.id}\t{self.name}\t{ self.course.name }\t\t{self.teacher.name}\t\t{', '.join([s.name for s in self.students])}")

    def change_course(self, new_course: Course):
        self.course = new_course
        if self.teacher is not None and new_course not in self.teacher.courses:
            self.teacher = None
            print(Fore.RED + emoji.emojize("The current teacher does not teach this course. Teacher removed.:cross_mark:")+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + emoji.emojize(f"Classroom course changed to {new_course.name}.:check_mark:")+ Style.RESET_ALL)
        kept = []
        for s in self.students:
            if new_course in s.courses:
                kept.append(s)
            else:
                print(Fore.RED + emoji.emojize(f"Student ID {s.id} removed (does not have this course).:cross_mark:")+ Style.RESET_ALL)
        self.students = kept
    def change_teacher(self, new_teacher: Teacher):
        if new_teacher is None or self.course not in new_teacher.courses:
            print(Fore.RED + emoji.emojize("This teacher does not teach this course.:cross_mark:")+ Style.RESET_ALL)
            return
        self.teacher = new_teacher
        print(Fore.GREEN + emoji.emojize(f"Teacher changed to {new_teacher.name} {new_teacher.family}.:check_mark:")+ Style.RESET_ALL)
    def add_student(self, student: Student):
        if student in self.students:
            print(Fore.RED + emoji.emojize("Student already in this classroom.:cross_mark:")+ Style.RESET_ALL)
            return
        if not any(c.id == self.course.id and c.score < 10 for c in student.courses):
            print(Fore.RED + emoji.emojize("Student does not qualify (no failing score in this course).:cross_mark:")+ Style.RESET_ALL)
            return
        self.students.append(student)
        print(Fore.GREEN + emoji.emojize(f"Student {student.name} {student.family} added successfully.:check_mark:")+ Style.RESET_ALL)

    def remove_student(self, student_id: int):
        student = Student(student_id, "", "")
        if student in self.students:
            self.students.remove(student)
            print(Fore.GREEN + emoji.emojize("Student removed successfully.:check_mark:")+ Style.RESET_ALL)
        else:
            print(Fore.RED + emoji.emojize("Student not found in this classroom.:cross_mark:")+ Style.RESET_ALL)
class School:
    name:str=""
    selected_student:Student=None
    selected_teacher:Teacher=None
    selected_classroom:Classroom=None
    courses:list[Course]=[]
    teachers:list[Teacher]=[]
    students:list[Student]=[]
    classrooms:list[Classroom]=[]
    def __init__(self,name):
        self.name=name
    def add_student(self,student:Student):
        if student in self.students:
            print(Fore.RED + emoji.emojize("The student already exist.:cross_mark:")+ Style.RESET_ALL)
        else:
            self.students.append(student)
            print(Fore.GREEN + emoji.emojize("student added sucssefully.:check_mark:")+ Style.RESET_ALL)
    def add_course (self,course:Course):
        if course in self.courses:
            print(Fore.RED + emoji.emojize("The course already exist.:cross_mark:")+ Style.RESET_ALL)
            
        else:
            self.courses.append(course)
            print(Fore.GREEN + emoji.emojize("course add succsesfully.:check_mark:")+ Style.RESET_ALL)
    def add_teacher (self,teacher:Teacher):
        if teacher in self.teachers:
            print(Fore.RED + emoji.emojize("The teacher already exist.:cross_mark:")+ Style.RESET_ALL)
        else:
            self.teachers.append(teacher)
            print(Fore.GREEN + emoji.emojize("teacher added sucssefully.:check_mark:")+ Style.RESET_ALL)
    def load_data(self):
        with open("dataa.json","rt")as f1:
            data=json.load(f1)   
        for item in data["courses"]:
            c= Course(item["id"], item["name"] , item["units"])
            self.courses.append(c)
            
        for item in data["students"]:
            s= Student(item["id"], item["name"] , item["family"])
            student_courses = []
            for course_id, score in item.get("courses", []):
                course_student = Course(course_id, "", 0)
                index = self.courses.index(course_student)
                original = self.courses[index]
                new_course = Course(original.id, original.name, original.units)
                new_course.score = score
                student_courses.append(new_course)
            s.courses = student_courses
            self.students.append(s)
        
        for item in data["teachers"]:
            teacher= Teacher(item["id"], item["name"] , item["family"], item["grade"])
            for course_id in item["courses"]:
                course_example = Course(course_id, "", 0)
                crs = self.courses[self.courses.index(course_example)]
                if crs not in teacher.courses:  
                    teacher.courses.append(crs)
            self.teachers.append(teacher)


        for item in data["classrooms"]:
            classroom=Classroom(item["id"], item["name"])

            course_temp = Course(item["course"], "", 0)
            course_index = self.courses.index(course_temp)
            classroom.course = self.courses[course_index]

            teacher_temp = Teacher(item["teacher"], "", "", "")
            teacher_index = self.teachers.index(teacher_temp)
            classroom.teacher = self.teachers[teacher_index]
            student_objs = []
            for student_id in item["students"]:
                student_temp = Student(student_id, "", "")
                student_index = self.students.index(student_temp)
                student_objs.append(self.students[student_index])
            classroom.students = student_objs

            self.classrooms.append(classroom)
    def save_data(self):
        course_data = [{"id": c.id, "name": c.name, "units": c.units} for c in self.courses]
    
        student_data = []
        for s in self.students:
            courses_list = [[c.id, c.score] for c in s.courses]
            student_data.append({
                "id": s.id,
                "name": s.name,
                "family": s.family,
                "courses": courses_list
            })
        teacher_data = []
        for t in self.teachers:
            courses_ids = [c.id for c in t.courses]
            teacher_data.append({
                "id": t.id,
                "name": t.name,
                "family": t.family,
                "grade": t.grade,
                "courses": courses_ids 
            })
        classroom_data = []
        for cls in self.classrooms:
            classroom_data.append({
                "id": cls.id,
                "name": cls.name,
                "course": cls.course.id,
                "teacher": cls.teacher.id,
                "students": [s.id for s in cls.students]
            })
        output = {
            "courses": course_data,
            "students": student_data,
            "teachers": teacher_data,
            "classrooms": classroom_data
        }
        with open("saves.json", "wt") as f2:
            json.dump(output, f2) 
        
    def remove_student(self,id):
        student_id = Student(id, "", "")
        if student_id not in self.students:
            print(Fore.RED + emoji.emojize("The student doesn't exist.:cross_mark:")+ Style.RESET_ALL)
        elif any(True for cls in self.classrooms for s in cls.students if s.id == id):
            print(Fore.RED + emoji.emojize("This student is used in a classroom and cannot be removed.:cross_mark:")+ Style.RESET_ALL)
        else:
            self.students.remove(student_id)
            print(Fore.GREEN + emoji.emojize("Student removed successfully.:check_mark:")+ Style.RESET_ALL)
    def remove_course(self,id):
        course_id = Course(id,"",0)
        if course_id not in self.courses:
            print(Fore.RED + emoji.emojize("the course doesn't exist.:cross_mark:")+ Style.RESET_ALL)
        elif (any(c.id == id for student in self.students for c in student.courses) or
              any(c.id == id for teacher in self.teachers for c in teacher.courses) or
              any(cls.course is not None and cls.course.id == id for cls in self.classrooms)+ Style.RESET_ALL):
                print(Fore.RED + emoji.emojize("This course is used in a student, teacher, or classroom and cannot be removed.:cross_mark:")+ Style.RESET_ALL)
        else:
            self.courses.remove(course_id)
            print(Fore.GREEN + emoji.emojize("Course removed successfully.:check_mark:")+ Style.RESET_ALL)
    def remove_teacher(self, id):
        teacher_id = Teacher(id, "", "", "")
        if teacher_id not in self.teachers:
            print(Fore.RED + emoji.emojize("The teacher doesn't exist.:cross_mark:")+ Style.RESET_ALL)
        elif any(cls.teacher is not None and cls.teacher.id == id for cls in self.classrooms):
            print(Fore.RED + emoji.emojize("This teacher is used in a classroom and cannot be removed.")+ Style.RESET_ALL)
        else:
            self.teachers.remove(teacher_id)
            print(Fore.GREEN + emoji.emojize("Teacher removed successfully.:check_mark:")+ Style.RESET_ALL)
            
    def remove_classroom(self,id):
        id_classroom = Classroom(id,"")
        if id_classroom in self.classrooms:
            self.classrooms.remove(id_classroom)
            print(Fore.GREEN + emoji.emojize("classroom removed successfully.:check_mark:")+ Style.RESET_ALL)
        else:
            print(Fore.RED + emoji.emojize("the classroom doesn't exist.:cross_mark:")+ Style.RESET_ALL)

    def edit_student(self,student:Student):
        if student not in self.students:
            print(Fore.RED + emoji.emojize("The student dosen't exist.:cross_mark:")+ Style.RESET_ALL)
        else:
             index = self.students.index(student)  
             self.students[index].name = student.name
             self.students[index].family = student.family
             print(Fore.GREEN +emoji.emojize( "Student edited successfully.:check_mark:")+ Style.RESET_ALL)
    def edit_teacher(self,teacher:Teacher):
        if teacher not in self.teachers:
            print(Fore.RED + emoji.emojize("The teacher doesn't exist.:cross_mark:")+ Style.RESET_ALL)
        else:
             index = self.teachers.index(teacher)  
             self.teachers[index].name = teacher.name
             self.teachers[index].family = teacher.family
             self.teachers[index].grade = teacher.grade
             print(Fore.GREEN +emoji.emojize("Student edited successfully.:check_mark:")+ Style.RESET_ALL)
    def edit_course(self,course:Course):
        if course not in self.courses:
            print(Fore.RED + emoji.emojize("The student dosen't exist.:cross_mark:")+ Style.RESET_ALL)
        else:
             index = self.courses.index(course)  
             self.courses[index].name = course.name
             self.courses[index].units = course.units
             print(Fore.GREEN +emoji.emojize("Student edited successfully.:check_mark:")+ Style.RESET_ALL )
    def edit_classroom(self,classroom:Classroom):
        if classroom not in self.classrooms:
            print(Fore.RED + emoji.emojize("The classroom dosen't exist.:cross_mark:")+ Style.RESET_ALL)
        else:
            index = self.classrooms.index(classroom)
            self.classrooms[index].name=classroom.name
    
    def print_students(self):
        for student in self.students:
            print(student)
        
    def print_courses(self):
        for course in self.courses:
            print(course)
        
    def print_teachers(self):
        for teacher in self.teachers:
            print(teacher)

    def print_classroom(self):
        for classroom in self.classrooms:
            print(classroom)