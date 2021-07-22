#coding:utf-8
#!/usr/bin/env python

from main import main

class TestMain:
    def setup_method(self):
        self.correct_behavior = main('bonjour', db_number=1)
        self.incorrect_behavior = main('vieux', db_number=1)

    def test_user_behavior_after_home_message(self):
        expected_behavior_result = False
        behavior_result = self.correct_behavior
        assert expected_behavior_result == behavior_result.user_incivility

        expected_behavior_result = True
        behavior_result = self.incorrect_behavior
        assert expected_behavior_result == behavior_result.user_incivility

    def test_number_user_incivility_to_X3(self):
        expected_number_user_incivility_result = 3
        self.incorrect_behavior
        self.incorrect_behavior
        number_user_incivility_result = self.incorrect_behavior
        assert expected_number_user_incivility_result ==\
            number_user_incivility_result.number_user_incivility



