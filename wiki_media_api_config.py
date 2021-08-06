#coding:utf-8
#!/usr/bin/env python
"""wikiMedia api config management menu"""

from apiData import ApiDataConfig

class WikiApiData:
    """management of WikiMedia APIs settings"""
    def __init__(self):
        self.wikimedia_api_config = ApiDataConfig()

    @staticmethod
    def get_url_parameters_for_wiki_api_page_localization(latitude, longitude):
        """data for wiki page localization url"""
        parameters = {
            'action': 'query',
            'list': 'geosearch',
            'gscoord': f'{latitude}|{longitude}',
            'gslimit': '10',
            'gsradius': '10000',
            'format': 'json'
        }
        return parameters

    def get_page_from_wiki_api(self, latitude, longitude):
        """A.P.I wikipedia function that returns a file
            Json containing the history of the requested address
        {
            'query': {
                'geosearch': [
                    {
                        'pageid': 3120618, 'ns': 0, 'title': 'Quai de la Charente',
                        'lat': 48.895636, 'lon': 2.384586, 'dist': 226.3, 'primary': ''
                    }
                ]
            }
        }
        """
        url_api = 'https://fr.wikipedia.org/w/api.php'
        parameter_data = self.get_url_parameters_for_wiki_api_page_localization(latitude, longitude)
        page_wiki = self.wikimedia_api_config.get_url_from_json(url_api, parameter_data)
        return page_wiki
