from Domain.Student import Student
from Domain.Assignment import Assignment
from Domain.Grade import Grade
from Controller.Excep import myException
from Repository.Repository import Repository

def readFile(fileName,repo,function):
    try:
        result = []
        f = open(fileName, "r")
        line = f.readline().strip()
        while  len(line) > 0:
            line = line.split(";")
            repo.addObject(function(line[0], line[1], line[2]))
            line = f.readline().strip()
        f.close()
    except IOError as e:
        print("An error occured - " + str(e))
        raise e
    return result

def writeStudentToFile(fileName, repo):
    f = open(fileName, "w")
    try:
        for i in range (len(repo)):
            pString = str(repo.getObject(i).getID()) + "; " + repo.getObject(i).getName() + " ;" + str(repo.getObject(i).getGroup()) + "\n"
            f.write(pString)
        f.close()
    except Exception as e:
        print("An error occured -" + str(e))
        
def writeAssignmentToFile(fileName, repo):
    f = open(fileName, "w")
    try:
        for i in range (len(repo)):
            pString = str(repo.getObject(i).getID()) + "; " + repo.getObject(i).getDescription() + " ;" + str(repo.getObject(i).getDeadline()) + "\n"
            f.write(pString)
        f.close()
    except Exception as e:
        print("An error occured -" + str(e))
        
def writeGradeToFile(fileName, repo):
    f = open(fileName, "w")
    try:
        for i in range (len(repo)):
            pString = str(repo.getObject(i).getStudentID()) + ";" + str(repo.getObject(i).getAssignmentID()) + ";" + str(repo.getObject(i).getGrade()) + "\n"
            f.write(pString)
        f.close()
    except Exception as e:
        print("An error occured -" + str(e))
        
        



