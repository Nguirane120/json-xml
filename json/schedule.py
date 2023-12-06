import json
import fnc

class ItineraryProcessor:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.data = json.load(file)


    def get_messages(self):
        grouped_response = self.data.get('groupedItineraryResponse', {})
        messages = grouped_response.get('messages', [])
        return fnc.get('messages', grouped_response, default=[])

    def get_version(self):
        return fnc.get('groupedItineraryResponse.version', self.data, default=None)

    def get_schedules(self):
        return self.data['groupedItineraryResponse'].get('scheduleDescs', [])

    def get_departures(self):
        schedules = self.get_schedules()
        mapped_departures = fnc.map(lambda schedule: schedule['departure'], schedules)
        return list(mapped_departures)

    def get_carrier(self):
        schedules = self.get_schedules()
        mapped_carrier = fnc.map(lambda schedule: schedule['carrier'], schedules)
        return list(mapped_carrier)
  

json_file_path = './search_rep.json'


processor = ItineraryProcessor(json_file_path)


version = processor.get_version()
departures = processor.get_departures()
cariers = processor.get_carrier()
messages = processor.get_messages()


print("***********************START DEPARTURE ****************")
print(departures)
print("***********************END DEPARTURE ****************")

print("***********************START CARRIEERS ****************")
print(cariers)
print("***********************END CARRIEERS    ****************")

print("***********************START MESSAGES ****************")
print(messages)
print("***********************END MESSAGES     ****************")
print("***********************VERSION ****************")
print(version)


