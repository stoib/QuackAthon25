from society_data import *
from timetable import *
from student import *

def compileTimesForStudent(idToFind):

    #find student
    foundStudent = "NULL"
    for i in range (len(studentData)):
        if (studentData[i].get('id') == idToFind):
            foundStudent = studentData[i]
    if (foundStudent == "NULL"):
        return foundStudent;
    
    #check and collate class times
    collatedTimes = [];

    for i in range (len(foundStudent.modules)):
        for j in range(len(classData)):
            if ((foundStudent.modules[i].get('id')) == (classData[j].get('id'))):
                    collatedTimes.append(classData[j])
    
    for i in range (len(foundStudent.societies)):
        for j in range(len(societyData)):
            if ((foundStudent.societies[i].get('id')) == (societyData[j].get('id'))):
                    collatedTimes.append(soietyData[j].get('events'))

    return collatedTimes