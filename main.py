#coding:utf-8
#!/usr/bin/env python
"""main management menu"""

from grandpyRobot import GrandpyRobot
from question import Question

def user_behavior(user_question):
    user = Question(user_question)
    return user.establishing_user_incivility_data()

# Main script
def main(user_question):
    grandpy = GrandpyRobot()
    grandpy.grandpy_data_of_message('home')
    return user_behavior(user_question)
