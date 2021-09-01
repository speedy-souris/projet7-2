#coding:utf-8
#!/usr/bin/env python
"""main management menu"""

from grandpyRobot import GrandpyRobot
from question import Question
from conversationData import CreateConversationData
from internal_api_management import InternalApiConfig

class LoadUserConversation:
    """class for managing grandpy's responses according to user behavior """
    def __init__(self, user_question, db_number=0):
        """initializing attributes with redis data values"""
        self.user_question = user_question
        self.grandpy_message = GrandpyRobot()
        self.grandpy_code = ' '
        self.conversation_data = CreateConversationData(db_number=db_number)
        self.api_management = InternalApiConfig()
        try:
            self.has_grandpy_overdose_quotas =\
                self.conversation_data.read_conversation_data('grandpy_overdose_quotas')
        except TypeError:
            self.conversation_data.initialization_db_data()

        self.has_user_incivility = self.conversation_data.read_conversation_data('user_incivility')
        self.number_user_incivility =\
            self.conversation_data.read_conversation_data('number_user_incivility')
        self.number_user_request = self.conversation_data.read_conversation_data('number_user_request')
        self.has_user_indecency = self.conversation_data.read_conversation_data('user_indecency')
        self.number_user_indecency =\
            self.conversation_data.read_conversation_data('number_user_indecency')
        self.has_user_incomprehension = self.conversation_data.read_conversation_data('user_incomprehension')
        self.number_user_incomprehension =\
            self.conversation_data.read_conversation_data('number_user_incomprehension')

    def manage_user_incivility_behavior(self):
        """Management of user incivility"""
        user = Question(self.user_question)
        # reassessment of the state
        #so as not to reset incivility
        #after "hello from the user"
        if self.has_user_incivility:
            self.has_user_incivility = user.establishing_user_incivility_data()
        # treatment of incivility
        if self.has_user_incivility:
            self.number_user_incivility += 1
            self.grandpy_code = 'mannerless'
            if self.number_user_incivility >= 3:
                self.number_user_incivility = 3
                self.has_grandpy_overdose_quotas = True
                self.grandpy_code = 'incivility_limit'
        elif self.has_user_incivility == 3:
            self.grandpy_code = 'user_question'

    def increment_user_request_counter(self):
        """Management of the number of user requests"""
        if not self.has_user_incivility:
            self.number_user_request += 1
            if self.number_user_request >= 10:
                self.number_user_request = 10
                self.has_grandpy_overdose_quotas = True
                self.grandpy_code = 'exhausted'
            elif 1 <= self.number_user_request <= 4 or 6 <= self.number_user_request <= 9:
                self.grandpy_code = 'response'
                self.grandpy_code = 'user_question'
            elif self.number_user_request == 5:
                self.grandpy_code = 'tired'

    def manage_user_indecency_behavior(self):
        """Management of user indecency"""
        user = Question(self.user_question)
        self.has_user_indecency = user.establishing_user_indecency_data()
        if self.has_user_indecency:
            self.number_user_indecency += 1
            self.grandpy_code = 'disrespectful'
            if self.number_user_indecency >= 3:
                self.number_user_indecency = 3
                self.has_grandpy_overdose_quotas = True
                self.grandpy_code = 'indecency_limit'

    def manage_user_incomprehension_behavior(self):
        """Management of user incomprehension"""
        user = Question(self.user_question)
        self.has_user_incomprehension = user.establishing_user_incomprehension_data()
        if self.has_user_incomprehension:
            self.number_user_incomprehension += 1
            self.grandpy_code = 'incomprehension'
            if self.number_user_incomprehension >= 3:
                self.number_user_incomprehension = 3
                self.has_grandpy_overdose_quotas = True
                self.grandpy_code = 'incomprehension_limit'

# Main script
def main(user_question, db_number=0):
    """Management of the discussion between grandpy robot and a user"""
    user_conversation_data = LoadUserConversation(user_question, db_number=db_number)
    user_conversation_data.grandpy_code = 'home'
    user_conversation_data.manage_user_incivility_behavior()
    user_conversation_data.increment_user_request_counter()
    user_conversation_data.manage_user_indecency_behavior()
    user_conversation_data.manage_user_incomprehension_behavior()
    # ~ user_conversation_data.api_management.wiki_pages(user_question)
    user_conversation_data.conversation_data.update_db_data(user_conversation_data)
    return user_conversation_data




