import json
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
            print("The student already exist")
        else:
            self.students.append(student)
            print("student added sucssefully")
    def add_course (self,course:Course):
        if course in self.courses:
            print("The course already exist")
            
        else:
            self.courses.append(course)
            print("course add succsesfully")
    def add_teacher (self,teacher:Teacher):
        if teacher in self.teachers:
            print("The teacher already exist")
        else:
            self.teachers.append(teacher)
            print("teacher added sucssefully")
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
            print("The student doesn't exist")
        elif any(True for cls in self.classrooms for s in cls.students if s.id == id):
            print("This student is used in a classroom and cannot be removed.")
        else:
            self.students.remove(student_id)
            print("Student removed successfully")
    def remove_course(self,id):
        course_id = Course(id,"",0)
        if course_id not in self.courses:
            print("the course doesn't exist")
        elif (any(c.id == id for student in self.students for c in student.courses) or
              any(c.id == id for teacher in self.teachers for c in teacher.courses) or
              any(cls.course is not None and cls.course.id == id for cls in self.classrooms)):
                print("This course is used in a student, teacher, or classroom and cannot be removed.")
        else:
            self.courses.remove(course_id)
            print("Course removed successfully")
    def remove_teacher(self, id):
        teacher_id = Teacher(id, "", "", "")
        if teacher_id not in self.teachers:
            print("The teacher doesn't exist")
        elif any(cls.teacher is not None and cls.teacher.id == id for cls in self.classrooms):
            print("This teacher is used in a classroom and cannot be removed.")
        else:
            self.teachers.remove(teacher_id)
            print("Teacher removed successfully")
            
    def remove_classroom(self,id):
        id_classroom = Classroom(id,"")
        if id_classroom in self.classrooms:
            self.classrooms.remove(id_classroom)
            print("classroom removed successfully")
        else:
            print("the classroom doesn't exist")

    def edit_student(self,student:Student):
        if student not in self.students:
            print("The student dosen't exist")
        else:
             index = self.students.index(student)  
             self.students[index].name = student.name
             self.students[index].family = student.family
             print("Student edited successfully")
    def edit_teacher(self,teacher:Teacher):
        if teacher not in self.teachers:
            print("The teacher doesn't exist")
        else:
             index = self.teachers.index(teacher)  
             self.teachers[index].name = teacher.name
             self.teachers[index].family = teacher.family
             self.teachers[index].grade = teacher.grade
             print("Student edited successfully")
    def edit_course(self,course:Course):
        if course not in self.courses:
            print("The student dosen't exist")
        else:
             index = self.courses.index(course)  
             self.courses[index].name = course.name
             self.courses[index].units = course.units
             print("Student edited successfully") 
    def edit_classroom(self,classroom:Classroom):
        if classroom not in self.classrooms:
            print("The classroom dosen't exist")
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
        print("1.students")
        print("2.teachers")
        print("3.courses")
        print("4.classrooms")
        print("5.save")
        print("0.exit")
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
        print("1.show students")
        print("2.add students")
        print("3.edit students")
        print("4.delete students")
        print("5.select students")
        print("0.back")
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
                print(f"Student {sc1.selected_student.name} {sc1.selected_student.family} selected.")
            else:
                print("Student not found")
                level = "students"
            level="select students"
        elif cmd==0:
            level="root"
    elif level=="select students":
        print("1.info")
        print("2.add course")
        print("3.delet course")
        print("4.set score")
        print("0.back")
        cmd=int(input())
        if cmd==1:
           sc1.selected_student.print_info()
        elif cmd==2:
            sc1.print_courses()
            course_id=int(input("Enter id too select:"))
            course_object=Course(course_id,"",0)
            if course_object in sc1.courses:
                index_c = sc1.courses.index(course_object)
                original_course = sc1.courses[index_c]
                new_course = Course(original_course.id, original_course.name, original_course.units)
                sc1.selected_student.courses.append(new_course)
                print(f"Course '{new_course.name}' added successfully.")
            else:
                print("Course not found")
        elif cmd==3:
            print("\tID\tName\tUnits\tScore")
            for course in sc1.selected_student.courses:
                print(f"  id:{course.id}, name:{course.name}, units:{course.units}, score:{course.score}")
            selected_course_id = int(input("Enter id too select:"))
            id_course = Course(selected_course_id,"",0)
            if id_course in sc1.selected_student.courses:
                sc1.selected_student.courses.remove(id_course)
                print("course removed successfully")
            else:
                print("the course doesn't exist")
        elif cmd==4:
            for course in sc1.selected_student.courses:
                new_score = int(input(f"  {course.name}: "))
                course.score = new_score
            print("scores added succsesfully")
            
        elif cmd==0:
            sc1.selected_student = None
            level="students"
    elif level=="teachers":
        print("1.show teachers")
        print("2.add teachers")
        print("3.edit teachers")
        print("4.delete teachers")
        print("5.select teachers")
        print("0.back")
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
                print(f"Teacher {sc1.selected_teacher.name} {sc1.selected_teacher.family} selected.")
            else:
                print("Teacher not found")
                level = "teachers"
            level="select teachers"
        elif cmd==0:
            level="root"
    elif level=="select teachers":
        print("1.info")
        print("2.add course")
        print("3.delet course")
        print("0.back")
        cmd=int(input())
        if cmd==1:
            sc1.selected_teacher.print_info()
        elif cmd==2:
            sc1.print_courses()
            course_id=int(input("Enter id too select:"))
            course_object=Course(course_id,"",0)
            if course_object in sc1.courses:
                index_c = sc1.courses.index(course_object)
                original_course = sc1.courses[index_c]
                new_course = Course(original_course.id, original_course.name, original_course.units)
                sc1.selected_teacher.courses.append(new_course)
                print(f"Course '{new_course.name}' added successfully.")
            else:
                print("Course not found") 
        elif cmd==3:
            print("\tID\tName\tUnits\tScore")
            for course in sc1.selected_teacher.courses:
                print(f"  id:{course.id}, name:{course.name}, units:{course.units}, score:{course.score}")
            selected_t_course_id = int(input("Enter id too select:"))
            id_course = Course(selected_t_course_id,"",0)
            if id_course in sc1.selected_teacher.courses:
                sc1.selected_teacher.courses.remove(id_course)
                print("course removed successfully")
            else:
                print("the course doesn't exist")
        elif cmd==4:
            pass
        elif cmd==0:
            sc1.selected_teacher = None
            level="teachers"
        
    elif level=="courses":
        print("1.show courses")
        print("2.add courses")
        print("3.edit courses")
        print("4.delete courses")
        print("0.back")
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
        print("1.show classrooms")
        print("2.add classrooms")
        print("3.edit classrooms")
        print("4.delete classrooms")
        print("5.select classrooms")
        print("0.back")
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
                print(f"Classroom {sc1.selected_classroom.name}  selected.")
            else:
                print("Classroom not found")
                level = "classrooms"
            level="select classroom"
        elif cmd==0:
            level="root"
    elif level=="select classroom":
        print("1.info")
        print("2.change course")
        print("3.change teacher")
        print("4.add student")
        print("5.remove student")
        print("0.back")
        cmd=int(input())
        if cmd==1:
           sc1.selected_classroom.print_info()
        elif cmd==2:
            selected = sc1.selected_classroom
            selected_course =selected.course
            print(f" This class allready have  {selected.course.name} this course") 
            print(sc1.print_courses())
            new_course_id = int(input("Enter new course ID: "))
            new_course = None
            course_temp=Course(new_course_id, "", 0)
            original_courses=sc1.courses[sc1.courses.index(course_temp)]
            new_course = Course(original_courses.id, original_courses.name, original_courses.units)

            current_teacher = selected.teacher
            selected.course = new_course 
            if current_teacher is not None and new_course in current_teacher.courses:
                print(f"Classroom course changed to {new_course.name} (ID: {new_course.id}).")
            else:
                selected.teacher = None 
                print("The current teacher does not teach this course. Teacher has been removed.")

            students_kept = []
            for student in selected.students:
                if new_course in student.courses:
                    students_kept.append(student)
                else:
                    print(f"Student ID {student.id} removed (does not have this course).")
            selected.students = students_kept

        elif cmd==3:
            selected_course = sc1.selected_classroom.course
            print(f" teacher {sc1.selected_classroom.teacher.id} allready have this class")
            matching_teachers = [t for t in sc1.teachers if selected_course in t.courses]
            if matching_teachers:
                for t in matching_teachers:
                    print(f"ID: {t.id} | Name: {t.name} {t.family}")
            else:
                print("No teachers found for this course.")
            new_teacher_id = int(input("Enter new teacher ID: "))
            new_teacher = None
            teacher_temp=Teacher(new_teacher_id, "", "","")
            original_teachers=sc1.teachers[sc1.teachers.index(teacher_temp)]
            new_teacher = Teacher(original_teachers.id, original_teachers.name, original_teachers.family, original_teachers.grade)
            
            if new_teacher:
                sc1.selected_classroom.teacher = new_teacher
                print(f"Classroom teacher changed to {new_teacher.name} {new_teacher.family}.")
            else:
                print("The entered teacher is not in the qualified list or does not exist.")

        elif cmd==4:
            cls = sc1.selected_classroom
            selected_course = cls.course
            valid_students=[]
            for s in sc1.students:
                if s not in cls.students:
                    for c in s.courses:
                        if c.id== selected_course.id and c.score < 10:
                            valid_students.append(s)
            for student in valid_students:
                print(student)
            new_add_student=(int(input("Enter ID too add:")))
            student_temp=Student(new_add_student, "", "")
            original_students=sc1.students[sc1.students.index(student_temp)]
            new_student = Student(original_students.id, original_students.name, original_students.family)
            if new_student:
                cls.students.append(new_student)
                print(f"new student {new_student.name} {new_student.family} added succssefully")
            else:
                print("New student not found")

        elif cmd==5:
            cls=sc1.selected_classroom
            for s in cls.students:
                print(s)
            student_remove_id=int(input("Enter ID too remove:"))
            student_temp=Student(student_remove_id, "", "")
            if student_temp in cls.students:
                cls.students.remove(student_temp)
                print(f"student {student_temp.name} {student_temp.family} remove successfully.")
            else:
                print("student not found")

            
        elif cmd==0:
            level=" select classroom"
        

        
