import model 
from model import Course , Student , Teacher , School , Classroom
import json
import emoji
from colorama import Fore , Back , Style , init
init(autoreset=True)
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
        print(Fore.YELLOW + "2." + Fore.WHITE + emoji.emojize(" :plus: ")        + " add students"    + Style.RESET_ALL)
        print(Fore.YELLOW + "3." + Fore.WHITE + emoji.emojize(" :keyboard: ")     + " edit students"   + Style.RESET_ALL)
        print(Fore.YELLOW + "4." + Fore.WHITE + emoji.emojize(" :wastebasket: ") + " delete students" + Style.RESET_ALL)
        print(Fore.YELLOW + "5." + Fore.WHITE + emoji.emojize(" :backhand_index_pointing_up: ")   +  " select students" + Style.RESET_ALL)
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
        print(Fore.YELLOW + "4." + Fore.WHITE + emoji.emojize(" :hundred_points:")                + " set score"    + Style.RESET_ALL)
        print(Fore.RED    + "0." + Fore.WHITE + emoji.emojize(" :BACK_arrow: ")               + " back"         + Style.RESET_ALL)
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
        print(Fore.YELLOW + "3." + Fore.WHITE + emoji.emojize(" :keyboard: ")     + " edit teachers"   + Style.RESET_ALL)
        print(Fore.YELLOW + "4." + Fore.WHITE + emoji.emojize(" :wastebasket: ") + " delete teachers" + Style.RESET_ALL)
        print(Fore.YELLOW + "5." + Fore.WHITE + emoji.emojize(" :backhand_index_pointing_up: ")        + " select teachers" + Style.RESET_ALL)
        print(Fore.RED    + "0." + Fore.WHITE + emoji.emojize(" :BACK_arrow:")        + " back"            + Style.RESET_ALL)
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
        print(Fore.RED    + "0." + Fore.WHITE + emoji.emojize(" :BACK_arrow:")               + " back"         + Style.RESET_ALL)
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
        print(Fore.YELLOW + "3." + Fore.WHITE + emoji.emojize(" :keyboard: ")     + " edit courses"   + Style.RESET_ALL)
        print(Fore.YELLOW + "4." + Fore.WHITE + emoji.emojize(" :wastebasket: ") + " delete courses" + Style.RESET_ALL)
        print(Fore.RED    + "0." + Fore.WHITE + emoji.emojize(" :BACK_arrow:")        + " back"           + Style.RESET_ALL)
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
        print(Fore.YELLOW + "1." + Fore.WHITE + emoji.emojize(" :clipboard: ")   + " show classrooms"   + Style.RESET_ALL)
        print(Fore.YELLOW + "2." + Fore.WHITE + emoji.emojize(" :plus: ")        + " add classrooms"    + Style.RESET_ALL)
        print(Fore.YELLOW + "3." + Fore.WHITE + emoji.emojize(" :keyboard: ")     + " edit classrooms"   + Style.RESET_ALL)
        print(Fore.YELLOW + "4." + Fore.WHITE + emoji.emojize(" :wastebasket: ") + " delete classrooms" + Style.RESET_ALL)
        print(Fore.YELLOW + "5." + Fore.WHITE + emoji.emojize(" :backhand_index_pointing_up: ")        + " select classrooms" + Style.RESET_ALL)
        print(Fore.RED    + "0." + Fore.WHITE + emoji.emojize(" :BACK_arrow:")        + " back"             + Style.RESET_ALL)
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
        print(Fore.YELLOW + "2." + Fore.WHITE + emoji.emojize(" :repeat_button:") + " change course"  + Style.RESET_ALL)
        print(Fore.YELLOW + "3." + Fore.WHITE + emoji.emojize(" :repeat_button:")                  + " change teacher" + Style.RESET_ALL)
        print(Fore.YELLOW + "4." + Fore.WHITE + emoji.emojize(" :plus:")                    + " add student"    + Style.RESET_ALL)
        print(Fore.YELLOW + "5." + Fore.WHITE + emoji.emojize(" :minus:")        + " remove student" + Style.RESET_ALL)
        print(Fore.RED    + "0." + Fore.WHITE + emoji.emojize(" :BACK_arrow:")                    + " back"           + Style.RESET_ALL)
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
        

        
