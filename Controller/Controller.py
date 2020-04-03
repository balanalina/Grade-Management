from Repository.Repository import *
from Domain.Student import Student
from Domain.Assignment import Assignment
from Domain.Grade import Grade
from Controller.Excep import myException
from Controller.Validator import Validator
from Undo.undo import *
from copy import deepcopy

class studentController:
    def __init__(self,s,a,g,u):
        self._studentList = s
        self._assignmentList = a
        self._gradeList = g
        self._undoController = u
        
        
    def getList(self):
        return self._studentList
    
    def addStudent(self,id,name,group):
        vs = Validator(id,name,group)
        vs.studentValidator()
        if self.checkID(id):
            raise myException("This id is used by another student! \n")
        undo = FunctionCall(self.removeStudent,id)
        redo = FunctionCall(self.addStudent,id, name, group)
        oper = Operation(undo,redo)
        self._undoController.addOperation(oper)
        self._studentList.addObject(Student(id,name,group))
        
    def removeStudent(self,id):
        index = self.getIndex(id)
        undo = FunctionCall(self.addStudent,id,self._studentList.getObject(index).getName(),self._studentList.getObject(index).getGroup())
        redo = FunctionCall(self.removeStudent, id)
        oper = Operation(undo,redo)
        self._undoController.addOperation(oper)
        self._studentList.removeObject(index)
        i = 0
        while i <len(self._gradeList):
            if self._gradeList.getObject(i).getStudentID() == id:
                self._gradeList.removeObject(i)
                i-=1
            i += 1
                
        
    def updateStudent(self,oldID,id,name,group):
        vs = Validator(id,name,group)
        vs.studentValidator()
        if self.checkID(id) and id != oldID:
            raise myException("There already is a student having this id! \n")
        index = self.getIndex(oldID)
        undo = FunctionCall(self.updateStudent,id ,oldID, self._studentList.getObject(index).getName(),self._studentList.getObject(index).getGroup())
        redo = FunctionCall(self.updateStudent,oldID, id, name, group)
        oper = Operation(undo,redo)
        self._undoController.addOperation(oper)
        self._studentList.getObject(index).setID(id)
        self._studentList.getObject(index).setName(name)
        self._studentList.getObject(index).setGroup(group)
        for i in range(len(self._gradeList)):
            if self._gradeList.getObject(i).getStudentID() == oldID:
                self._gradeList.getObject(i).setStudentID(id)
        
    def getIndex(self,id):
        for i in range(len(self._studentList)):
            if self._studentList.getObject(i).getID() == id:
                return i
        
        
    def checkID(self,id):
        for i in range (len(self._studentList)):
            if self._studentList.getObject(i).getID() == id:
                return True
        return False
        
    def checkGroup(self,group):
        for i in range(len(self._studentList)):
            if self._studentList.getObject(i).getGroup() == group:
                return True
        return False
        
        
