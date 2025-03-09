from society_data import *
from timetable import *
from student import *

def compileTimesForStudent(idToFind):

    #find student
    foundStudent = "NULL"
    for i in range (len(studentData)):
        if (studentData[i].get('id') == idToFind):
            foundStudent = studentData[i]
            print(foundStudent)
    if (foundStudent == "NULL"):
        return foundStudent;
    
    #check and collate class times
    collatedTimes = [];

    for i in range (len(foundStudent.get('modules'))):
        for j in range(len(classData)):
            if ((foundStudent.get('modules')[i]) == (classData[j].get('id'))):
                    collatedTimes.append(classData[j])
    
    for i in range (len(foundStudent.get('societies'))):
        for j in range(len(societyData)):
            if ((foundStudent.get('societies')[i]) == (societyData[j].get('id'))):
                    collatedTimes.append(societyData[j].get('events'))

    return collatedTimes