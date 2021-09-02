#coding:utf-8
#!/usr/bin/env python

import requests
from google_api_config import GoogleApiData

class TestGoogleApi:
    def setup_method(self):
        self.google_api_data = GoogleApiData()

    def test_get_identifier_geolocated_address(self, monkeypatch):
        identifier_expected = {
            'candidates': [{
                'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
            }],
            'status' : 'OK'
        }
        mock_result = identifier_expected
        mockreturn = self.google_api_data.mock_params.get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        identifier_result = self.google_api_data.get_placeid_from_address('openClassrooms')
        assert identifier_expected == identifier_result

        identifier_expected = {
            'candidates': [],
            'status' : 'ZERO_RESULTS'
        }
        mock_result = identifier_expected
        mockreturn = self.google_api_data.mock_params.get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        identifier_result = self.google_api_data.get_placeid_from_address('rueopenClassRooms')
        assert identifier_expected == identifier_result

        identifier_expected = {
            'candidates' : [],
            'error_message' : 'This API key is not authorized to use this service or API.',
            'status' : 'REQUEST_DENIED'
        }
        mock_result = identifier_expected
        mockreturn = self.google_api_data.mock_params.get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        identifier_result =\
            self.google_api_data.get_placeid_from_address('openClassrooms')
        assert identifier_expected == identifier_result

    def test_geolocated_api_address(self, monkeypatch):
        address_api_expected = {
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
        mock_result = address_api_expected
        mockreturn = self.google_api_data.mock_params.get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        address_api_result =\
            self.google_api_data.get_address_api_from_placeid('ChIJIZX8lhRu5kcRGwYk8Ce3Vc8')
        assert address_api_expected == address_api_result

        address_api_expected = {
           'error_message' : 'This API key is not authorized to use this service or API.',
           'html_attributions' : [],
           'status' : 'REQUEST_DENIED'
        }
        mock_result = address_api_expected
        mockreturn = self.google_api_data.mock_params.get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        address_api_result =\
            self.google_api_data.get_address_api_from_placeid('ChIJIZX8lhRu5kcRGwYk8Ce3Vc8')
        assert address_api_expected == address_api_result

        address_api_expected = {
           'html_attributions': [],
            'status': 'INVALID_REQUEST'
        }
        mock_result = address_api_expected
        mockreturn = self.google_api_data.mock_params.get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        address_api_result =\
            self.google_api_data.get_address_api_from_placeid('ChIJky12Zn3p9EcREQI4zzdgzbk')
        assert address_api_expected == address_api_result





