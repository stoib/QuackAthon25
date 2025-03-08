classData = [
        {'id':1, 'name':"multiParadigm", 'location':"dalhousie LG05", 'time': "08:00", "map": "link"},
        {'id':1, 'name':"webdev", 'location':"dalhousie LG05", 'time': "08:00", "map": "link"},
        {'id':2, 'name':"Database", 'location':"QMB lab 3", 'time': "08:00", "map": "link"},
        {'id':3, 'name':"UserDesign", 'location':"dalhousie LG105", 'time': "08:00", "map": "link"}
]

def getTimeTableById(toFind):
    for i in range (len(classData)):
        if (classData[i].get('id') == toFind):
            return classData[i]
    return "Null"

def getFullTimeTableData():
    return classData