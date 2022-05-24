class RainfallData(object):
    def __init__(self, data, location):
        self.data = data
        self.location = location

    def get(self):
        data = self.data
        location = self.location
        found_data = {}
        station_data = data['metadata']['stations']
        readings_data = data['items'][0]['readings']
        for i in range(len(station_data)):

            for k, v  in station_data[i].items():
                if k == 'name':
                   if ((location).replace(" ", "") == v.replace(" ", "")):
                        found_data['name'] = v
                        found_data['time'] = (data['items'][0]['timestamp']).split("+")[0]
                        station_id = station_data[i]['id']
                print(k)
                print(v)
        for j in range(len(readings_data)):
            for k1, v1  in readings_data[j].items():
                if k1 == 'station_id' and v1 == station_id :
                   raining_value = readings_data[j]['value']
                   if int(raining_value) == 0:
                       found_data['is_raining'] = "Not Raining"
                   else:
                       found_data['is_raining'] = "Raining"

        print(found_data)
        return (', '.join(found_data.values()))





