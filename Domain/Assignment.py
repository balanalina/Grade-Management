import unittest
"""
This class creates an assignment, having an ID,description and a deadline.
Input: id - unsigned integer, description - string , deadline - unsigned integer
Output: assignment - object
"""
class Assignment:
    def __init__(self,id,description,deadline):
        self._id = int(id)
        self._description = str(description)
        self._deadline = int(deadline)
        
    """
    Getters are used to obtain a certain attribute of an assignment(id, description, deadline), while being outside the class.
    Input: - 
    Output: attribute
    """
    
    def getID(self):
        return self._id
    
    def getDescription(self):
        return self._description
    
    def getDeadline(self):
        return self._deadline
    
    """
    Setters are used to change a certain attribute of an assignment(id, description, deadline), while being outside the class.
    Input: the new attribute
    Output: - 
    """
        
    def setID(self,id):
        self._id = id
        
    def setDescription(self,description):
        self._description = description
        
    def setDeadline(self,deadline):
        self._deadline = deadline
        
    def __str__(self):
        return str(self._id) + " " + str(self._description) + " " + str(self._deadline) + "\n"
    
class testAssignment(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test(self):
        a1 = Assignment(547,"Do something",5)
        a2 = Assignment(354,"Do another thing",9)
        a2.setID(547)
        a2.setDescription("Do something")
        a2.setDeadline(5)
        assert a1.getID() == a2.getID()
        assert a1.getDescription() == a2.getDescription()
        assert a1.getDeadline() == a2.getDeadline() 