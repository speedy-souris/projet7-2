#coding:utf-8
#!/usr

import pdb
from main import main

class TestMain:
    def setup_method(self):
        self.user_conversation_data = main('', db_number=1)
        self.user_conversation_data.conversation_data.initialization_db_data()

    def test_check_user_behavior_after_grandpy_home_message(self):
        has_expected_incivility_behavior = False
        grandpy_code_expected = 'user_question'
        user_conversation_data = main('bonjour', db_number=1)

        assert has_expected_incivility_behavior == user_conversation_data.has_user_incivility
        assert grandpy_code_expected == user_conversation_data.grandpy_code

        has_an_expected_incivility_behavior = False
        grandpy_code_expected = 'user_question'
        user_conversation_data = main('ou se trouve Openclassrooms', db_number=1)

        assert has_an_expected_incivility_behavior == user_conversation_data.has_user_incivility
        assert grandpy_code_expected == user_conversation_data.grandpy_code

    def test_count_number_of_user_incivility_up_to_3(self):
        number_of_expected_user_incivility = 3
        grandpy_code_expected = 'exhausted'

        for counter_user_incivility in range(1,3):
            main('ou se trouve Openclassrooms', db_number=1)
        user_conversation_data = main('ou se trouve Openclassrooms', db_number=1)

        assert number_of_expected_user_incivility == user_conversation_data.number_user_incivility
        assert grandpy_code_expected == user_conversation_data.grandpy_code

    def test_count_number_of_user_request_up_to_10(self):
        number_of_expected_user_request = 10
        main('bonjour', db_number=1)
        for counter_user_request in range(1,9):
            main('ou se trouve Openclassrooms', db_number=1)
        user_conversation_data = main('ou se trouve Openclassrooms', db_number=1)

        assert number_of_expected_user_request == user_conversation_data.number_user_request

