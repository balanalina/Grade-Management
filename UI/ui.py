from Controller.Excep import myException
from Controller.Controller import *
from Controller.Validator import Validator
from Undo.undo import *
from Files.TextFile import *
from Files.PickleFile import *

class UI:
    def __init__(self,s,a,g,u,se):
        self._studentController = s
        self._assignmentController = a
        self._gradeController = g
        self._undoController = u
        self._setting = se
        
    def menu(self):
        s=" Menu \n"
        s += " 0.Exit \n"
        s += " 1.List students \n"
        s += " 2.List assignments \n"
        s += " 3.List grades \n"
        s += " 4.Add a new student \n"
        s += " 5.Add a new assignment \n"
        s += " 6.Remove a student \n"
        s += " 7.Remove assignment \n"
        s += " 8.Update a student \n"
        s += " 9.Update an assignment \n"
        s += " 10.Give assignment to a student \n"
        s += " 11.Give assignment to a group \n"
        s += " 12.Grade a student for a certain assignment \n"
        s += " 13.List students ordered  by average grade for a certain assignment. \n"
        s += " 14.List students that are late at handing their assignments. \n"
        s += " 15.List students by their average grade received for all assignments. \n"
        s += " 16.List all assignmets average graeds obtained by all students. \n"
        s += " u.Undo \n"
        s += " r.Redo \n"
        return s
    
        
    
    def start(self):
        k = True
        while k:
            if self._setting == 1:
                writeStudentToFile("Students.txt", self._studentController.getList())
                writeAssignmentToFile("Assignment.txt", self._assignmentController.getList())
                writeGradeToFile("Grade.txt", self._gradeController.getList())
                writeToBinaryFile("Studentspickle.txt",self._studentController.getList())
                writeToBinaryFile("Assignmentpickle.txt", self._assignmentController.getList())
                writeToBinaryFile("Gradepickle.txt", self._gradeController.getList())
            elif self._setting == 2:
                writeToBinaryFile("Studentspickle.txt",self._studentController.getList())
                writeToBinaryFile("Assignmentpickle.txt", self._assignmentController.getList())
                writeToBinaryFile("Gradepickle.txt", self._gradeController.getList())
            print(self.menu())
            try:
                command = input("Enter command: ")
                if command == "0":
                    k = False
                elif command == "1":
                    print(self._studentController.getList())
                elif command == "2":
                    print(self._assignmentController.getList())
                elif command == "3":
                    print(self._gradeController.getList())
                elif command == "4": 
                    self.addStudent()
                elif command == "5":
                    self.addAssignment()
                elif command == "6":
                    self.removeStudent()
                elif command == "7":
                    self.removeAssignment()
                elif command == "8":
                    self.updateStudent()
                elif command == "9":
                    self.updateAssignment()
                elif command == "10":
                    self.giveAssignmenttoStudent()
                elif command == "11":
                    self.giveAssignmenttoGroup()
                elif command == "12":
                    self.giveGrade()
                elif command == "13":
                    self.s1()
                elif command == "14":
                    self.s2()
                elif command == "15":
                    self.s3()
                elif command == "16":
                    self.s4()
                elif command == "u":
                    self._undoController.undo()
                elif command == "r":
                    self._undoController.redo()
                else:
                    print("Invalid command! \n" )
            except myException as e:
                print(e)
                
    """
    These functions are used to take input from the user(e.g. a student's id, a student's grade....).
    Input: - 
    Output: user's input
    """
    def readStudentID(self):
        id = int(input("Enter the student's id: "))
        return id
    
    def readStudentName(self):
        name = input("Enter the student's name: ")
        return name
    
    def readStudentGroup(self):
        group = int(input("Enter the student's group: "))
        return group
    
    def readAssignmentID(self):
        id = int(input("Enter the assignment's id: "))
        return id
    
    def readAssignmentDescription(self):
        desc = input("Enter the assignment's description: ")
        return desc
    
    def readAssignmentDeadline(self):
        deadline = int(input("Enter the deadline: "))
        return deadline
    
    def readGrade(self):
        grade = float(input("Enter the grade: "))
        return grade
    
    def readCurrentDeadline(self):
        cd = int(input("Please enter the current week: "))
        return cd
    
    def addStudent(self):
        id = self.readStudentID()
        name = self.readStudentName()
        group = self.readStudentGroup()
        self._studentController.addStudent(id,name,group)
    
    def addAssignment(self):
        id = self.readAssignmentID()
        desc = self.readAssignmentDescription()
        deadline = self.readAssignmentDeadline()
        self._assignmentController.addAssignment(id, desc, deadline)
        
    def removeStudent(self):
        id = self.readStudentID()
        if not self._studentController.checkID(id):
            raise myException("There is no student having this id! \n")
        self._studentController.removeStudent(id)
        
    def removeAssignment(self):
        id = self.readAssignmentID()
        self._assignmentController.removeAssignment(id)
        
    def updateStudent(self):
        id = self.readStudentID()
        if not self._studentController.checkID(id):
            raise myException("There is no student havin this id! \n")
        print("Enter the new data: \n")
        idn = self.readStudentID()
        name = self.readStudentName()
        group = self.readStudentGroup()
        self._studentController.updateStudent(id,idn,name,group)
        
    def updateAssignment(self):
        id = self.readAssignmentID()
        if not self._assignmentController.checkID(id):
            raise myException("There is no assignment having this id! \n")
        print("Enter the new data: \n")
        idn = self.readAssignmentID()
        desc = self.readAssignmentDescription()
        deadline = self.readAssignmentDeadline()
        self._assignmentController.updateAssignment(id,idn,desc,deadline)
        
    def giveAssignmenttoStudent(self):
        ids = self.readStudentID()
        if not self._studentController.checkID(ids):
            raise myException("There is no student having this id! \n")
        ida = self.readAssignmentID()
        if not self._assignmentController.checkID(ida):
            raise myException("There is no assignment having this id! \n")
        self._gradeController.giveAssigmenttoStudent(ids,ida)
        
    def giveAssignmenttoGroup(self):
        group = self.readStudentGroup()
        if not self._studentController.checkGroup(group):
            raise myException("This group does not exist! \n")
        ida = self.readAssignmentID()
        if not self._assignmentController.checkID(ida):
            raise myException("There is no assignment having this id! \n")
        self._gradeController.giveAssigmenttoGroup(group,ida)
        
    def giveGrade(self):
        ids = self.readStudentID()
        if not self._studentController.checkID(ids):
            raise myException("There is no student having this id! \n")
        ida = self.readAssignmentID()
        if not self._assignmentController.checkID(ida):
            raise myException("There is no assignment having this id! \n")
        grade = self.readGrade()
        self._gradeController.giveGrade(ids,ida,grade)
        
        
    def s1(self):
        ida = self.readAssignmentID()
        if not self._assignmentController.checkID(ida):
            raise myException("There is no assignment having this id! \n")
        newList = self._gradeController.s1(ida)
        for p in newList:
            i = self._studentController.getIndex(p.getStudentID())
            print(str(p.getGrade()) + "  " + str(self._studentController.getList().getObject(i)))
            
    def s2(self):
        cd = self.readCurrentDeadline()
        if type(cd)!= int or cd<1:
            raise myException("The current date must be an integer greater than 1!")
        newList = self._assignmentController.s2(cd)
        for p in newList:
            i = self._studentController.getIndex(p.getStudentID())
            print(str(p.getAssignmentID()) + "  " + str(self._studentController.getList().getObject(i)))
            
    def s3(self):
        newList = self._gradeController.s3()
        for p in newList:
            print(str(self._gradeController.getAverage(p.getID())) + "  " + str(p))
            
    def s4(self):
        newList = self._assignmentController.s4()
        for p in newList:
            print(str(self._assignmentController.getAverage(p.getID())) + "  " + str(p))