#coding:utf-8
#!/usr/bin/env python

import requests
from apiData import ApiDataConfig
from google_api_config import GoogleApiData

def get_mockreturn(result):
    def mock_get(url, params):
        class JsonResponse:
            @staticmethod
            def json():
                return result
        return JsonResponse()
    return mock_get

class TestGoogleApi:
    def setup_method(self):
        self.google_api_data = GoogleApiData()
        self.google_api_config = ApiDataConfig()
        self.api_keys = self.google_api_config.read_internal_google_api_keys()
        self.key_map = self.api_keys[0]
        self.key_static_map = self.api_keys[1]

    def test_get_identifier_geolocated_address(self, monkeypatch):
        identifier_expected = {
            'candidates': [{
                'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
            }],
            'status' : 'OK'
        }
        mock_result = identifier_expected
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)

        identifier_result = self.google_api_data.get_placeid_from_address('openClassrooms', self.key_map)
        assert identifier_expected == identifier_result

        identifier_expected = {
            'candidates': [],
            'status' : 'ZERO_RESULTS'
        }
        mock_result = identifier_expected
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)

        identifier_result = self.google_api_data.get_placeid_from_address('rueopenClassRooms', self.key_map)
        assert identifier_expected == identifier_result
        
        identifier_expected = {
            'candidates' : [],
            'error_message' : 'This API key is not authorized to use this service or API.',
            'status' : 'REQUEST_DENIED'
        }
        mock_result = identifier_expected
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        
        identifier_result =\
            self.google_api_data.get_placeid_from_address('openClassrooms', self.key_static_map)
        assert identifier_expected == identifier_result
