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

sc1 = School("sama")
sc1.load_data()
level="root"
while True:
    if level=="root":
        print(Fore.YELLOW + "1." + Fore.WHITE + emoji.emojize(" :man_student:") + " students"    + Style.RESET_ALL)
        print(Fore.YELLOW + "2." + Fore.WHITE + emoji.emojize(" :man_teacher:") + " teachers"    + Style.RESET_ALL)
        print(Fore.YELLOW + "3." + Fore.WHITE + emoji.emojize(" :books:")       + " courses"      + Style.RESET_ALL)
        print(Fore.YELLOW + "4." + Fore.WHITE + emoji.emojize(" :school:")      + " classrooms"   + Style.RESET_ALL)
        print(Fore.GREEN  + "5." + Fore.WHITE + emoji.emojize(" :floppy_disk:") + " save"         + Style.RESET_ALL)
        print(Fore.RED    + "0." + Fore.WHITE + emoji.emojize(" :door:")        + " exit"         + Style.RESET_ALL)
        cmd=int(input())
        if cmd==1:
            level="students"
        elif cmd==2:
            level="teachers"
        elif cmd==3:
            level="courses"
        elif cmd==4:
            level="classrooms"
        elif cmd==5:
            sc1.save_data()
        elif cmd==0:
            level="root"
            print("exit")
            
    elif level=="students":
        print(Fore.YELLOW + "1." + Fore.WHITE + emoji.emojize(" :clipboard:")   + " show students"   + Style.RESET_ALL)
        print(Fore.YELLOW + "2." + Fore.WHITE + emoji.emojize(" :plus:")        + " add students"    + Style.RESET_ALL)
        print(Fore.YELLOW + "3." + Fore.WHITE + emoji.emojize(" :keyboard:")     + " edit students"   + Style.RESET_ALL)
        print(Fore.YELLOW + "4." + Fore.WHITE + emoji.emojize(" :wastebasket: ") + " delete students" + Style.RESET_ALL)
        print(Fore.YELLOW + "5." + Fore.WHITE + emoji.emojize(" :backhand_index_pointing_up_light_skin_tone:")   +  " select students" + Style.RESET_ALL)
        print(Fore.RED    + "0." + Fore.WHITE + emoji.emojize(" :BACK_arrow:")      + " back"       + Style.RESET_ALL)
        cmd=int(input())
        if cmd==1:
            sc1.print_students() 
        elif cmd==2:
            id = int(input("id:"))
            name= str(input("name:"))
            family= str(input("family:"))
            sc1.add_student(Student(id, name , family))
        elif cmd==3:
            id = int(input("id:"))
            name= str(input("new_name:"))
            family= str(input("new_family:"))
            sc1.edit_student(Student(id, name, family))
        elif cmd==4:
            id=int(input("id:"))
            sc1.remove_student(id)
        elif cmd==5:
            sc1.print_students()
            student_id = int(input("Enter id too select:"))
            student_object = Student(student_id, "", "")
            if student_object in sc1.students:
                indexx = sc1.students.index(student_object)
                sc1.selected_student = sc1.students[indexx]
                print(Fore.GREEN + emoji.emojize(f"Student {sc1.selected_student.name} {sc1.selected_student.family} selected.:check_mark:")+ Style.RESET_ALL)
            else:
                print(Fore.RED + emoji.emojize("Student not found.:cross_mark:")+ Style.RESET_ALL)
                level = "students"
            level="select students"
        elif cmd==0:
            level="root"
    elif level=="select students":
        print(Fore.YELLOW + "1." + Fore.WHITE + emoji.emojize(" :information_source:") + " info"         + Style.RESET_ALL)
        print(Fore.YELLOW + "2." + Fore.WHITE + emoji.emojize(" :plus:")               + " add course"   + Style.RESET_ALL)
        print(Fore.YELLOW + "3." + Fore.WHITE + emoji.emojize(" :wastebasket:")        + " delet course" + Style.RESET_ALL)
        print(Fore.YELLOW + "4." + Fore.WHITE + emoji.emojize(" :100:")                + " set score"    + Style.RESET_ALL)
        print(Fore.RED    + "0." + Fore.WHITE + emoji.emojize(" :back:")               + " back"         + Style.RESET_ALL)
        cmd=int(input())
        if cmd==1:
           sc1.selected_student.print_info()
        elif cmd==2:
            sc1.print_courses()
            course_id = int(input("Enter id to select: "))
            course_obj = Course(course_id, "", 0)
            if course_obj in sc1.courses:
                original = sc1.courses[sc1.courses.index(course_obj)]
                sc1.selected_student.add_course(original)
            else:
                print(Fore.RED + emoji.emojize("Course not found")+ Style.RESET_ALL)
        elif cmd==3:
            print("\tID\tName\tUnits\tScore")
            for course in sc1.selected_student.courses:
                print(f"  id:{course.id}, name:{course.name}, units:{course.units}")
            course_id = int(input("Enter id to remove: "))
            sc1.selected_student.remove_course(course_id)
        elif cmd==4:
            for course in sc1.selected_student.courses:
                new_score = float(input(f"  {course.name}: "))
                sc1.selected_student.set_score(course.id, new_score)
            
        elif cmd==0:
            sc1.selected_student = None
            level="students"
    elif level=="teachers":
        print(Fore.YELLOW + "1." + Fore.WHITE + emoji.emojize(" :clipboard:")   + " show teachers"   + Style.RESET_ALL)
        print(Fore.YELLOW + "2." + Fore.WHITE + emoji.emojize(" :plus:")        + " add teachers"    + Style.RESET_ALL)
        print(Fore.YELLOW + "3." + Fore.WHITE + emoji.emojize(" :pencil2:")     + " edit teachers"   + Style.RESET_ALL)
        print(Fore.YELLOW + "4." + Fore.WHITE + emoji.emojize(" :wastebasket:") + " delete teachers" + Style.RESET_ALL)
        print(Fore.YELLOW + "5." + Fore.WHITE + emoji.emojize(" :dart:")        + " select teachers" + Style.RESET_ALL)
        print(Fore.RED    + "0." + Fore.WHITE + emoji.emojize(" :back:")        + " back"            + Style.RESET_ALL)
        cmd=int(input())
        if cmd==1:
            sc1.print_teachers()
        elif cmd==2:
            id = int(input("id:"))
            name= str(input("name:"))
            family= str(input("family:"))
            grade= str(input("grade:"))
            sc1.add_teacher(Teacher(id, name, family, grade))
        elif cmd==3:
            id = int(input("id:"))
            name= str(input("new_name:"))
            family= str(input("new_family:"))
            grade= str(input("new_grade:"))
            sc1.edit_teacher(Teacher(id, name, family,grade))
        elif cmd==4:
            sc1.print_teachers()
            id=int(input("id:"))
            sc1.remove_teacher(id)
        elif cmd==5:
            sc1.print_teachers()
            teacher_id = int(input("Enter id too select:"))
            teacher_object = Teacher(teacher_id, "", "","")
            if teacher_object in sc1.teachers:
                index_t = sc1.teachers.index(teacher_object)
                sc1.selected_teacher = sc1.teachers[index_t]
                print(Fore.GREEN + emoji.emojize(f"Teacher {sc1.selected_teacher.name} {sc1.selected_teacher.family} selected.:check_mark:")+ Style.RESET_ALL)
            else:
                print(Fore.RED + emoji.emojize("Teacher not found.:check_mark:")+ Style.RESET_ALL)
                level = "teachers"
            level="select teachers"
        elif cmd==0:
            level="root"
    elif level=="select teachers":
        print(Fore.YELLOW + "1." + Fore.WHITE + emoji.emojize(" :information_source:") + " info"         + Style.RESET_ALL)
        print(Fore.YELLOW + "2." + Fore.WHITE + emoji.emojize(" :plus:")               + " add course"   + Style.RESET_ALL)
        print(Fore.YELLOW + "3." + Fore.WHITE + emoji.emojize(" :wastebasket:")        + " delet course" + Style.RESET_ALL)
        print(Fore.RED    + "0." + Fore.WHITE + emoji.emojize(" :back:")               + " back"         + Style.RESET_ALL)
        cmd=int(input())
        if cmd==1:
            sc1.selected_teacher.print_info()
        elif cmd==2:
            sc1.print_courses()
            course_id = int(input("Enter id to select: "))
            course_obj = Course(course_id, "", 0)
            if course_obj in sc1.courses:
                original = sc1.courses[sc1.courses.index(course_obj)]
                sc1.selected_teacher.add_course(original)
            else:
                print(Fore.RED + emoji.emojize("Course not found.:cross_mark:")+ Style.RESET_ALL)
        elif cmd==3:
            print("\tID\tName\tUnits\tScore")
            for course in sc1.selected_teacher.courses:
                print(f"  id:{course.id}, name:{course.name}, units:{course.units}")
            course_id = int(input("Enter id to remove: "))
            sc1.selected_teacher.remove_course(course_id)
    
        elif cmd==0:
            sc1.selected_teacher = None
            level="teachers"
        
    elif level=="courses":
        print(Fore.YELLOW + "1." + Fore.WHITE + emoji.emojize(" :clipboard:")   + " show courses"   + Style.RESET_ALL)
        print(Fore.YELLOW + "2." + Fore.WHITE + emoji.emojize(" :plus:")        + " add courses"    + Style.RESET_ALL)
        print(Fore.YELLOW + "3." + Fore.WHITE + emoji.emojize(" :pencil2:")     + " edit courses"   + Style.RESET_ALL)
        print(Fore.YELLOW + "4." + Fore.WHITE + emoji.emojize(" :wastebasket:") + " delete courses" + Style.RESET_ALL)
        print(Fore.RED    + "0." + Fore.WHITE + emoji.emojize(" :back:")        + " back"           + Style.RESET_ALL)
        cmd=int(input())
        if cmd==1:
            sc1.print_courses()
        elif cmd==2:
            id = int(input("id:"))
            name= str(input("name:"))
            units= int(input("units:"))
            sc1.add_course(Course(id, name, units))
            
        elif cmd==3:
            id = int(input("id:"))
            name= str(input("new_name:"))
            units= str(input("new_units:"))
            sc1.edit_course(Course(id, name, units)) 
        elif cmd==4:
            id=int(input("id:"))
            sc1.remove_course(id)
        elif cmd==0:
            level="root"

    elif level=="classrooms":
        print(Fore.YELLOW + "1." + Fore.WHITE + emoji.emojize(" :clipboard:")   + " show classrooms"   + Style.RESET_ALL)
        print(Fore.YELLOW + "2." + Fore.WHITE + emoji.emojize(" :plus:")        + " add classrooms"    + Style.RESET_ALL)
        print(Fore.YELLOW + "3." + Fore.WHITE + emoji.emojize(" :pencil2:")     + " edit classrooms"   + Style.RESET_ALL)
        print(Fore.YELLOW + "4." + Fore.WHITE + emoji.emojize(" :wastebasket:") + " delete classrooms" + Style.RESET_ALL)
        print(Fore.YELLOW + "5." + Fore.WHITE + emoji.emojize(" :dart:")        + " select classrooms" + Style.RESET_ALL)
        print(Fore.RED    + "0." + Fore.WHITE + emoji.emojize(" :back:")        + " back"             + Style.RESET_ALL)
        cmd=int(input())
        if cmd==1:
            print("classrooms:")
            print("\tID\tClass\tCourse\tTeacher\tstudents count")
            for cls in sc1.classrooms:
                print(f"\t{cls.id}\t{cls.name}\t{cls.teacher.name}\t{len(cls.students)}")

        elif cmd==2:
            id = int(input("id:"))
            name= str(input("name:"))
            sc1.print_courses()
            course_id=int(input("Enter id too select:"))
            for teacher in sc1.teachers:
                if any(course.id == course_id for course in teacher.courses):
                    print(teacher)
            teacher_id=int(input("Enter id too select:"))
            while True:
                students_classroom=[]
                for student in sc1.students:
                    if any(course.score < 10 and course.id == course_id for course in student.courses):
                        print(student.id)
                student_id=int(input("Enter id too select student:"))
                if student_id==0:
                    break
                elif student_id!=0:
                     student_classrooms= Student(student_id, "", "")
                     original_student = sc1.students[sc1.students.index(student_classrooms)]
                     new_student = Student(original_student.id, original_student.name, original_student.family)
                     students_classroom.append(new_student)

                    
            c1=Classroom(id,name)
            course_classrooms= Course(course_id, "", 0)
            original = sc1.courses[sc1.courses.index(course_classrooms)]
            new_course = Course(original.id, original.name, original.units)
            c1.course=new_course
            

            teacher_classrooms = Teacher(teacher_id, "", "","")
            original_teacher=sc1.teachers[sc1.teachers.index(teacher_classrooms)]
            new_teacher = Teacher(original_teacher.id, original_teacher.name, original_teacher.family, original_teacher.grade)
            c1.teacher=new_teacher
            for sc2 in students_classroom:
                c1.students.append(sc2)
            
        elif cmd==3:
            id = int(input("id:"))
            name= str(input("new_name:"))
            sc1.edit_classroom(Classroom(id,name))
        elif cmd==4:
            id=int(input("id:"))
            sc1.remove_classroom(id)
        elif cmd==5:
            sc1.print_classroom()
            classroom_id = int(input("Enter id too select:"))
            classroom_object = Classroom(classroom_id, "")
            if classroom_object in sc1.classrooms:
                index_c = sc1.classrooms.index(classroom_object)
                sc1.selected_classroom = sc1.classrooms[index_c]
                print(Fore.GREEN + emoji.emojize(f"Classroom {sc1.selected_classroom.name}  selected.:check_mark:"))
            else:
                print(Fore.RED + emoji.emojize("Classroom not found.:cross_mark:")+ Style.RESET_ALL)
                level = "classrooms"
            level="select classroom"
        elif cmd==0:
            level="root"
    elif level=="select classroom":
        print(Fore.YELLOW + "1." + Fore.WHITE + emoji.emojize(" :information_source:")      + " info"           + Style.RESET_ALL)
        print(Fore.YELLOW + "2." + Fore.WHITE + emoji.emojize(" :arrows_counterclockwise:") + " change course"  + Style.RESET_ALL)
        print(Fore.YELLOW + "3." + Fore.WHITE + emoji.emojize(" :repeat:")                  + " change teacher" + Style.RESET_ALL)
        print(Fore.YELLOW + "4." + Fore.WHITE + emoji.emojize(" :plus:")                    + " add student"    + Style.RESET_ALL)
        print(Fore.YELLOW + "5." + Fore.WHITE + emoji.emojize(" :heavy_minus_sign:")        + " remove student" + Style.RESET_ALL)
        print(Fore.RED    + "0." + Fore.WHITE + emoji.emojize(" :back:")                    + " back"           + Style.RESET_ALL)
        cmd=int(input())

        cls = sc1.selected_classroom

        if cmd==1:
           sc1.selected_classroom.print_info()
        elif cmd==2:
            selected = sc1.selected_classroom
            selected_course =selected.course
            print(Fore.RED + emoji.emojize(f" This class allready have  {selected.course.name} this course.:cross_mark:")+ Style.RESET_ALL )
            print(sc1.print_courses())
            new_course_id = int(input("Enter new course ID: "))
            new_course = None
            course_temp=Course(new_course_id, "", 0)
            original_courses=sc1.courses[sc1.courses.index(course_temp)]
            new_course = Course(original_courses.id, original_courses.name, original_courses.units)

            current_teacher = selected.teacher
            selected.course = new_course 
            if current_teacher is not None and new_course in current_teacher.courses:
                print(Fore.GREEN + emoji.emojize(f"Classroom course changed to {new_course.name} (ID: {new_course.id}).:check_mark:")+ Style.RESET_ALL)
            else:
                selected.teacher = None 
                print(Fore.RED + emoji.emojize("The current teacher does not teach this course. Teacher has been removed.:cross_mark:")+ Style.RESET_ALL)

            students_kept = []
            for student in selected.students:
                if new_course in student.courses:
                    students_kept.append(student)
                else:
                    print(Fore.RED + emoji.emojize(f"Student ID {student.id} removed (does not have this course).:cross_mark:")+ Style.RESET_ALL)
            selected.students = students_kept

        elif cmd==3:
            selected_course = sc1.selected_classroom.course
            print(Fore.RED + emoji.emojize(f" teacher {sc1.selected_classroom.teacher.id} allready have this class.:cross_mark:")+ Style.RESET_ALL)
            matching_teachers = [t for t in sc1.teachers if selected_course in t.courses]
            if matching_teachers:
                for t in matching_teachers:
                    print(f"ID: {t.id} | Name: {t.name} {t.family}")
            else:
                print(Fore.RED + emoji.emojize("No teachers found for this course.:cross_mark:")+ Style.RESET_ALL)

            for t in sc1.teachers:
                if cls.course in t.courses:
                    print(f"ID: {t.id} | Name: {t.name} {t.family}")
            teacher_id = int(input("Enter new teacher id: "))
            teacher_obj = Teacher(teacher_id, "", "", "")
            if teacher_obj in sc1.teachers:
                original = sc1.teachers[sc1.teachers.index(teacher_obj)]
                cls.change_teacher(original)
            else:
                print(Fore.RED + emoji.emojize("Teacher not found.:cross_mark:")+ Style.RESET_ALL)

        elif cmd==4:
            for s in sc1.students:
                if s not in cls.students and any(
                    c.id == cls.course.id and c.score < 10 for c in s.courses
                ):
                    print(s)
            student_id = int(input("Enter student id to add: "))
            student_obj = Student(student_id, "", "")
            if student_obj in sc1.students:
                original = sc1.students[sc1.students.index(student_obj)]
                cls.add_student(original)
            else:
                print(Fore.RED + emoji.emojize("Student not found")+ Style.RESET_ALL)

        elif cmd==5:
            cls=sc1.selected_classroom
            for s in cls.students:
                print(s)
            student_id = int(input("Enter student id to remove:"))
            cls.remove_student(student_id)
            
        elif cmd==0:
            level=" select classroom"
        

        
