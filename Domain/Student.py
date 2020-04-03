import unittest
"""
This class creates a student, having an ID, name and a group.
Input: id - unsigned integer, name - string , group - unsigned integer
Output: student - object
"""
class Student:
    def __init__(self,id,name,group):
        self._id = int(id)
        self._name = str(name)
        self._group = int(group)
    
    """
    Getters are used to obtain a certain attribute of a student(id, name, group), while being outside the class.
    Input: - 
    Output: attribute
    """
        
    def getID(self):
        return self._id
    
    def getName(self):
        return self._name
    
    def getGroup(self):
        return self._group
    
    """
    Setters are used to change a certain attribute of a student(id, name, group), while being outside the class.
    Input: the new attribute
    Output: - 
    """
    
    def setID(self,id):
        self._id = id
        
    def setName(self,name):
        self._name = name
        
    def setGroup(self,group):
        self._group = group
        
    def __str__(self):
        return str(self._id) + " " + str(self._name) + " " + str(self._group) + "\n"
    
class testStudent(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test(self):
        s1 = Student(20,"Mihai",542)
        s2 = Student(56,"Maria", 561)
        s2.setID(20)
        s2.setName("Mihai")
        s2.setGroup(542)
        assert s1.getID() == s2.getID()
        assert s1.getName() == s2.getName()
        assert s1.getGroup() == s2.getGroup()
        
        
    
    