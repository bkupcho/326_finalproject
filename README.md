# 326_finalproject
## Purpose of Files in Repository:

* simple_course_data -> this is the only Python file required to run our program. By running this program, this file with create a course database (which is the crux of our project) based on the respective csv's (which'll be command line arguments).
* class1.csv -> Contains information about a particular course, along with students in that course. Uses ExtendsClass's random data generator to obtain random names.
* class2.csv -> Contains information about a particular course, along with students in that course. Uses ExtendsClass's random data generator to obtain random names.
* class3.csv -> Contains information about a particular course, along with students in that course. Uses ExtendsClass's random data generator to obtain random names.
* teachers.csv -> Contains information about all the teachers of a course (including TAs). Uses ExtendsClass's random data generator to obtain random names.
* oh -> 

## How to Run Program from the Command Line:

To run the program from the command line, type the following into the terminal (WITHOUT the apostrophes): 

'python simple_course_data.py class1.csv class2.csv class3.csv teachers.csv oh_waitlist.csv'

Make sure you have the CSV's and the Python file in the same folder. 

## How to Interpret the Output of this Program:

This program creates a 'Database' object for a particular course being taught at a University. This course has multiple professors (multiple classes for the same course, in essence), and each class' data can be compared with the other classes. Within this database, the the user can access information regarding each Professor, TA, and Student. Students information is stored in a 'Student' object, whereas professor and TA information is stored within a 'Teacher' object. To store these objects, the overarching 'DataBase' object keeps a dictionary of 'Student' objects (whose name are keys) and a list of 'Teacher' objects as attributes of the class. To initialize the 'Student' and 'Teacher' objects, CSV files are read in.

Once this data is stored in our 'DataBase', we can do all sorts of things with this data!!! For the scope of this project, we only demonstrate some of the things you can do. When running this program, the user will see in the standard output the the results of the methods each contributor made. (Those being Derek, Brittany, Elliott, and Shreeya). To understand better how those results we're printed, inspect the Python program and refer to the Docstrings within. Each method showcases some sort of Python functionality. There is overlap for sure, however to makes things clear:

* Derek -> gets credit for **With Statements**, **Regular Expressions**
* Brittany -> gets credit for **Concatenating Pandas DataFrames**, **Comprehensions**
* Elliott -> gets credit for **Magic Methods**, **Conditional Expressions**
* Shreeya -> gets credit for **F-Strings**, **Seaborn Plots**

## Primary Authors: Who Wrote What?

* Derek ->
  * 'DataBase' class
  * 'DataBase' __str__()
  * update_oh_queue()
  * filter_by_oh_capacity()
  * main() / parse_args()
* Elliott ->
  * 'Teacher' __str__()
  * 'Student' __str__()
  * 'Student' __add__()
* Brittany ->
  * concatenate()
  * fletter_sort()
* Shreeya ->
  * plot()
  * person_info()
