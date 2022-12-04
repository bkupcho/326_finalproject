from argparse import ArgumentParser
import re
import sys
import pandas as pd

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
	return allnames
    
def fletter_sort(colname, letter):
	"""Creates a filtering system based off the first letter of the words in a column using a list comprehension and f strings.
		
  		args:
			colname (str): the name of a column in the allnames dataframe
			letter (str): a capital letter that represents the first letter of the items in a column that the user wants to filter by.
		
  		returns:
			the frquency of the results and a list of names begins with the given letter.
	"""
	wordlist = allnames[colname].to_list()
	fletter = [x for x in fletter if letter in x[0]]
	return f"frequency of {letter} in {colname} :{len(fletter)}; results:{fletter}"

class Student:
    """Class representing a student and their information.

    Attributes:
        name (str): person's first and last name.
        number (int): individual's 10-digit phone number.
        year (str): individual's year at college.
        course_grade (int): numeric grade average of the student.
        professor (str): student's course professor.
        home_state (str): student's home state.
        hr_week_studying (int): hours a week student spends for the particular
			course.
    """
    
    def __init__(self, fname, lname, number, year, course_grade, professor,
                home_state, hr_week_studying):
        self.name = fname + lname
        self.number = number
        self.year = year
        self.course_grade = course_grade
        self.professor = professor
        self.home_state = home_state
        self.hr_week_studying = hr_week_studying

	# extracts information about a person from a csv file; prints it as an f-string.
    def person_info():
        """ Displays basic information about an individual.
		
  			Args:
				name (str): person's first and last name
    			number (int): individual's 10-digit phone number
				year (str): individual's address expressed as a regex
				county (str, optional): county where the person lives
    
    		Returns:
	    		An f-string showing a person's basic information.
		"""
        return 0
    # sees similarities between person 1 person two from the data in the csv file
    def compare(self, person2):
        """ Compares information about person 1 to person 2 using set operations and conditional statements

    		Args:
     			Person2 (str): an instance of a person
    		
      		Returns:
				A list of the commonalities between two people
    	"""
        return 0
    	
# creates a sorted dataframe that only shows people who live in a given county
def sort_by_county(self, county_name):
    """ Uses pandas filtering to display the people that live in a given county
    		Args:
				county_name (str): the name of the county to filter by
    		
      		Returns:
				A dataframe consisting of the people in a given county
    """
    return 0
    
def sort_by_name(self, last_name):
	""" Uses pandas to filter and display the people that have the same last name
    		
      		Args:
				last_name (str): the last name of the person
    
    		Returns:
				A dataframe of the people that are related to one another
    """
	return 0

def differences(self, person2):
    """ Compares and displays the differences between person 1 and person 2 using sequence unpacking
    	
     	Args:
			person2 (str): an instance of a person
    	
     	Returns:
			A list of differences between the two people
    """
    return 0

