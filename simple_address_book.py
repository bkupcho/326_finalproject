class Person:
    """Class representing a person and their information.

    Attributes:
        name (str): person's first and last name
        number (int): individual's 10-digit phone number
        address (str): individual's address expressed as a regex
        county (str, optional): county where the person lives
    """
    def __init__(self, name, number, address, county=None):
        # dictionary of attributes listed above

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
	
class ResourceDatabase:
''' Class representing the resources within a county
Attributes: 
	database (Set) '''

	def __init__(self, filepath):
	''' For each 'line’ in file being read in
	expression = r “ … “
			New_resource = Resource
			Here, I’m going to create a new ‘Resource’ object for each line, then 
	Read in the file with data about local nearby resources, these include:
	Schools
	Health Centers / Hospitals ''' 
	
	with open ( … ) as f:

	def __str__(self):


	resources_by_town(String: town_name):
