#coding:utf-8
#!/usr/bin/env python

import redis
from frozendict import frozendict

class CreateConversationData:
    def __init__(self, db_number=0):
        """database initialization"""
        self.chat_bdAccess = self.get_database_access(db_number=db_number)

    @staticmethod
    def boolean_to_string_conversion(value):
        """conversion from boolean to string"""
        if value :
            value = 'True'
        else:
            value = 'False'
        return value

    @staticmethod
    def string_to_boolean_conversion(value):
        """conversion from string to boolean"""
        if value == b'False':
            value = False
        elif value == b'True':
            value = True
        else:
            value = False
        return value

    @staticmethod
    def string_to_int_conversion(value):
        """conversion from string to integer"""
        return int(value)

    def get_database_access(self, db_number=0):
        """method for data_connection to the database
           db_number arg = 0 ==> Redis connect 'dev'
           db_number arg = 1 ==> Redis connect 'test'"""
        redis_connect = redis.Redis(
            host='localhost',
            port=6379,
            db=db_number
        )
        return redis_connect

    @property
    def read_conversation_data(self, db_data):
        """reading the value of conversation in db_data"""
        chat_data_value = frozendict({
            'user_incivility': self.string_to_boolean_conversion(
                self.chat_dbAccess.get('user_incivility')
            )
        })
        return chat_data_value[db_data]

    def write_conversation_data(self, script_data, script_data_value):
        """writing the value of conversation in db_data"""
        chat_data_value = frozendict({
            script_data: self.chat_bdAccess.set (
                script_data, self.boolean_to_string_conversion(script_data_value)
            )
        })
        return chat_data_value[script_data]
    
    def initialization_db_data(self):
        self.chat_bdAccess.flushall()
        self.write_conversation_data('user_incivility', None)

