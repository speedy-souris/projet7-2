#coding:utf-8
#!/usr/bin/env python
"""main management menu"""

from grandpyRobot import GrandpyRobot
from question import Question
from conversationData import CreateConversationData

class UserConversation:
    def __init__(self, user_question, db_number=0):
        self.user_question = user_question
        self.grandpy = GrandpyRobot()
        self.conversation_data = CreateConversationData(db_number=db_number)
        try:
            self.user_incivility = self.conversation_data.read_conversation_data('user_incivility')
        except TypeError:
            self.conversation_data.initialization_db_data()
        self.number_user_incivility = 0

    def user_behavior(self):
        user = Question(self.user_question)
        self.user_incivility = user.establishing_user_incivility_data()

    # Main script
    def main(self):
        grandpy_response = self.grandpy.grandpy_data_of_message('home')
        self.user_behavior()
        self.conversation_data.write_conversation_data('user_incivility', self.user_incivility)
        return self.user_incivility

