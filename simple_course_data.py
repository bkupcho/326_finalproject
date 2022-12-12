from argparse import ArgumentParser
import re
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataBase:
    """ This class contains information abouts the students, professors, and 
            TAs for a particular course at the University of Maryland. None of
            the information is real per se, however the data represents data
            that you may see associated with a course in rea life. 
            
            Attributes:
                course_data (Dictionary of 'Students'): The key of this
                    dictionary is a student's first and last name as a String,
                    like "firstname lastname". The value of each key is a 
                    Student object associated with the student named in the key.
                teacher_data (List of 'Teacher'): Represents a list of 'Teacher' 
                    objects. 
    """
    
    def __init__(self, c1, c2, c3, t1):
        """ This method initializes the 'DataBase' class.
        
        Args:
            self ('DataBase'): The object calling the method.
            c1 (str): represents csv to be read in for course 1.
            c2 (str): represents csv to be read in for course 2.
            c3 (str): represents csv to be read in for course 3.
            t1 (str): represents csv to be read in for course 4.
            
        Side Effects:
            Initializes the attributes 'course-data' and 'teacher_data'
            by reading in csv's and created new 'Student'/'Teacher' objects
            for each line.
        """
        
        df = concatenate(c1,c2,c3).reset_index()
        self.course_data = {}
        self.teacher_data = []
    
        for i in range(len(df)): 
                key = df.loc[i, "first_name"] + " " + df.loc[i, "last_name"]
                self.course_data[key] = Student(df.loc[i, "first_name"],
                df.loc[i, "last_name"],df.loc[i, "year"],
                df.loc[i, "course_grade"],df.loc[i, "professor"],
                df.loc[i, "home_state"],df.loc[i, "hr_week_studying"])
        
        with open(t1, "r", encoding="utf-8") as f:
            for line in f: 
               matched_obj = re.search(r"(\w+),(\w+),(\w+),(\w+),(\w+)", line)
               self.teacher_data.append(Teacher(matched_obj.group(1),
                matched_obj.group(2), matched_obj.group(3), matched_obj.group(4),
                matched_obj.group(5)))
            del self.teacher_data[0]
            
    def __str__(self):
        """ This method prints an informal string representation of the 'Database'
                object.
                
            Args:
                self ('DataBase'): The object calling the method.
                
            Side Effects:
                Prints information about the calling 'DataBase' object (and
                the 'Students' and 'Teachers' within it) to stdout.
            
            Returns (str): Returns the empty string, as only data is being 
                printed to stdout.
        """
        
        for teacher in self.teacher_data:
            print(f"{teacher.name} has {int(teacher.office_hr_capacity) - len(teacher.queue)} spots open")
            
        for student in self.course_data:
            print(f"{student} has a gpa of {self.course_data[student].course_grade}")
            
        return ""
    
class Teacher:
    """ This class reprsents a specific teacher of the course the overarching
            'DataBase' represents. 
            
        Attributes:
            name(str): represents a teachers first and last names.
            position(str): denotes whether the teacher is a TA or Professor.
            years_of_experience(int): how many years of experience the teacher
                has
            office_hr_capacity(int): how many office hours does the teacher have
            queue(list of 'Students'): represents a list of students waiting in
                the office hour queue.
    """
    
    def __init__(self, fname, lname, position, years_of_experience, office_hr_capacity):
        """ This method initializes the 'Teacher' class.
        
        Args:
            self ('Teacher'): The object calling the method.
            fname (str): represents the teachers first name.
            lname (str): represents the teachers last name.
            years_of_experience(int): how many years of experience the teacher
                has
            office_hr_capacity(int): how many office hours does the teacher have
            queue(list of 'Students'): represents a list of students waiting in
                the office hour queue.
            
        Side Effects:
            Initializes the attributes of the class by reading the arguments 
            passed in, or by giving them default values
        """
        
        self.name = fname + " " + lname
        self.position = position
        self.years_of_experience =years_of_experience
        self.office_hr_capacity = office_hr_capacity
        self.queue = []
        
    def update_oh_queue(self, filepath, database):
        """ This method updates a 'Teachers' office hour attribute 'queue', 
                specifically by adding 'Student' objects to the 'queue' based
                on a csv being read in. 
                
                Args:
                    self ('Teacher'): The object calling the method.
                    filepath (str): The csv being read in, which contains the
                        first and last names of the students.
                    database ('DataBase'): The 'DataBase' object the method uses
                        to check whether the student on the list is a part of or
                        not.
        
                Side Effects:
                    Updates(appends) 'Student' objects to the office hour queue.
        """
                
        with open(filepath, "r", encoding="utf-8") as f:
             for line in f: 
                 matched_obj = re.search(r"(\w+),(\w+)", line)
                 name = matched_obj.group(1) + " " + matched_obj.group(2)
                 
                 if name in database.course_data.keys():
                    self.queue.append(database.course_data[name])
                
    def __str__(self):
        """Returns an f-string that correlates with the conditional expression stating whether or not a teacher is tenured."""
        exp = self.years_of_experience
        prof = self.name
        
        print(f'{prof} has taught for {exp} years and is tenured') \
            if int(exp) > 4 else print(f'{prof} has taught for \
                {exp} years and is not tenured yet.')           

        return ""
    
