#coding:utf-8
#!/usr/bin/env python
"""Mock data management"""
import requests

class MockData:
    """mock internal configuration
       Method 1
       mock configuration to simulate a single method call
       configuration using the get_mockreturn(result) method .
       Method 2
       mock configuration to simulate a multi methode call
       configuration using the get_mockreturn2(result1, result2, result3) method .
       The get_url_from_json method converts the url of an API to JSON format
       """
    # Method 1 
    @staticmethod
    def get_mockreturn(result):
        def mock_get(url, params):
            class JsonResponse:
                @staticmethod
                def json():
                    return result
            return JsonResponse()
        return mock_get

    # Method 2
    def get_mockreturn2(self, result1, result2, result3):
        def mock_get(url, params):
            class JsonResponse:
                @staticmethod
                def json():
                    if 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json' in url:
                        return result1
                    elif 'https://maps.googleapis.com/maps/api/place/details/json' in url:
                        return result2
                    elif 'https://fr.wikipedia.org/w/api.php' in url:
                        return result3
            return JsonResponse()
        return mock_get

    @staticmethod
    def get_url_from_json(url, params):
        """conversion of the address found in JSON format"""
        request = requests.get(url, params)
        url_json = request.json()
        return url_json
