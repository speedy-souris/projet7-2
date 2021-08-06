#coding:utf-8
#!/usr/bin/env python

import requests
from apiData import ApiDataConfig
from wiki_media_api_config import WikiApiData

class TestWikiMediaAPi:
    def setup_method(self):
        self.wiki_api_config = ApiDataConfig()
        self.wiki_api_data = WikiApiData()

    def test_search_wiki_media_page(self, monkeypatch):
        wiki_page_expected = {
            'query': {
                'geosearch': [
                    {
                        'pageid': 3120618, 'ns': 0, 'title': 'Quai de la Charente',
                        'lat': 48.895636, 'lon': 2.384586, 'dist': 226.3, 'primary': ''
                    }
                ]
            }
        }
        mock_result = wiki_page_expected
        mockreturn = self.wiki_api_config.get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)

        wiki_page_result = self.wiki_api_data.get_page_from_wiki_api(48.895636, 2.384586)
        assert wiki_page_result == wiki_page_expected

        wiki_page_expected = {
            'query': {
                'geosearch': [
                    {
                        'title': 'Bouée Soul'
                    },
                    {
                        'title': 'Null Island'
                    }
                ]
            }
        }
        mock_result = wiki_page_expected
        mockreturn = self.wiki_api_config.get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)

        wiki_page_result = self.wiki_api_data.get_page_from_wiki_api(0, 0)
        assert wiki_page_result == wiki_page_expected