class Student:
    """Class representing a student and their information.

    Attributes:
        name (str): student's first and last name.
        year (str): student's year at college.
        course_grade (int): numeric grade point average of the student.
        professor (str): student's course professor.
        home_state (str): student's home state.
        hr_week_studying (int): hours a week student spends for the particular
            course.
    """
    
    def __init__(self, fname, lname, year, course_grade, professor,
                home_state, hr_week_studying):
        """ This method initializes the 'Teacher' class.
        
        Args:
            fname (str): student's first name.
            lname (str): student's last name.
            year (str): student's year at college.
            course_grade (int): numeric grade point average of the student.
            professor (str): student's course professor.
            home_state (str): student's home state.
            hr_week_studying (int): hours a week student spends for the 
            particular course.
            
        Side Effects:
            Initializes the attributes of the class by reading the arguments 
            passed in, or by giving them default values.
        """
        self.name = fname + " " + lname
        self.year = year
        self.course_grade = course_grade
        self.professor = professor
        self.home_state = home_state
        self.hr_week_studying = hr_week_studying
    
    def __add__(self, other):
        """Finds the average course grade of two students."""
        return (self.course_grade + other.course_grade) / 2
    
    def __str__(self):
        """Returns an f-string that correlates with a conditional expression stating whether or not a student made the Dean's list."""
        gpa = self.course_grade
        student = self.name
        print(f"{student} is on the Dean's list") if (gpa >= 3) else \
            (print(f"{student} did not make the Dean's list"))
        
        return ""    
# Brittany
def concatenate(f1,f2,f3):
    """concatenates the seprate csv files into one dataframe.
        args:
            f1 (str): a path to the first file
            f2 (str): a path to the second file
            f3 (str): a path to the third file
        returns:
            a dataframe of all the class sections.
    """
    df1 = pd.read_csv(f1)
    df2 = pd.read_csv(f2)
    df3 = pd.read_csv(f3)
    allnames = pd.concat([df1, df2, df3])
    return allnames.drop('Unnamed: 7', axis = 1)
    
def fletter_sort(allnames, colname, letter):
    """Creates a filtering system based off the first letter of the words 
             in a column using a list comprehension and f strings.
        
          args:
            allnames: a dataframe that compiles the 3 class sections
            colname (str): the name of a column in the allnames dataframe
            letter (str): a capital letter that represents the first letter of 
                   the items in a column that the user wants to filter by.
        
          returns:
            the frquency of the results and a list of names begins with the 
                   given letter.
    """
    wordlist = allnames[colname].to_list()
    fletter = [x for x in wordlist if letter in x[0]]
    return f"frequency of {letter} in {colname} :{len(fletter)}; results:{fletter}"
    
def plot(allnames):
    """ Uses seaborn implot to display the correlation between hr_week_studying 
        and course_grade based on each teacher
    
         Args:
            allnames (str): dataframe of all 3 csv files
            
         Returns:
            a seaborn implot
    """
    sns.lmplot( x = "hr_week_studying", y = "course_grade" , data = allnames, hue = "professor")

