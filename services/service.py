from database import db

DB = db.DB

def findOne(name):
    sectorList = list(DB.values())
    for sector in sectorList:
        if sector["name"] == name:
            return sector
    return None

def findAll():
    return DB

def insert(sector):
    newKey = max(list(DB.keys())) + 1
    DB[newKey] = sector
    return DB[newKey]

def update(id : str):
    pass

def delete(id : str):
    pass
