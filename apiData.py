#coding:utf-8
#!/usr/bin/env python
"""api data management menu"""

import os

class ApiDataConfig:
    """API data configuration
       With the read_internal_google_api_keys method 
       which determines the use of private keys for the GoogleMap API 
       in relation to a local or production environment .
       With the get_google_api_data method 
       which determines the use of a specific private key according 
       to the GoogleMap API used GoogleMap / static GoogleMap (address display / map display)"""
    def __init__(self):
        self.key_map = ' '
        self.key_static_map = ' '
        self.has_status_prod = None

    def read_internal_google_api_keys(self):
        """Internal Key Management Local / Production
           HEROKU_KEY_API_MAP / HEROKU_KEY_API_STATIC_MAP 
           contain the private keys of GoogleMap APIs used in production environment .
           KEY_API_MAP / KEY_API_STATIC_MAP 
           contain the private keys of GoogleMap APIs used in local environment"""
        if os.environ.get('HEROKU_KEY_API_MAP') is None: # local internal key
            self.key_map = os.getenv('KEY_API_MAP')
            self.key_static_map = os.getenv('KEY_API_STATIC_MAP')
            self.status_prod = False
        else: # internal production key
            self.key_map = os.getenv('HEROKU_KEY_API_MAP')
            self.key_static_map = os.getenv('HEROKU_KEY_API_STATIC_MAP')
            self.status_prod = True

        return (self.key_map, self.key_static_map, self.status_prod)

    def get_google_api_data(self, data):
        """Get the production or local keys for the googleMap API
           as well as the production status ==> local / prod (False / True)
           Argument data 
                'map' ==> returns the private key of the GoogleMap API
                'static_map' ==> returns the private key of the static GoogleMap API
                'status' ==> returns False / True"""
        keys_api_value = self.read_internal_google_api_keys()
        if data == 'map':
            return keys_api_value[0]
        elif data == 'static_map':
            return keys_api_value[1]
        elif data == 'status':
            return keys_api_value[2]
