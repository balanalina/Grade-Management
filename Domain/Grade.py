import unittest
"""
This class creates a grade, having an assignment ID,student ID and a grade.
Input: assignment id - unsigned integer, student ID - unsigned integer, grade - unsigned integer between 1 and 10 
Output: grade - object
"""
class Grade:
    def __init__(self,assignmentID,studentID,grade):
        self._assignmentID = int(assignmentID)
        self._studentID = int(studentID)
        self._grade = float(grade)
        
    """
    Getters are used to obtain a certain attribute of a grade(assignment id,student id, grade), while being outside the class.
    Input: - 
    Output: attribute
    """
    
    def getAssignmentID(self):
        return self._assignmentID
    
    def getStudentID(self):
        return self._studentID
    
    def getGrade(self):
        return self._grade
    
    """
    Setters are used to change a certain attribute of a grade(assignment id, student id, grade), while being outside the class.
    Input: the new attribute
    Output: - 
    """
    
    def setAssignmentID(self,newID):
        self._assignmentID = newID
        
    def setStudentID(self,newID):
        self._studentID = newID
        
    def setGrade(self,grade):
        self._grade = grade
        
    def __str__(self):
        return str(self._assignmentID) + " " + str(self._studentID) + " " + str(self._grade) + "\n"
    
class gradeTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test(self):
        g1 = Grade(132,54,5)
        g2 = Grade(654,255154,6)
        g2.setAssignmentID(132)
        g2.setStudentID(54)
        g2.setGrade(5)
        assert g1.getAssignmentID() == g2.getAssignmentID()
        assert g1.getStudentID() == g2.getStudentID()
        assert g1.getGrade() == g2.getGrade()
        