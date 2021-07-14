#coding:utf-8
#!/usr/bin/env python
"""main management menu"""

from grandpyRobot import GrandpyRobot
from question import Question

class GeneralBehavior:
    def __init__(self, user_question):
        self.user_question = user_question
        self.grandpy = GrandpyRobot()
        self.user_incivility = None
        self.number_user_incivility = 0

    def user_behavior(self):
        user = Question(self.user_question)
        self.user_incivility = user.establishing_user_incivility_data()

    # Main script
    def main(self):
        grandpy_response = self.grandpy.grandpy_data_of_message('home')
        self.user_behavior()
        return self.user_incivility

