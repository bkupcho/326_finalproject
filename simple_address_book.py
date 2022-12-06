from argparse import ArgumentParser
import re
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
            
    def __str__(self):
        for teacher in self.teacher_data:
            print(f"{teacher.name} has {int(teacher.office_hr_capacity) - len(teacher.queue)} spots open")
            
        for student in self.course_data:
            print(f"{student} has a gpa of {self.course_data[student].course_grade}")
            
        return ""
    
    def filter_by_oh_capacity(self, index, original_list, new_list, n):
        if index == len(original_list):
            return new_list
        else:
            (self.filter_by_oh_capacity(index + 1, original_list, new_list, n)) \
                if (original_list[index].office_hr_capacity < 5) else \
                    (self.filter_by_oh_capacity(index + 1, original_list, 
                              new_list.append(original_list[index]), n))
    
class Teacher:
    
    def __init__(self, fname, lname, position, years_of_experience, office_hr_capacity):
        self.name = fname + lname
        self.position = position
        self.years_of_experience = years_of_experience
        self.office_hr_capacity = office_hr_capacity
        self.queue = []
        
    def update_oh_queue(self, filepath, database):
        with open(filepath, "r", encoding="utf-8") as f:
             for line in f: 
                 matched_obj = re.search(r"(\w+),(\w+)", line)
                 name = matched_obj.group(1) + " " + matched_obj.group(2)
                 
                 if name in database.course_data.keys():
                    self.queue.append(database.course_data[name])
                
    def __str__(self):
        exp = self.years_of_experience
        prof = self.name
        
        tenure = print(f'{prof} has taught for {exp} years and is tenured') \
            if len(exp) > 4 else print(f'{prof} has taught for \
                {exp} years and is not tenured yet.')           

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
    
    def person_info(self, allnames, name, lname):
        """Displays basic information about an individual.

        Args:
            allname (str): dataframe of 3 csv files
            name (str): individual's first and last name
            lname (str): individual's last name
    
        Returns:
            An f-string and row showing a selected person's basic information. 
        """	
     
        df = allnames
        print(f"This is {self.name}'s personal information:")
        df.loc[df['last_name'] == lname]
        
    # sees similarities between person 1 person two from the data in the csv
    # file
    def compare(self, person2):
        """ Compares information about person 1 to person 2 using set operations 
                and conditional statements

            Args:
                 Person2 (str): an instance of a person
            
              Returns:
            A list of the commonalities between two people
        """
        return 0
    
    def __add__(self, other):
        return (self.course_grade + other.course_grade) / 2
    
    def __str__(self):
        gpa = self.course_grade
        student = self.name
        
        location = print(f'{student} is on the Dean\'s list') if gpa >= 3 else \
            print(f'{student} did not make the Dean\'s list')
            
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
    return f"frequency of {letter} in {colname} :{len(fletter)}; \
     results:{fletter}"
        
# creates a sorted dataframe that only shows people who live in a given county
def sort_by_professor(self, professor):
    """ Uses set operations to compare students' professors.
    
        Args:
            professors (str): the name of the professor
            
        Returns:
            list of names of students that fulfill the given set operation	
    """
    
def plot(self, allnames):
    """ Uses seaborn implot to display the correlation between hr_week_studying 
        and course_grade based on each teacher
    
         Args:
            allnames (str): dataframe of all 3 csv files
            
         Returns:
            a seaborn implot
    """
    
    df = allnames
    sns.lmplot( x = "hr_week_studying", y = "course_grade" , data = df, hue = "professor")
    
def differences(self, person2):
    """ Compares and displays the differences between person 1 and person 2 
            using sequence unpacking
         
           Args:
            person2 (str): an instance of a person
    
        Returns:
            A list of differences between the two people
    """
    return 0
