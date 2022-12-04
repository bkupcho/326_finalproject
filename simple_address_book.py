from argparse import ArgumentParser
import re
import sys
import pandas as pd

class Person:
    def concatenate(f1,f2):
	'''concatenates the seprate csv files into one dataframe.
	args:
		f1 (str): a path to the first file
		f2 (str): a path to the second file
		f3 (str): a path to the third file
	returns:
		a dataframe of all the class sections.
	'''
        df1 = pd.read_csv(f1)
        df2 = pd.read_csv(f2)
	df3 = pd.read_csv(f3)
        allnames = pd.concat([df1, df2, df3])
        return allnames
    def fletter_sort(colname, letter):
	'''Creates a filtering system based off the first letter of the words in a column using a list comprehension and f strings.
	args:
		colname (str): the name of a column in the allnames dataframe
		letter (str): a capital letter that represents the first letter of the items in a column that the user wants to filter by.
	returns:
		the frquency of the results and a list of names begins with the given letter.
	'''
        wordlist = allnames[colname].to_list()
        fletter = [x for x in fletter if letter in x[0]]
        return f"frequency of {letter} in {colname} :{len(fletter)}; results:{fletter}"





class Person:
    """Class representing a person and their information.

    Attributes:
        name (str): person's first and last name
        number (int): individual's 10-digit phone number
        address (str): individual's address expressed as a regex
        county (str, optional): county where the person lives
    """
    def __init__(self, name, number=None, address, city):
        self.name = name
	self.number = number
	self.address = address
	self.city = city

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
	# extracts information about a person from a csv file; prints it as an f-string.
  
    def compare(self, person2):
    """ Compares information about person 1 to person 2 using set operations and conditional statements

    Args:
        Person2 (str): an instance of a person
    Returns:
	A list of the commonalities between two people
    """
	# sees similarities between person 1 person two from the data in the csv file

    def sort_by_county(self, county_name):
    """ Uses pandas filtering to display the people that live in a given county
    Args:
	county_name (str): the name of the county to filter by
    Returns:
	A dataframe consisting of the people in a given county
    """
	# creates a sorted dataframe that only shows people who live in a given county
	
    def sort_by_name(self, last_name):
	""" Uses pandas to filter and display the people that have the same last name
    Args:
	last_name (str): the last name of the person
    Returns:
	A dataframe of the people that are related to one another
    """
	
	def differences(self, person2):
	""" Compares and displays the differences between person 1 and person 2 using sequence unpacking
    Args:
	person2 (str): an instance of a person
    Returns:
	A list of differences between the two people
    """
 
	
class ResourceDatabase:
''' Class representing the resources within a county

    Attributes: 
	database (dictionary -> list of 'Resource' objects) -> represents a
		dictionary whose keys are town names, and each keys value is
		a list of 'Resource' objects for that town. These resources can
		either be schools, hospitals, police departments, fire departments,
		or etc. (i.e., public services)
'''

	def __init__(self, filepath):
	'''
		Here, I'm going to read in the file with data about local nearby resources, these include:
		schools, hospitals, police departments, fire departments, or etc. (i.e., public services).
		I'm going to match each line read in with a regex, and capture groups. I'm going to use those
		capture groups to represent a 'Resource' object for each line. Based on the town of the resource
		object, I'm going to append each 'Resource' object to it's corresponding list value in the 
		'database' dictionary attribute, using the 'Resource' objects name as the key in the dictionary. 
	''' 
	    with open ( … ) as f:
		For each 'line’ in file being read in
			expression = r “ … “
			m = re.match(line, expression)
			x = group(town)
			y = group(2)
			...
			self.database[x].append(Resource(..., ..., ...))

				
	def resources_by_town(eelf, String: town_name):
	""" outputs a list of resources based on a specified town
		Args:
			town_name (string) -> specified town to get list of resources for
		Returns (list of 'Resource' objects) -> returns resources a town has
	"""
		return self.database[town_name]

class Resource:
	''' This class represents a public service in our database. This class has many sub classes,
	    based on the type of pubic service '''
	
	def __str__(self):
	''' This function will use f-strings to specify what the magic method str should print out for each 'Resource' object''' 
	    return f" {...} is a Resource"
	
class School(Resource):
   	""" This is a class representing a school in our database, and it has subclasses based on
	the type of school (elementary, middle, high)
	
	Attributes:
		name (string) -> name of the school
		address (string) -> school address
		enrollment (int) -> total number of students
		rating (float) -> total rating """
		
   	def __init__(self, name, address, total_enrollment, rating):
       		self.name = name
       		self.address = address
       		self.enrollment = total_enrollment
       		self.rating = rating
				
	def __str__(self):
	''' This function will use f-strings to specify what the magic method str should print out for each 'School' object''' 
	    return f" {...} is a School in {...} "

class ElementarySchool(School):
  	 """ This is a class representing an elementary school in our database
	 	Uses the super method to call its parents 'init' method
	
	Attributes:
		name (string) -> name of the school
		address (string) -> school address
		enrollment (int) -> total number of students
		rating (float) -> total rating
		grades (list of ints) -> list of school grades for the school (like 3rd, 4th grade, etc.) """
  
   	def __init__(self, name, address, total_enrollment, rating, grades):
       		super().__init__(name, address, total_enrollment, rating)
       		self.grades = grades

	def __str__(self):
	''' This function will use f-strings to specify what the magic method str should print out for each 'ElementarySchool' object''' 
	    return f" {...} is an Elementary School in {...}"
		

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
		

