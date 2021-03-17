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

def update(updatedSector):
    if updatedSector.id:
        sectorList = list(DB.values())
        for sector in sectorList:
            if sector["id"] == updatedSector.id:
                if updatedSector.name:
                    sector["name"] = updateSector.name
                if updateSector.field:
                    sector["field"] = updateSector.field
                return sector
        return None
    return None

def delete(id : str):
    pass
