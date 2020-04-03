from Domain.Student import Student
from Domain.Assignment import Assignment
from Domain.Grade import Grade
from Repository.Repository import *
from Controller.Controller import *
from UI.ui import UI
from Undo.undo import undoCrontroller
from Files.TextFile import readFile
import random
from random import choice

def listInit(studentList,assignmentList,gradeList):
    firstName = [ "James " , "John " , "Robert " , "Michael " , "William " , "Mary "  , "Patricia " , "Jennifer " , "Linda " , "Elizabeth "]
    lastName = ["Smith" , "Johnson" , "Williams" , "Brown" , "Jonrs" , "Garcia" , "Miller" , "Davis" , "Rodriguez" , "Martinez"]
    group = [511 , 512 , 513 ,514 , 515 ,516]
    for i in range(100):
        studentList.addObject(Student(i+1,choice(firstName) + choice(lastName), choice(group)))
    desc1 = ["Copper " , "Nitric Acid " , "Potassium Iodide " , "Hydrogen Peroxide " , "Alkali Metal "]
    desc2 = ["in Water" , "reaction" , "coloring Fire" , "dehydration" , "and thermite"]
    deadline = [3 , 4 , 5, 6]
    for i in range(100):
        assignmentList.addObject(Assignment(i+1,choice(desc1) + choice(desc2) , choice(deadline)))
    nr = [1,2,3,4,5,6,7,8,9,10]
    for i in range(100):
        gradeList.addObject(Grade(1+i,100 -i, choice(nr)))
    

k = True
while k:
    print("Data can be read: in-memory, text file, binary \n")
    print("0.Exit")
    setting = input("Enter data mode: ")
    if setting == "in-memory":
        k = False
        studentList = Repository()
        assignmentList = Repository()
        gradeList = Repository()
        listInit(studentList, assignmentList, gradeList)
        settings = 0
    elif setting == "text file":
        k = False
        studentList = Repository()
        assignmentList = Repository()
        gradeList = Repository()
        readFile("Students.txt ",studentList, Student)
        readFile("Assignment.txt",assignmentList,Assignment)
        readFile("Grade.txt", gradeList , Grade)
        settings = 1
    elif setting == "binary":
        k = False
        studentList = PickleRepository("Studentspickle.txt")
        assignmentList = PickleRepository("Assignmentpickle.txt")
        gradeList = PickleRepository("Gradepickle.txt")
        settings = 2
    else:
        print("Invalid input!")

u = undoCrontroller()
s = studentController(studentList,assignmentList,gradeList,u)
a = assignmentController(studentList,assignmentList,gradeList,u)
g = gradeController(studentList,assignmentList,gradeList,u)
ui = UI(s,a,g,u,settings)
ui.start()
