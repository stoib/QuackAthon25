#store society data here for now, maybe store it somewhere else later, or in a file
societyData = [
        {'id':1, 'name':"boardgames", 'description':"play board games etc etc etc", 'image':"boardgames.jpg"},
        {'id':2, 'name':"computing", 'description':"buncha nerds", 'image':"ducs.png"},
        {'id':3, 'name':"esports", 'description':"also nerds but videogames", 'image':"esports.jpg"}
]

def getSocietyById(toFind):
    for i in range (len(societyData)):
        if (societyData[i].get('id') == toFind):
            return societyData[i]
    return "NULL"

def getFullSocietyData():
    return societyData