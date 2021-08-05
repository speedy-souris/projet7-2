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
        grandpy_code_expected = 'incivility_limit'

        for counter_user_incivility in range(1,3):
            main('ou se trouve Openclassrooms', db_number=1)
        user_conversation_data = main('ou se trouve Openclassrooms', db_number=1)

        assert number_of_expected_user_incivility == user_conversation_data.number_user_incivility
        assert grandpy_code_expected == user_conversation_data.grandpy_code

    def test_count_number_of_user_request_up_to_10(self):
        number_of_expected_user_request = 10
        grandpy_code_expected = 'exhausted'
        main('bonjour', db_number=1)
        for counter_user_request in range(1,10):
            main('ou se trouve Openclassrooms', db_number=1)
        user_conversation_data = main('ou se trouve Openclassrooms', db_number=1)

        assert number_of_expected_user_request == user_conversation_data.number_user_request
        assert grandpy_code_expected == user_conversation_data.grandpy_code

    def test_count_number_of_user_request_equal_to_5(self):
        number_of_expected_user_request = 5
        grandpy_code_expected = 'tired'
        main('bonjour', db_number=1)
        for counter_user_request in range(1,4):
            main('ou se trouve Openclassrooms', db_number=1)
        user_conversation_data = main('ou se trouve Openclassrooms', db_number=1)

        assert number_of_expected_user_request == user_conversation_data.number_user_request
        assert grandpy_code_expected == user_conversation_data.grandpy_code

    def test_count_number_of_user_indecency_up_to_3(self):
        number_of_expected_user_indecency = 3
        grandpy_code_expected = 'indecency_limit'
        main('bonjour', db_number=1)
        for counter_user_indecency in range(1,3):
            main('vieux', db_number=1)
        user_conversation_data = main('vieux', db_number=1)

        assert number_of_expected_user_indecency == user_conversation_data.number_user_indecency
        assert grandpy_code_expected == user_conversation_data.grandpy_code
    
    def test_count_number_of_user_incomprehension_up_to_3(self):
        number_of_expected_user_incomprehension = 3
        grandpy_code_expected = 'incomprehension_limit'
        main('bonjour', db_number=1)
        for counter_user_indecency in range(1,3):
            main('XXXX', db_number=1)
        user_conversation_data = main('XXXX', db_number=1)

        assert number_of_expected_user_incomprehension == user_conversation_data.number_user_incomprehension
        assert grandpy_code_expected == user_conversation_data.grandpy_code