class assignmentController:
    def __init__(self,s,a,g,u):
        self._studentList = s
        self._assignmentList = a
        self._gradeList = g
        self._undoController = u
        
    def getList(self):
        return self._assignmentList
    
    def addAssignment(self,id,desc,deadline):
        va = Validator(id,desc,deadline)
        va.assignmentValidator()
        if self.checkID(id):
            raise myException("This id is used by another assignment! \n")
        undo = FunctionCall(self.removeAssignment,id)
        redo = FunctionCall(self.addAssignment,id, desc, deadline)
        oper = Operation(undo,redo)
        self._undoController.addOperation(oper)
        self._assignmentList.addObject(Assignment(id,desc,deadline))
        
    def removeAssignment(self,id):
        if not self.checkID(id):
            raise myException("There is no assignment having this id! \n")
        index = self.getIndex(id)
        undo = FunctionCall(self.addAssignment,id,self._assignmentList.getObject(index).getDescription(),self._assignmentList.getObject(index).getDeadline())
        redo = FunctionCall(self.removeAssignment,id)
        oper = Operation(undo,redo)
        self._undoController.addOperation(oper)
        self._assignmentList.removeObject(index)
        i = 0 
        while i < len(self._gradeList):
            if self._gradeList.getObject(i).getAssignmentID() == id:
                self._gradeList.removeObject(i)
                i -= 1
            i += 1
        
    def updateAssignment(self,oldID,id,desc,deadline):
        va = Validator(id, desc, deadline)
        va.assignmentValidator()
        if self.checkID(id) and id != oldID:
            raise myException("There already is an assignment having this id! \n")
        index = self.getIndex(oldID)
        undo = FunctionCall(self.updateAssignment , id,oldID, self._assignmentList.getObject(index).getDescription(), self._assignmentList.getObject(index).getDeadline())
        redo = FunctionCall(self.updateAssignment,oldID, id, desc, deadline)
        oper = Operation(undo,redo)
        self._undoController.addOperation(oper)
        self._assignmentList.getObject(index).setID(id)
        self._assignmentList.getObject(index).setDescription(desc)
        self._assignmentList.getObject(index).setDeadline(deadline)
        for i in range(len(self._gradeList)):
            if self._gradeList.getObject(i).getAssignmentID() == oldID:
                self._gradeList.getObject(i).setAssignmentID(id) 
                
    def f21(self,object,cd):
        if object.getDeadline() < cd:
            return True
        return False
    
    def f22(self,object,x):
        if object.getGrade() == -1:
            return True
        return False
    
    def s2(self,cd):
        #l = list(filter(lambda x: x.getDeadline()< cd, self._assignmentList.getAll()))
        l = my_filter(self._assignmentList.getAll(), self.f21, cd)
        #l1 = list(filter(lambda x: x.getGrade() == -1,self._gradeList.getAll()))
        l1 = my_filter(self._gradeList.getAll(), self.f22)
        if len(l) == 0 or len(l1) == 0:
            raise myException("There are no late students in handing their assignments! \n")
        i = 0
        while i<len(l1):
            k = False
            j = 0
            while j < len(l):
                if l1[i].getAssignmentID() == l[j].getID():
                    k = True
                j += 1
            if not k:
                l1.pop(i)
                i -= 1
            i += 1
        return l1
        
    def cmp4(self,a,b):
        if self.getAverage(a.getID()) < self.getAverage(b.getID()):
            return True
        return False
        
    def f4(self,object,x):
        if self.getAverage(object.getID()) != -1:
            return True
        return False
        
    def s4(self):
        #l = list(filter(lambda x: self.getAverage(x.getID()) != -1 , self._assignmentList.getAll()))
        l = my_filter(self._assignmentList.getAll(), self.f4)
        if len(l) == 0:
            raise myException("There are no graded assignments! \n")
        my_sort(l, self.cmp4)
        return l
    
        
    def getAverage(self,ida):
        s = 0
        nr = 0
        for i in range(len(self._gradeList)):
            if self._gradeList.getObject(i).getAssignmentID() == ida:
                s += self._gradeList.getObject(i).getGrade()
                nr += 1
        if nr != 0:
            return s/nr
        return -1
        
    def getIndex(self,id):
        for i in range (len(self._assignmentList)):
            if self._assignmentList.getObject(i).getID() == id:
                return i
        
    def checkID(self,id):
        for i in range (len(self._assignmentList)):
            if self._assignmentList.getObject(i).getID() == id:
                return True
        return False
        
