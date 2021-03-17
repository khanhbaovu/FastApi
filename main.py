from fastapi import FastAPI
from models import sector
from services import service

app = FastAPI()

Sector = sector.Sector

@app.get("/findAll")
async def getAllSectors():
    return service.findAll()

@app.get("/findOne")
async def getSector(sector : Sector):
    return service.findOne(sector.name)

@app.post("/insert")
async def insertSector(sector : Sector):
    newSector = {
      "id" : sector.id,
      "name" : sector.name,
      "field" : sector.field
    }
    return service.insert(newSector)

@app.put("/update/{id}")
async def updateSector(id: str):
    pass

@app.delete("/delete/{id}")
async def deleteSector(id : str):
    pass
