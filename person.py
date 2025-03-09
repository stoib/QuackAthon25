personData = [
    {'id': 1, 'first_name': "Euan", 'surname': "Wilson", 'age': 20, 'modules': [1], 'societies': [2, 3, 5]},
    {'id': 2, 'first_name': "Iain", 'surname': "Mckenzie", 'age': 19, 'modules': [1, 2], 'societies': [2, 3, 4, 6]},
    {'id': 3, 'first_name': "Scott", 'surname': "Hamilton", 'age': 21, 'modules': [2, 1], 'societies': [1, 2, 6, 7]}
]

def getPersonById(toFind):
    results = []
    for i in range (len(personData)):
        if (personData[i].get('id') == toFind):
            results.append(classData[i])
    if len(results) >= 1:
        return results
    else:
        print("Error")
        return "NULL"
    
def getFullPersonData():
    return personData