import unittest

from rainfall import RainfallData

class RainFallTest(unittest.TestCase):
    def test_get_rainfall_data_notfound(self):
        mock_data = {"metadata":{"stations":[{"id":"S108","device_id":"S108","name":"Marina Gardens Drive","location":{"latitude":1.2799,"longitude":103.8703}}],"reading_type":"TB1 Rainfall 5 Minute Total F","reading_unit":"mm"}, \
                       "items": [{"timestamp":"2022-05-24T14:25:00+08:00","readings":[{"station_id":"S108","value":0}]}],"api_info":{"status":"healthy"}}
        rainfalldataTest1 = RainfallData(mock_data, "S211")
        data = rainfalldataTest1.get_rainfall_data()
        self.assertEqual(data, "Raining details for 'S211' not found!")

    def test_get_rainfall_data_found(self):
        mock_data = {"metadata":{"stations":[{"id":"S108","device_id":"S108","name":"Marina Gardens Drive","location":{"latitude":1.2799,"longitude":103.8703}}],"reading_type":"TB1 Rainfall 5 Minute Total F","reading_unit":"mm"}, \
                     "items": [{"timestamp":"2022-05-24T14:25:00+08:00","readings":[{"station_id":"S108","value":0}]}],"api_info":{"status":"healthy"}}
        rainfalldataTest2 = RainfallData(mock_data, 'Marina Gardens Drive')
        data = rainfalldataTest2.get_rainfall_data()
        self.assertEqual(data, 'Marina Gardens Drive, 14:25:00, 0mm, Not Raining')

    def test_check_for_valid_dict(self):
        mock_data = {}
        rainfalldataTest2 = RainfallData(mock_data, 'invalid')
        data = rainfalldataTest2.check_for_valid_dict()
        self.assertEqual(data, False)

if __name__ == '__main__':
    unittest.main()
