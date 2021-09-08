#coding:utf-8
#!/usr/bin/env python
"""google api config management menu"""
import requests
from apiData import ApiDataConfig
from mockParameter import MockData

class GoogleApiData:
    """management of Google APIs settings"""
    def __init__(self):
        self.google_api_config = ApiDataConfig()
        self.mock_params = MockData()
        self.api_keys = self.google_api_config.read_internal_google_api_keys()
        self.key_map = self.api_keys[0]
        self.key_static_map = self.api_keys[1]

    def get_settings_for_placeid_api(self, address):
        """determining placeid for the address found"""
        key = self.key_map
        parameters = {
            'input': f'{address}',
            'inputtype': 'textquery',
            'key': f'{key}'
        }
        return parameters

    def get_settings_for_address_api(self, placeid):
        """determining the localized address for the found placeid"""
        key = self.key_map
        parameters = {
            'placeid': f'{placeid}',
            'fields': 'formatted_address,geometry',
            'key': f'{key}'
        }
        return parameters

    def get_settings_for_map_static_api(self, address, localization):
        """determination of the static map for the address found"""
        key = self.key_map
        markers_data =\
            f"color:red|label:A|{localization['lat']},"\
            f"{localization['lng']}"
        parameters = {
            'center': f'{address}',
            'zoom': '18.5',
            'size': '600x300',
            'maptype': 'roadmap',
            'markers': f'{markers_data}',
            'key': f'{key}'
        }
        return parameters

    def get_placeid_from_address(self, address):
        """Google map API place_id search function
        Result ok with address to 'openClassrooms'
        {
           'candidates': [
              {
                 'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
              }
           ],
           'status' : 'OK'
        }
        """
        url_api = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
        parameter_data = self.get_settings_for_placeid_api(address)
        placeid_value = self.mock_params.get_url_from_json(url_api, parameter_data)
        return placeid_value

    def get_address_api_from_placeid(self, placeid):
        """Google map API address search with place_id function
            Result OK with place_id 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
            {
                'html_attributions': [],
                'result': {
                    'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                    'geometry': {
                        'location': {'lat': 48.8975156, 'lng': 2.3833993},
                        'viewport': {
                            'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                            'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}}}},
                'status': 'OK'
            }
        """
        url_api = 'https://maps.googleapis.com/maps/api/place/details/json'
        parameter_data = self.get_settings_for_address_api(placeid)
        address_api_value = self.mock_params.get_url_from_json(url_api, parameter_data)
        return address_api_value

    def get_static_map_from_address_api(self, address, localization):
        """Display of the static map at the user's request"""
        url_api = 'https://maps.googleapis.com/maps/api/staticmap'
        parameter_data = self.get_settings_for_map_static_api(address, localization)
        map_static_api = requests.get(url=url_api, params=parameter_data)
        return map_static_api

if __name__ == '__main__':
    data_api = GoogleApiData()
    address = data_api.get_placeid_from_address('openClassrooms')
    print(f'\n address {address}')
    address_from_placeid = address['candidates'][0]['place_id']
    placeid = data_api.get_address_api_from_placeid(address_from_placeid)
    print(f'\nplace_id = {placeid}\n')
