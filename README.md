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