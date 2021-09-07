#coding:utf-8
#!/usr/bin/env python
"""Mock data management"""
import os
import requests

class MockData:
    """mock internal configuration
       Method 1
       mock configuration to simulate a single method call
       configuration using the get_mockreturn(result) method
       ----------
       Methode 2
       mock configuration to simulate a multi method call
       configuration using the get_mockreturn2(result1, result2, result3) method
    """

    @staticmethod
    def get_mockreturn(result):
        def mock_get(url, params):
            class JsonResponse:
                @staticmethod
                def json():
                    return result
            return JsonResponse()
        return mock_get

    def get_mockreturn2(self, result1, result2, result3):
        def mock_get(url, params):
            class JsonResponse:
                def __init__(self):
                    self.key_map = os.getenv('KEY_API_MAP')
                    self.key_satic_map = os.getenv('KEY_API_STACTIC_MAP')
            
                    self.url1 =\
                        'https://maps.googleapis.com/maps/api/place/findplacefromtext/json\
                         /input=openClassrooms/inputtype=testquery/key=self.key_map'
            
                    self.url2 = 'https://maps.googleapis.com/maps/api/place/details/json\
                                 /placeid=ChIJIZX8lhRu5kcRGwYk8Ce3Vc8/fields=formatted_address,geometry/key=self.key_map'
            
                    self.url3 = 'https://maps.googleapis.com/maps/api/staticmap/center=10%20Quai%20de%20laCharente,\
                                 %2075019%20Paris,%20France/zoom=18.5/size=600x300/maptype=roadmap\
                                 /markers=color=red|label=A|48.8975156,2.3833993/key=self.key_static_map'
                def json(self):
                    if url == self.url1:
                        return result1
                    elif url == self.url2:
                        return result2
                    elif url == self.url3:
                        return result3
            return JsonResponse()
        return mock_get

    @staticmethod
    def get_url_from_json(url, params):
        """conversion of the address found in JSON format"""
        request = requests.get(url, params)
        url_json = request.json()
        return url_json
