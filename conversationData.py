#coding:utf-8
#!/usr/bin/env python

import redis
from frozendict import frozendict

class CreateConversationData:
    def __init__(self, db_number=0):
        """database initialization"""
        self.chat_dbAccess = self.get_database_access(db_number=db_number)

    @staticmethod
    def boolean_to_string_conversion(boolean_value):
        """conversion from boolean to string"""
        if boolean_value :
            boolean_value = 'True'
        else:
            boolean_value = 'False'
        return boolean_value

    @staticmethod
    def string_to_boolean_conversion(string_value):
        """
            conversion from string to boolean
        """
        if string_value == b'False':
            string_value = False
        elif string_value == b'True':
            string_value = True
        else:
            string_value = False
        return string_value

    @staticmethod
    def string_to_int_conversion(string_value):
        """conversion from string to integer"""
        return int(string_value)

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

    def read_conversation_data(self, db_data):
        """reading the value of conversation in db_data"""
        chat_data_value = frozendict({
            'user_incivility': self.string_to_boolean_conversion(self.chat_dbAccess.get('user_incivility')),
            'number_user_incivility': self.string_to_int_conversion(
                self.chat_dbAccess.get('number_user_incivility')
            ),
            'grandpy_overdose_quotas': self.string_to_boolean_conversion(
                self.chat_dbAccess.get('grandpy_overdose_quotas')
            ),
            'number_user_request': self.string_to_int_conversion(
                self.chat_dbAccess.get('number_user_request')
            ),
            'user_indecency': self.string_to_boolean_conversion(self.chat_dbAccess.get('user_indecency')),
            'number_user_indecency': self.string_to_int_conversion(
                self.chat_dbAccess.get('number_user_indecency')
            ),
        })
        return chat_data_value[db_data]

    def write_conversation_data(self, script_data, script_data_value):
        """writing the value of conversation in db_data"""
        self.chat_dbAccess.set(script_data, script_data_value)

    def initialization_db_data(self):
        self.chat_dbAccess.flushall()
        self.write_conversation_data('user_incivility', self.boolean_to_string_conversion(True))
        self.write_conversation_data('number_user_incivility', 0)
        self.write_conversation_data('grandpy_overdose_quotas', self.boolean_to_string_conversion(False))
        self.write_conversation_data('number_user_request',0)
        self.write_conversation_data('user_indecency', self.boolean_to_string_conversion(True))
        self.write_conversation_data('number_user_indecency', 0)

    def update_db_data(self, conversation):
        self.write_conversation_data(
            'user_incivility',\
            self.boolean_to_string_conversion(conversation.has_user_incivility)
        )
        self.write_conversation_data(
            'number_user_incivility', conversation.number_user_incivility
        )
        if conversation.has_grandpy_overdose_quotas:
            self.chat_dbAccess.expire('grandpy_overdose_quotas', 60)
        else:
            self.write_conversation_data(
                'grandpy_overdose_quotas',\
                self.boolean_to_string_conversion(conversation.has_grandpy_overdose_quotas)
        )
        self.write_conversation_data(
            'number_user_request', conversation.number_user_request
        )
        self.write_conversation_data(
            'user_indecency',\
            self.boolean_to_string_conversion(conversation.has_user_indecency)
        )
        self.write_conversation_data(
            'number_user_indecency', conversation.number_user_indecency
        )
