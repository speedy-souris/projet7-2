#coding:utf-8
#!/usr/bin/env python

from main import main

class TestMain:
    def setup_method(self):
        self.user_conversation_data = main('', db_number=1)
        self.user_conversation_data.conversation_data.initialization_db_data()

    def test_check_user_behavior_after_grandpy_home_message(self):
        has_expected_incivility_behavior = False
        grandpy_code_expected = 'user_question'
        has_user_incivility_behavior_been_detected = main('bonjour', db_number=1)

        user_incivility_has_been_detected = has_user_incivility_behavior_been_detected.user_incivility
        assert has_expected_incivility_behavior == user_incivility_has_been_detected

        code_grandpy_has_been_detected = has_user_incivility_behavior_been_detected.grandpy_code
        assert grandpy_code_expected == code_grandpy_has_been_detected

        has_an_expected_incivility_behavior = True
        grandpy_code_expected = 'mannerless'
        has_user_incivility_behavior_been_detected = main('ou se trouve Openclassrooms', db_number=1)

        user_incivility_has_been_detected = has_user_incivility_behavior_been_detected.user_incivility
        assert has_an_expected_incivility_behavior == user_incivility_has_been_detected

        code_grandpy_has_been_detected = has_user_incivility_behavior_been_detected.grandpy_code
        assert grandpy_code_expected == code_grandpy_has_been_detected

    def test_count_number_of_user_incivility_up_to_3(self):
        number_of_expected_user_incivility = 3
        grandpy_code_expected = 'exhausted'

        main('ou se trouve Openclassrooms', db_number=1)
        main('ou se trouve Openclassrooms', db_number=1)
        has_user_incivility_behavior_been_detected = main('ou se trouve Openclassrooms', db_number=1)

        number_user_incivility_has_been_detected =\
            has_user_incivility_behavior_been_detected.number_user_incivility
        assert number_of_expected_user_incivility == number_user_incivility_has_been_detected

        grandpy_code_displayed = has_user_incivility_behavior_been_detected.grandpy_code
        assert grandpy_code_expected == grandpy_code_displayed

