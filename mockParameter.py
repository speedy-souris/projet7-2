#coding:utf-8
#!/usr/bin/env python
"""Mock data management"""
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

    @staticmethod
    def get_mockreturn2(result1, result2, result3):
        def mock_get(url, params):
            class JsonResponse:
                @staticmethod
                def json():
                    if url == result1:
                        return result1
                    elif url == result2:
                        return result2
                    else:
                        return result3
            return JsonResponse()
        return mock_get

    @staticmethod
    def get_url_from_json(url, params):
        """conversion of the address found in JSON format"""
        request = requests.get(url, params)
        url_json = request.json()
        return url_json
