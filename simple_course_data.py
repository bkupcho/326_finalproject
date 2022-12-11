from argparse import ArgumentParser
import re
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import termplotlib as tpl

class DataBase:
    
    def __init__(self, c1, c2, c3, t1):
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
    
    # Derek
    def __str__(self):
        for teacher in self.teacher_data:
            print(f"{teacher.name} has {int(teacher.office_hr_capacity) - len(teacher.queue)} spots open")
            
        for student in self.course_data:
            print(f"{student} has a gpa of {self.course_data[student].course_grade}")
            
        return ""
            
class Teacher:
    
    def __init__(self, fname, lname, position, years_of_experience, office_hr_capacity):
        self.name = fname + " " + lname
        self.position = position
        self.years_of_experience = years_of_experience
        self.office_hr_capacity = office_hr_capacity
        self.queue = []
        
    # Derek    
    # Updates office hour queue attribute for Teacher
    # Does so by reading in a file, checking to see if those 
    # names exist as actual students in our database, if so, 
    # we append the associated student object to the 
    # queue list
    def update_oh_queue(self, filepath, database):
                
        with open(filepath, "r", encoding="utf-8") as f:
             for line in f: 
                 matched_obj = re.search(r"(\w+),(\w+)", line)
                 name = matched_obj.group(1) + " " + matched_obj.group(2)
                 
                 if name in database.course_data.keys():
                    self.queue.append(database.course_data[name])
          
    # Elliott      
    def __str__(self):
        exp = self.years_of_experience
        prof = self.name
        
        print(f'{prof} has taught for {exp} years and is tenured') \
            if exp > 4 else print(f'{prof} has taught for \
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
        self.name = fname + " " + lname
        self.year = year
        self.course_grade = course_grade
        self.professor = professor
        self.home_state = home_state
        self.hr_week_studying = hr_week_studying
    
    # Elliott
    def __add__(self, other):
        return (self.course_grade + other.course_grade) / 2
    
    # Elliott
    def __str__(self):
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

# Brittany
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
    
# Shreeya
def plot(allnames):
    """ Uses seaborn implot to display the correlation between hr_week_studying 
        and course_grade based on each teacher
    
         Args:
            allnames (str): dataframe of all 3 csv files
            
         Returns:
            a seaborn implot
    """
    sns.lmplot( x = "hr_week_studying", y = "course_grade" , data = allnames, hue = "professor")

# Shreeya
def person_info(allnames, name, lname):
        """Displays basic information about an individual.

        Args:
            allname (str): dataframe of 3 csv files
            name (str): individual's first and last name
            lname (str): individual's last name
    
        Returns:
            An f-string and row showing a selected person's basic information. 
        """	
     
        print(f"This is {name}'s personal information:")
        print(allnames.loc[allnames['last_name'] == lname])
        
# Derek
# This function filters teachers by the amount of office hours 
# they hold, does so in a recursive fashion. 'n' is the upper 
# bound. index starts at 0. original_list is list of teachers, 
# new_list is initially empty, the list serves as an 
# accumulator that will be returned.
def filter_by_oh_capacity(index, original_list, new_list, n):
    if index == len(original_list):
        return new_list
    else:
        if (int(original_list[index].office_hr_capacity) < n):
            if (isinstance(new_list, list)):
                new_list.append(original_list[index])
                return filter_by_oh_capacity(index + 1, original_list, 
                                new_list, n)
        else:
            return filter_by_oh_capacity(index + 1, 
                                    original_list, new_list, n)
    
def main(class1, class2, class3, teachers, oh_waitlist):
    # Brittany
    x = DataBase(class1, class2, class3, teachers)
    df = concatenate(class1, class2, class3).reset_index()
    #print(df)
    #print(fletter_sort(df,"first_name","S"))
    
    # Elliott
    s1 = Student("person","one", "Freshman", 3.7, "prof 2", "MD", 10)
    s2 = Student("person","two", "Freshman", 2.3, "prof 1", "MD", 10)
    
    #print(s1 + s2)
    #print(str(s1))
    #print(str(s2))
    
    t1 = Teacher("teacher","one", "Professor", 10, 12)
    #print(str(t1))

    # Shreeya
    #person_info(df, "Suzette Jillane", "Jillane")
    #plot(df)
    #plt.show()
    
    # Derek
    #print(t1.queue)
    #t1.update_oh_queue(oh_waitlist, x)
    #for i in t1.queue:
    #    print(i.name)
        
    y = filter_by_oh_capacity(0, x.teacher_data, [], 5)
    for i in y:
        print(i.name + ", " + i.office_hr_capacity)
    
    
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