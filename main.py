#coding:utf-8
#!/usr/bin/env python
"""main management menu"""

from grandpyRobot import GrandpyRobot
from question import Question
from conversationData import CreateConversationData

class LoadUserConversation:
    def __init__(self, user_question, db_number=0):
        self.user_question = user_question
        self.grandpy_message = GrandpyRobot()
        self.grandpy_code = ' '
        self.conversation_data = CreateConversationData(db_number=db_number)
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

    def manage_user_incivility_behavior(self):
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
        user = Question(self.user_question)
        self.has_user_indecency = user.establishing_user_indecency_data()
        if self.has_user_indecency:
            self.number_user_indecency += 1
            self.grandpy_code = 'disrespectful'
            if self.number_user_indecency >= 3:
                self.number_user_indecency = 3
                self.has_grandpy_overdose_quotas = True
                self.grandpy_code = 'indecency_limit'

# Main script
def main(user_question, db_number=0):
    user_conversation_data = LoadUserConversation(user_question, db_number=db_number)
    user_conversation_data.grandpy_code = 'home'
    user_conversation_data.manage_user_incivility_behavior()
    user_conversation_data.increment_user_request_counter()
    user_conversation_data.manage_user_indecency_behavior()
    user_conversation_data.conversation_data.update_db_data(user_conversation_data)
    return user_conversation_data




