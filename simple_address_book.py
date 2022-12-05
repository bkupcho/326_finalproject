from argparse import ArgumentParser
import re
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
            colname (str): the name of a column in the allnames dataframe
            letter (str): a capital letter that represents the first letter of 
                   the items in a column that the user wants to filter by.
        
          returns:
            the frquency of the results and a list of names begins with the 
                   given letter.
    """
    wordlist = allnames[colname].to_list()
    fletter = [x for x in fletter if letter in x[0]]
    return f"frequency of {letter} in {colname} :{len(fletter)}; \
     results:{fletter}"

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
        self.name = fname + lname
        self.year = year
        self.course_grade = course_grade
        self.professor = professor
        self.home_state = home_state
        self.hr_week_studying = hr_week_studying
    
    def person_info():
        """Displays basic information about an individual.

        Args:
            name (str): person's first and last name
            number (int): individual's 10-digit phone number
            address (str): individual's address expressed as a regex
            county (str, optional): county where the person lives
    
        Returns:
            An f-string showing a person's basic information. 
        """	
     
        df = pd.read_csv('class1.csv', index_col = "last_name")
        return df.loc['Tiffa']
        
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
        
# creates a sorted dataframe that only shows people who live in a given county
def sort_by_professor(self, professor):
    """ Uses set operations to compare students' professors.
            Args:
            professors (str): the name of the professor
            
              Returns:
            list of names of students that fulfill the given set operation	
    """
    
def plot(self):
    """ Uses seaborn implot to display the correlation between hr_week_studying 
        and course_grade based on each teacher
    
         Args:
            df (str): dataframe of all 3 csv files"""
    df = pd.concat(map(pd.read_csv, ['class1.csv', 'class2.csv','class3.csv']))
    sns.lmplot( x = "hr_week_studying", y = "course_grade" , data = df, hue = 
            "professor")
    
def differences(self, person2):
    """ Compares and displays the differences between person 1 and person 2 
            using sequence unpacking
         
           Args:
            person2 (str): an instance of a person
    
        Returns:
            A list of differences between the two people
    """
    return 0

class Teacher:
    
    def __init__(self, fname, lname, position, years_of_experience, office_hr_capacity):
        self.name = fname + lname
        self.position = position
        self.years_of_experience = years_of_experience
        self.office_hr_capacity = office_hr_capacity
        self.queue = []
        
    def how_many_students_waiting(filepath):
        
        with open(filepath, "r", encoding="utf-8") as f:
             for line in f: 
                 matched_obj = re.search(r"(\w+),(\w+),(\w+),(\w+),(\w+)")

class DataBase:
    
    def __init__(self, c1, c2, c3, t1):
        newfile = concatenate(c1,c2,c3).to_csv
        self.course_data = {}
        self.teacher_data = []
        
        with open(t1, "r", encoding="utf-8") as f:
                 for line in f: matched_obj = re.search(r"(\w+),(\w+),(\w+),(\w+),(\w+),(\w+),(\w+)", line)
                 key = matched_obj.group(1) + matched_obj.group(2)
                 self.course_data[key] = Student(matched_obj.group(1),
                 matched_obj.group(2),matched_obj.group(3),
                 matched_obj.group(4),matched_obj.group(5),
                 matched_obj.group(6),matched_obj.group(7)) 
        
        #with open(t1, "r", encoding="utf-8") as f:
        #    for line in f: 
        #       matched_obj = re.search(r"(\w+),(\w+),(\w+),(\w+),(\w+)")
                 
                 
    