class gradeController:
    def __init__(self,s,a,g,u):
        self._studentList = s
        self._assignmentList = a
        self._gradeList = g
        self._undoController = u
        
    def getList(self):
        return self._gradeList
    
    def removeAssignment(self,ids,ida):
        for i in range(len(self._gradeList)):
            if self._gradeList.getObject(i).getStudentID() == ids and self._gradeList.getObject(i).getAssignmentID() == ida:
                self._gradeList.removeObject(i)
    
    def giveAssigmenttoStudent(self,ids,ida):
        undo = FunctionCall(self.removeAssignment,ids,ida)
        redo = FunctionCall(self.giveAssigmenttoStudent,ids, ida)
        oper = Operation(undo,redo)
        self._undoController.addOperation(oper)
        for i in range(len(self._gradeList)):
            if self._gradeList.getObject(i).getStudentID() == ids and self._gradeList.getObject(i).getAssignmentID() == ida:
                return None
        self._gradeList.addObject(Grade(ida,ids,-1))
        
    
    def giveAssigmenttoGroup(self,group,ida):
        for i in range(len(self._studentList)):
            if self._studentList.getObject(i).getGroup() == group:
                self.giveAssigmenttoStudent(self._studentList.getObject(i).getID(), ida)
                
    def giveGradeUndo(self,ids,ida):
        for i in range(len(self._gradeList)):
            if self._gradeList.getObject(i).getStudentID() == ids and self._gradeList.getObject(i).getAssignmentID() == ida:
                self._gradeList.getObject(i).setGrade(-1)
                
    def giveGrade(self,ids,ida,grade):
        vg = Validator(grade)
        vg.gradeValidator()
        for i in range(len(self._gradeList)):
            if self._gradeList.getObject(i).getStudentID() == ids and self._gradeList.getObject(i).getAssignmentID() == ida:
                if self._gradeList.getObject(i).getGrade() == -1:
                    undo = FunctionCall(self.giveGradeUndo, ids, ida)
                    redo = FunctionCall(self.giveGrade,ids, ida, grade)
                    oper = Operation(undo,redo)
                    self._undoController.addOperation(oper)
                    self._gradeList.getObject(i).setGrade(grade)
                else:
                    raise myException("This student has already been graded for this assignment! \n")
    
    def getStudentIndex(self,ids):
        for i in range(len(self._studentList)):
            if self._studentList.getObject(i).getID() == ids:
                return i         
            
    def getIDS(self,ids):
        for i in range (len(self._gradeList)):
            if self._gradeList.getObject(i).getStudentID() == ids:
                return i
            
    def getAverage(self,ids):
        s = 0
        nr = 0
        for i in range(len(self._gradeList)):
            if self._gradeList.getObject(i).getStudentID() == ids:
                s += self._gradeList.getObject(i).getGrade()
                nr += 1
        if nr != 0:
            return s/nr
        return -1
    
    def cmp1(self,a,b):
        if a.getGrade() < b.getGrade():
            return True
        return False
    
    def f1(self,object,x):
        if object.getAssignmentID() == x and object.getGrade() != -1:
            return True
        return False
    
    def s1(self,ida):
        #l = list(filter(lambda x: x.getAssignmentID() == ida and x.getGrade() != -1 , self._gradeList.getAll()))
        l = my_filter(self._gradeList.getAll(), self.f1, ida)
        if(len(l)) == 0:
            raise myException("There is no student graded at this assignment! \n")
        my_sort(l, self.cmp1)
        return l

    
    def cmp3(self,a,b):
        if self.getAverage(a.getID()) < self.getAverage(b.getID()):
            return True
        return False
    
    def f3(self,object,x):
        if self.getAverage(object.getID()) != -1:
            return True
        return False
    
    def s3(self):
        #l = list(filter(lambda x: self.getAverage(x.getID()) != -1 , self._studentList.getAll()))
        l = my_filter(self._studentList.getAll(), self.f3)
        if len(l) == 0:
            raise myException("No student was graded! \n")
        my_sort(l, self.cmp3)
        return l        
                    
    
def my_sort(list,function):
    gap = len(list) // 2
    while gap > 0:
        for i in range(gap, len(list)):
            val = list[i]
            j = i
            while j >= gap and function(list[j-gap],val):
                list[j] = list[j-gap]
                j -= gap
            list[j] = val
        gap //= 2

def my_filter(list,function, x = 0):
    result = []
    for i in range(len(list)):
        if function(list[i],x):
            result.append(list[i])
    return result
    
