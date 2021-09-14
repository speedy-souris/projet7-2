#coding:utf-8
#!/usr/bin/env python

import requests
from wiki_media_api_config import WikiApiData

class TestWikiMediaAPi:
    def setup_method(self):
        self.wiki_api_data = WikiApiData()

    def test_wiki_media_api_config(self, monkeypatch):
        wiki_content_expected =  {
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
        mock_result = wiki_content_expected
        mockreturn = self.wiki_api_data.google_mock.mock_params.get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)

        wiki_content_result = self.wiki_api_data.get_pages_from_wiki_api(48.895636, 2.384586)
        assert mock_result == wiki_content_result