def person_info(allnames, name, lname):
        """Displays basic information about an individual.

        Args:
            allnames (str): dataframe of all csv files
            name (str): individual's first and last name
            lname (str): individual's last name
            
        Side Effects:
            prints f-string and row showing a selected person's basic information. 
        """	
     
        print(f"This is {name}'s personal information:")
        print(allnames.loc[allnames['last_name'] == lname])

def filter_by_oh_capacity(index, original_list, new_list, n):
        """ This method filters teachers by their office hours capacity. The 
        method does so in a recursive fashion. 
        
        Args:
            index(int): When first called, this arguments has the value of 0.
                In order to iterate through the 'original_list' of teachers, 
                this 'index' will be incremented by 1 for each iteration. 
            original_list(list of 'Teachers'): A list of teacher objects (like
                DataBase.teacher_data) is passed in, as this is the list the 
                method will recursively filter and extract data from.
            new_list(list of 'Teachers'): When first passed in the method, the
                list is empty. This list will serve as an accumulator. With
                each recursive call, this list may have a 'Teacher' object 
                appended to it or not, depending on whether the current
                'Teacher' object in 'original_list' (being accessed by 'index')
                meets a specified criteria.
            n (int): This is the criteria mentioned above. This is the number 
                the method makes decisions by. 
                
        Returns (list of 'Teachers'): This list is initially empty, and will
            possibly be built upon based on the arguments being passed in. This
            list represents all the teachers that have a GREATER number of
            office hours then the number 'n' being passed in.
        """
        
        if (isinstance(new_list, list)):
            if index == len(original_list):
                return new_list
            else:
                if (int(original_list[index].office_hr_capacity)< n):
                    return filter_by_oh_capacity(index + 1, original_list, new_list, n)
                else:
                    new_list.append(original_list[index])
                    return filter_by_oh_capacity(index + 1, original_list, new_list, n)
                        
def main(class1, class2, class3, teachers, oh_waitlist):
    # DataBase Creation -> Derek
    x = DataBase(class1, class2, class3, teachers)
    
    # DataFrames / Using Pandas / List Comprehensions -> Brittany
    print("Demonstration of Brittany's Methods:")
    df = concatenate(class1, class2, class3).reset_index()
    print(df)
    print(fletter_sort(df,"first_name","S"))
    print('\n')
    
    # Magic Methods / Conditional Expressions -> Elliott
    print("Demonstration of Elliott's Methods:")
    s1 = Student("person","one", "Freshman", 3.7, "idk", "MD", 10)
    s2 = Student("person","two", "Freshman", 2.3, "idk", "MD", 10)
    print(s1 + s2)
    print('\n')
    print(str(s1))
    print(str(s2))
    
    # With statements / Regular Expressions -> Derek
    print("Demonstration of Derek's Methods:\n")
    t1 = Teacher("teacher","one", "Professor", 10, 12)
    print("Queue is Empty:")
    print(t1.queue)
    print('\n')
    print("Updated Queue:")
    t1.update_oh_queue(oh_waitlist, x)
    for i in t1.queue:
        print(i.name)
    print('\n')
    print("Finding Teachers who have MORE than 5 office hours (INCLUSIVE).\n")
    filter_t = filter_by_oh_capacity(0, x.teacher_data, [], 5)
    for i in filter_t:
        print(i.name + " " + i.office_hr_capacity)

    # F-Strings / Seaborn Plot -> Shreeya
    print('\n')
    print("Demonstration of Shreeya's Methods:\n")
    print(person_info(df, "Suzette Jillane", "Jillane"))
    plot(df)
    plt.show()
    
    
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("class1", help="file containing data for course 1")
    parser.add_argument("class2", help="file containing data for course 2")
    parser.add_argument("class3", help="file containing data for course 3")
    parser.add_argument("teachers", help="file containing teacher data")
    parser.add_argument("oh_waitlist", help="file containing students on oh waitlist")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.class1, args.class2, args.class3, args.teachers, args.oh_waitlist)
