import json
import fnc

class ItineraryProcessor:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.data = json.load(file)

    def get_schedules(self):
        return self.data['groupedItineraryResponse'].get('scheduleDescs', [])

# Chemin vers votre fichier JSON
json_file_path = './search_rep.json'

# Créer une instance de la classe ItineraryProcessor
processor = ItineraryProcessor(json_file_path)

# Récupérer les données relatives aux schedules avec fnc
schedules = processor.get_schedules()

# Filtrer les schedules si nécessaire
# Par exemple, filtrer les schedules avec stopCount > 0
filtered_schedules = fnc.map(lambda schedule: (schedule['id'], schedule), schedules)
filtered_schedules_list = list(filtered_schedules)

# Afficher les schedules filtrés
print("Schedules filtrés :")
print(filtered_schedules_list)
