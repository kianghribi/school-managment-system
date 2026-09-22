## School Management System

This project is a  simple school management system.It allows you add, edit, delete and search for students, teachers, courses, and classrooms.All the data is stored in five classes: `Course`, `Student`, `Teacher`, `Classroom`, and `School`.`School` is the main of all this program.

This project saves everything in JSON files. The `load_data()` method reads everything from `dataa.json` and recreates the objects, and `save_data()` writes the current state to `saves.json`. So you can work, save, and pick up where you left off later. We also put some rules in this program to keep the data consistent: for example, if a course or teacher is already used in a classroom, you can't delete it. Or a student can only be added to a classroom if they've scored less than 10 in that course — just like getting a failing grade and needing to retake it in a real school.

In the end, this program is a good choice for anyone who wants to learning Python and object-oriented programming. It covers  operator overloading like `__eq__` and `__str__`, class composition, and working with JSON files.  this program helps you understand  where to correctly use conditional statements and loops,and allows you tp learn the inner workings of a real program.

## Installation

Getting this project up and running is super easy. Just follow these steps:

**1. Clone the repository**

```bash
git clone https://github.com/your-username/school-management-system.git
cd school-management-system
```

**2. Make sure you have Python installed**

This project works with Python 3.7 or higher. You can check your version with:

```bash
python --version
```

**3. Run the program**

There's nothing to install — no extra libraries, no pip, nothing! Just run:

```bash
python main.py
```

**4. That's it!** 🎉

Now you can use this program.

## Output

Here's a quick look at how the program actually looks when you run it. Below is a sample of the main menu, a list of students, and a student's full info:

**Main menu**

```
1.students
2.teachers
3.courses
4.classrooms
5.save
0.exit
```

**Students menu**

```
1.show students
2.add students
3.edit students
4.delete students
5.select students
0.back
```

**Showing all students**

```
id:2001, name:Ali, family:Rezai
id:2002, name:Reza, family:Alinia
id:2003, name:Ahmad, family:Hassani
```

**Student info (selected student)**

```
id:2001
name:Ali
family:Rezai
courses:
	ID	   Name	 Units	Score
	1001 	Math	3	18.0
	1002	Physics	2	15.5
	1003	Chemistry	3	9.0
```

**Classroom list**

```
classrooms:
	ID	Class	Course	Teacher	students count
	1	Class-A	Math	Mr. Hosseini	2
	2	Class-B	Physics	Mrs. Sadeghi	1
```

**After saving**

```
$ python main.py
...
5
```

```
(no output — data is written silently to saves.json)
```

## Structure

### Course

**Properties:**
- `id`: unique identifier of the course
- `name`: name of the course
- `units`: number of units (credits)
- `score`: score of the student in this course (used when a course is attached to a student)

**Methods:**
- `__init__(self, id, name, units)`: creates a new course with the given id, name, and units
- `__eq__(self, other)`: compares two courses by their id
- `__str__(self)`: returns a readable string representation of the course

---

### Student

**Properties:**
- `id`: unique identifier of the student
- `name`: first name
- `family`: last name
- `courses`: list of `Course` objects the student is enrolled in (each with its own score)

**Methods:**
- `__init__(self, id, name, family)`: creates a new student
- `__eq__(self, other)`: compares two students by their id
- `__str__(self)`: returns a readable string representation of the student
- `print_info(self)`: prints full details of the student and their courses
- `add_course(self, course)`: adds a course to the student's list (with a fresh score of 0.0)
- `remove_course(self, course_id)`: removes a course from the student's list by its id
- `set_score(self, course_id, score)`: sets the score of a specific course for this student

---

### Teacher

**Properties:**
- `id`: unique identifier of the teacher
- `name`: first name
- `family`: last name
- `grade`: academic rank or degree of the teacher
- `courses`: list of `Course` objects the teacher teaches

**Methods:**
- `__init__(self, id, name, family, grade)`: creates a new teacher
- `__eq__(self, other)`: compares two teachers by their id
- `__str__(self)`: returns a readable string representation of the teacher
- `print_info(self)`: prints full details of the teacher and their courses
- `add_course(self, course)`: adds a course to the teacher's list
- `remove_course(self, course_id)`: removes a course from the teacher's list by its id

---

### Classroom

**Properties:**
- `id`: unique identifier of the classroom
- `name`: name of the classroom
- `course`: the `Course` object taught in this classroom
- `teacher`: the `Teacher` object who teaches this classroom
- `students`: list of `Student` objects enrolled in this classroom

**Methods:**
- `__init__(self, id, name)`: creates a new classroom
- `__eq__(self, other)`: compares two classrooms by their id
- `__str__(self)`: returns a readable string representation of the classroom
- `print_info(self)`: prints full details of the classroom, including course, teacher, and students
- `change_course(self, new_course)`: changes the classroom's course; removes the teacher if they don't teach it, and removes students who don't have this course
- `change_teacher(self, new_teacher)`: changes the classroom's teacher (only if they actually teach the course)
- `add_student(self, student)`: adds a student to the classroom (only if they have a failing score below 10 in this course)
- `remove_student(self, student_id)`: removes a student from the classroom by their id

---

### School

**Properties:**
- `name`: name of the school
- `selected_student`: currently selected student (used in the interactive menu)
- `selected_teacher`: currently selected teacher
- `selected_classroom`: currently selected classroom
- `courses`: list of all `Course` objects in the school
- `teachers`: list of all `Teacher` objects
- `students`: list of all `Student` objects
- `classrooms`: list of all `Classroom` objects

**Methods:**
- `__init__(self, name)`: creates a new school
- `add_student(self, student)`: adds a student if not already present
- `add_course(self, course)`: adds a course if not already present
- `add_teacher(self, teacher)`: adds a teacher if not already present
- `add_classroom(self, id, name, course_id, teacher_id, student_ids)`: creates a new classroom with the given course, teacher, and students (with full validation)
- `load_data(self)`: loads all data from `dataa.json` and reconstructs the objects
- `save_data(self)`: saves the current state to `saves.json`
- `remove_student(self, id)`: removes a student by id if not used in any classroom
- `remove_course(self, id)`: removes a course by id if not used by any student, teacher, or classroom
- `remove_teacher(self, id)`: removes a teacher by id if not assigned to any classroom
- `remove_classroom(self, id)`: removes a classroom by id
- `edit_student(self, student)`: updates an existing student's name and family
- `edit_teacher(self, teacher)`: updates an existing teacher's name, family, and grade
- `edit_course(self, course)`: updates an existing course's name and units
- `edit_classroom(self, classroom)`: updates an existing classroom's name
- `print_students(self)`: prints all students
- `print_courses(self)`: prints all courses
- `print_teachers(self)`: prints all teachers
- `print_classroom(self)`: prints all classrooms