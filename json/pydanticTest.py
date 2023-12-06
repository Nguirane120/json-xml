import json
from pydantic import BaseModel
from datetime import date

voyageur_json = "./voyageur.json"

class Itineraire(BaseModel):
    origin: str
    destination: str
    departureDate: date  

class Voyageur(BaseModel):
    requestType: str
    customer: str
    excludeBasicEconomy: bool
    maxConnection: int
    baggagePref: bool
    adult: int
    child: int
    infant: int
    csv: str
    pcc: str
    alternatePcc: str
    preferredAirlines: str
    itineraries: list[Itineraire]

# Lecture des données à partir du fichier JSON
with open(voyageur_json, 'r') as json_file:
    json_data = json.load(json_file)


voyageur = Voyageur(**json_data)

print(voyageur)
