studentData = [
    {'id': 1, 'first_name': "Euan", 'surname': "Wilson", 'age': 20, 'modules': [1, 4, 3], 'societies': [2, 3, 5]},
    {'id': 2, 'first_name': "Iain", 'surname': "Mckenzie", 'age': 19, 'modules': [1, 2, 3], 'societies': [2, 3, 4, 6]},
    {'id': 3, 'first_name': "Scott", 'surname': "Hamilton", 'age': 21, 'modules': [2, 1, 5], 'societies': [1, 2, 6, 7]}
    {'id': 4, 'first_name': "Test", 'surname': "Person", 'age': 91, 'modules': [1, 2, 3, 4, 5], 'societies': [1, 2, 3, 4, 5, 6 ,7]}
]

def getStudentById(toFind):
    results = []
    for i in range (len(studentData)):
        if (studentData[i].get('id') == toFind):
            results.append(studentData[i])
    if len(results) >= 1:
        return results
    else:
        print("Error")
        return "NULL"
    
def getFullStudentData():
    return studentData