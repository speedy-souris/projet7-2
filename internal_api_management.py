#coding:utf-8
#!/usr/bin/env python
"""api internal data management menu"""

from google_api_config import GoogleApiData
from wiki_media_api_config import WikiApiData

class InternalApiConfig:
    """methods for the internal management of APIs"""
    def __init__(self):
        self.google_api = GoogleApiData()
        self.wikimedia_api = WikiApiData()

    def wiki_pages(self, user_question):
        """searches for pages on the WikiMedia API
        with the location coordinates requested by the user
        (after the parser)
        call get_placeid_from_address method
        call get_address_api_from_placeid method
        both from GoogleApiData class of the module google_api_config
        call get_page_from_wiki_api method
        from WikiApiData class of the module wiki_media_api_config
        example :
        user_question = 'openClassrooms'
        get_place_id_from_address = {
           'candidates': [
              {
                 'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
              }
           ],
           'status' : 'OK'
        }
        get_address_api_from_placeid = {
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
        get_page_from_wiki_api = {
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
        place_id_research = self.google_api.get_placeid_from_address(user_question)
        try:
            place_id = place_id_research['candidates'][0]['place_id']
        except IndexError:
            return {}
        address_api = self.google_api.get_address_api_from_placeid(place_id)
        latitude = address_api['result']['geometry']['location']['lat']
        longitude = address_api['result']['geometry']['location']['lng']
        wiki_pages = self.wikimedia_api.get_page_from_wiki_api(latitude, longitude)
        return wiki_pages

if __name__ == '__main__':
    api = InternalApiConfig()
    print(api.wiki_pages('openClassrooms'))
