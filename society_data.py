#store society data here for now, maybe store it somewhere else later, or in a file
societyData = [
        {'id':1, 'name':"boardgames", 'description':"play board games etc etc etc", 'image':"boardgames.jpg", 'events':{
        'id':1, 'name':"board games society", 'lectures': [{'title':"club", 'day':"Wednesday", 'time': "19:00", 'location':"Bonar Hall", 'map': "link"},
        {'title':"club", 'day':"Sunday", 'time': "19:00", 'location':"Bonar Hall", 'map': "link"}]}},

        {'id':2, 'name':"computing", 'description':"buncha nerds", 'image':"ducs.png", 'events':{
        'id':2, 'name':"computing society", 'lectures': 
        [{'title':"Hackathon", 'day':"Saturday", 'time': "10:00", 'location':"QMB", 'map': "link"}]}},

        {'id':3, 'name':"esports", 'description':"also nerds but videogames", 'image':"esports.jpg", 'events':{
        'id':3, 'name':"esports society", 'lectures': 
        [{'title':"smash bros", 'day':"Monday", 'time': "20:00", 'location':"The Liar", 'map': "link"},
        {'title':"jackbox", 'day':"Friday", 'time': "17:00", 'location':"Online",'map': "link"}]}},

        {'id':4, 'name':"roleplay", 'description':"playing rolls, and rolling dice", 'image':"durps.webp", 'events':{
        'id':4, 'name':"roleplay society", 'lectures': 
        [{'title':"DnD", 'day':"Monday", 'time': "19:00", 'location':"Dalhousie", 'map': "link"},
        {'title':"Wargames", 'day':"Sunday", 'time': "11:00", 'location':"Cake or Dice",'map': "link"}]}},


        {'id':5, 'name':"marketing", 'description':"they do seem to be advertising right now", 'image':"marketing.webp", 'events':{
        'id':5, 'name':"marketing society", 'lectures': 
        [{'title':"field research", 'day':"Tuesday", 'time': "10:00", 'location':"Big Tesco", 'map': "link"},
        {'title':"promotion", 'day':"Friday", 'time': "17:05", 'location':"Wetherspoons",'map': "link"}]}},

        {'id':6, 'name':"mycology", 'description':"that means the study of mushrooms", 'image':"mycology.webp", 'events':{
        'id':6, 'name':"mycology society", 'lectures': 
        [{'title':"tasting session", 'day':"Thursday", 'time': "02:00", 'location':"Dundee Law", 'map': "link"}]}},

        {'id':7, 'name':"pokemon", 'description':"this one specific videogame", 'image':"pokemon.jpg", 'events':{
        'id':7, 'name':"pokemon society", 'lectures': 
        [{'title':"Quiz", 'day':"Monday", 'time': "19:00", 'location':"The Liar", 'map': "link"}]}},
]

def getSocietyById(toFind):
    for i in range (len(societyData)):
        if (societyData[i].get('id') == toFind):
            return societyData[i]
    return "NULL"

def getFullSocietyData():
    return societyData