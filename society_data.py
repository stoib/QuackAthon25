#store society data here for now, maybe store it somewhere else later, or in a file
societyData = [
        {'id':1, 'name':"boardgames", 'description':"play board games etc etc etc", 'image':"boardgames.jpg"},
        {'id':2, 'name':"computing", 'description':"buncha nerds", 'image':"ducs.png"},
        {'id':3, 'name':"esports", 'description':"also nerds but videogames", 'image':"esports.jpg"},
        {'id':4, 'name':"roleplay", 'description':"playing rolls, and rolling dice", 'image':"durps.webp"},
        {'id':5, 'name':"marketing", 'description':"they do seem to be advertising right now", 'image':"marketing.webp"},
        {'id':6, 'name':"mycology", 'description':"that means the study of mushrooms", 'image':"mycology.webp"},
        {'id':7, 'name':"pokemon", 'description':"this one specific videogame", 'image':"pokemon.jpg"}
]

def getSocietyById(toFind):
    for i in range (len(societyData)):
        if (societyData[i].get('id') == toFind):
            return societyData[i]
    return "NULL"

def getFullSocietyData():
    return societyData