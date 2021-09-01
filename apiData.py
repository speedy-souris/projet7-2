#coding:utf-8
#!/usr/bin/env python
"""api data management menu"""

import os
import requests

class ApiDataConfig:
    """API data configuration"""
    def __init__(self):
        self.key_map = ' '
        self.key_static_map = ' '
        self.has_status_prod = None

    def read_internal_google_api_keys(self):
        """Internal Key Management Local / Production"""
        if os.environ.get('HEROKU_KEY_API_MAP') is None: # local internal key
            self.key_map = os.getenv('KEY_API_MAP')
            self.key_static_map = os.getenv('KEY_API_STATIC_MAP')
            self.status_prod = False
        else: # internal production key
            self.key_map = os.getenv('HEROKU_KEY_API_MAP')
            self.key_static_map = os.getenv('HEROKU_KEY_API_STATIC_MAP')
            self.status_prod = True

        return (self.key_map, self.key_static_map, self.status_prod)
