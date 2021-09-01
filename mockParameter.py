#coding:utf-8
#!/usr/bin/env python
"""Mock data management"""

class MockData:
    """mock internal configuration
       Method 1
       mock configuration to simulate a single method call
       configuration using the get_mockreturn (result) method
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
    def get_url_from_json(url, params):
        """conversion of the address found in JSON format"""
        request = requests.get(url, params)
        url_json = request.json()
        return url_json
