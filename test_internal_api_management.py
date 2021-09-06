#coding:utf-8
#!/usr/bin/env python

import requests
from internal_api_management import InternalApiConfig

class TestInternalAPIManagement:
    def setup_method (self):
        self.user_question = 'openClassrooms'
        self.api_address_pages = InternalApiConfig()

    def test_api_address_pages(self, monkeypatch):
        expected_result1 = {
            'candidates': [{
                'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
            }],
            'status' : 'OK'
        }
        expected_result2 = {
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
        expected_result3 = {
            'query': {
                'geosearch': [
                    {
                        'pageid': 3120618, 'ns': 0, 'title': 'Quai de la Charente',
                        'lat': 48.895636, 'lon': 2.384586, 'dist': 226.3, 'primary': ''
                    }
                ]
            }
        }
        mock_result1 = expected_result1
        mock_result2 = expected_result2
        mock_result3 = expected_result3
        mockreturn =\
            self.api_address_pages.google_api.mock_params.get_mockreturn2(
                mock_result1, mock_result2, mock_result3
            )
        monkeypatch.setattr(requests, 'get', mockreturn)

        result = self.api_address_pages.wiki_address_pages(self.user_question)
        assert result == expected_result3
