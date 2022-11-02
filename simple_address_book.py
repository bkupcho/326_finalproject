class Filters:
    """ A filtering system for an collection of people and their information """
    def __init__(self, name, data):
        self.data = data
        self.name = name
     
class School:
    """ This is a class representing a school in our database """
    
    def __init__(self, name, address, total_enrollment, rating):
        self.name = name
        self.address = address
        self.enrollment = total_enrollment
        self.rating = rating:

class ElementarySchool:
    """ This is a class representing an elementary school in our database"""
    
    def __init__(self, name, address, total_enrollment, rating, grades):
        super().__init__(name, address, total_enrollment, rating)
        self.grades = grades
        
