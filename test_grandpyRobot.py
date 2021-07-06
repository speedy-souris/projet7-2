#coding:utf-8
#!/usr/bin/env python

import grandpyRobot

class TestGrandpyRobot:
    def setup_method(self):
        self.grandpy = grandpyRobot.GrandpyRobot()

    def test_grandpy_data_message(self):
        expected_response_result =\
           "Bonjour Mon petit, en quoi puis-je t'aider ?"
        response_result =\
            self.grandpy.grandpy_data_of_message('home')

        assert expected_response_result ==\
            response_result
