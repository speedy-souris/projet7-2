#coding:utf-8
#!/usr/bin/env python

import requests
from apiData import ApiDataConfig
from wiki_media_api_config import WikiApiData

class TestWikiMediaAPi:
    def setup_method(self):
        self.wiki_api_config = ApiDataConfig()
        self.wiki_api_data = WikiApiData()

    def test_wiki_media_page_content(self, monkeypatch):
        mock_result =  {
            'query':
                {
                    'geosearch': [
                        {
                            'title': 'Quai de la Gironde'
                        },
                        {
                            'title': 'Parc du Pont de Flandre'
                        }
                    ]
                }
        }
        wiki_content_expected = mock_result
        mockreturn = self.wiki_api_config.get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)

        wiki_content_result = self.wiki_api_data.get_page_from_wiki_api(48.895636, 2.384586)
        assert wiki_content_result == wiki_content_expected


