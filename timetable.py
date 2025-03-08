classData = [
        {'id':1, 'name':"multiParadigm", 'location':"dalhousie LG05", 'time': "08:00", "map": "link", "day": "Monday"},
        {'id':1, 'name':"webdev", 'location':"dalhousie LG05", 'time': "08:00", "map": "link", "day": "Tuesday" },
        {'id':2, 'name':"Database", 'location':"QMB lab 3", 'time': "08:00", "map": "link", "day": "Wednesday"},
        {'id':3, 'name':"UserDesign", 'location':"dalhousie LG105", 'time': "08:00", "map": "link", "day": "Wednesday"}
]

def getTimeTableById(toFind):
    results = []
    for i in range (len(classData)):
        if (classData[i].get('id') == toFind):
            results.append(classData[i])
    if len(results) >= 1:
        return results
    else:
        print("I am an error")
        return "Null"

def getFullTimeTableData():
    return classData