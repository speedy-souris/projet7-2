#coding:utf-8
#!/usr/bin/env python
"""google api config management menu"""
import requests

class GoogleApiData:
    """management of Google APIs settings"""
    @staticmethod
    def get_url_from_json(url, params):
        """conversion of the address found in JSON format"""
        request = requests.get(url, params)
        url_json = request.json()
        return url_json

    @staticmethod
    def get_settings_for_placeid_api(address, key):
        """determining placeid for the address found"""
        parameters = {
            'input': f'{address}',
            'inputtype': 'textquery',
            'key': f'{key}'
        }
        return parameters

    def get_placeid_from_address(self, address, key):
        """Google map API place_id search function

        Result ok with address to 'openClassrooms'
        {
           "candidates" : [
              {
                 "place_id" : "ChIJIZX8lhRu5kcRGwYk8Ce3Vc8"
              }
           ],
           "status" : "OK"
        }
        """
        url_api = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
        parameter_data = self.get_settings_for_placeid_api(address, key)
        placeid_value = self. get_url_from_json(url_api, parameter_data)
        return placeid_value
