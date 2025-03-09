# classData = [
#         {'id':1, 'name':"multiParadigm", 'location':"dalhousie LG05", 'time': "08:00", "map": "link", "day": "Monday"},
#         {'id':1, 'name':"webdev", 'location':"dalhousie LG05", 'time': "08:00", "map": "link", "day": "Tuesday" },
#         {'id':2, 'name':"Database", 'location':"QMB lab 3", 'time': "08:00", "map": "link", "day": "Wednesday"},
#         {'id':3, 'name':"UserDesign", 'location':"dalhousie LG105", 'time': "08:00", "map": "link", "day": "Wednesday"}
# ]

#id is the module_id
classData = [
    {
    'id':1, 'name':"multi-paradigm", 'lectures': [{'title':"Seminar", 'day':"Monday", 'time': "12:00", 'location':"QMB", 'map': "link"},{'title':"lab", 'day':"Friday", 'time': "09:00", 'location':"Dalhousie",'map': "link"}]
    },
    {
    'id':2, 'name':"webdev", 'lectures': [{'title':"Seminar", 'day':"Wednesday", 'time': "11:00", 'location':"QMB", 'map': "link"},
                                          {'title':"lab", 'day':"Friday", 'time': "09:00", 'location':"Dalhousie",'map': 'link'}]
    }
]
#Queen+Mother+Building+(QMB)/@56.4584671,-3.0010929,15
#will need to rework to use student information
def getTimeTableById(toFind):
    results = []
    for i in range (len(classData)):
        if (classData[i].get('id') == toFind):
            #print(classData[i])
            results.append(classData[i])
    if len(results) >= 1:
        return results
    else:
        print("I am an error")
        return "NULL"

def getFullTimeTableData():
    return classData