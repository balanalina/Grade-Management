from Domain.Student import Student
from Domain.Assignment import Assignment
from Domain.Grade import Grade
from Controller.Excep import myException

class Validator:
    def __init__(self,c1,c2 = None,c3 = None):
        self._c1 = c1
        self._c2 = c2
        self._c3 = c3
        
    def studentValidator(self):
        s = ""
        if type(self._c1) != int or self._c1<1:
            s += "The student's id must be a positive integer! \n"
        k = True
        for letter in self._c2:
            if not letter.isalpha() and not letter.isspace():
                k = False
        if not k:
            s += "The student's name must contain only letters! \n"
        if type(self._c3) != int or self._c3<1:
            s += "The student's group must be a positive integer! \n"
        if len(s)!=0:
            raise myException(s)
        return None
    
    def assignmentValidator(self):
        s = ""
        if type(self._c1) != int or self._c1<1:
            s += "The assignment's id must be a positive integer! \n"
        k = True
        for letter in self._c2:
            if not letter.isalpha() and not letter.isspace():
                k = False
        if not k:
            s += "The assignment's description must contain only letters! \n"
        if type(self._c3) != int or self._c3<1:
            s += "The assignment's deadline must be a positive integer corresponding to a week! \n"
        if len(s)!=0:
            raise myException(s)
        return None
        
    def gradeValidator(self):
        if type(self._c1) != float or self._c1<1 or self._c1>10:
            raise myException("The grade must be a positive value between 1 and 10! \n")
