#coding:utf-8
#!/usr/bin/env python
"""main management menu"""

from grandpyRobot import GrandpyRobot
from question import Question
from conversationData import CreateConversationData

class UserConversation:
    def __init__(self, user_question, db_number=0):
        self.user_question = user_question
        self.grandpy_message = GrandpyRobot()
        self.grandpy_code = ' '
        self.conversation_data = CreateConversationData(db_number=db_number)
        try:
            self.grandpy_overdose_quotas =\
                self.conversation_data.read_conversation_data('grandpy_overdose_quotas')
        except TypeError:
            self.conversation_data.initialization_db_data()

        self.user_incivility = self.conversation_data.read_conversation_data('user_incivility')
        self.number_user_incivility =\
            self.conversation_data.read_conversation_data('number_user_incivility')

    def user_incivility_behavior(self):
        user = Question(self.user_question)
        self.user_incivility = user.establishing_user_incivility_data()
        if self.user_incivility:
            self.number_user_incivility += 1
            print(f"\nGrandpy repond {self.grandpy_message.grandpy_data_of_message('mannerless')}")
            self.grandpy_code = 'mannerless'
            if self.number_user_incivility >= 3:
                self.number_user_incivility = 3
                self.grandpy_overdose_quotas = True
                self.grandpy_code = 'incivility_limit'
                print(f"\nGrandpy répond {self.grandpy_message.grandpy_data_of_message('incivility_limit')}")
                self.grandpy_code = 'exhausted'
                print(f"               {self.grandpy_message.grandpy_data_of_message('exhausted')}")
        else:
            self.grandpy_code = 'user_question'

# Main script
def main(user_question, db_number=0):
    user_conversation_data = UserConversation(user_question, db_number=db_number)
    user_conversation_data.grandpy_code = 'home'
    user_conversation_data.user_incivility_behavior()
    user_conversation_data.conversation_data.update_db_data(user_conversation_data)
    return user_conversation_data



