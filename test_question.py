#coding:utf-8
#!/usr/bin/env python

from question import Question

class TestQuestion:
    def setup_method(self):
        self.user_question_bonjour = Question('bonjour')
        self.user_question_empty = Question('')
        self.user_question_openClassrooms =\
            Question('ou se trouve openClassrooms ?')

    def test_establishing_user_incivility_data(self):
        question_1 = self.user_question_bonjour
        expected_result = False
        result = question_1.establishing_user_incivility_data()
        assert expected_result == result

        question_1 = self.user_question_empty
        expected_result = True
        result = question_1.establishing_user_incivility_data()
        assert expected_result == result

        question_1 = self.user_question_openClassrooms
        expected_result = True
        result = question_1.establishing_user_incivility_data()
        assert expected_result == result

        question_1 = Question('Bonjour Grandpy')
        expected_result = False
        result = question_1.establishing_user_incivility_data()
        assert expected_result == result

    def test_establishing_user_indecency_data(self):
        question_1 = Question('vieille baderne')
        expected_result = True
        result = question_1.establishing_user_indecency_data()
        assert expected_result == result

        question_1 = self.user_question_empty
        expected_result = False
        result = question_1.establishing_user_indecency_data()
        assert expected_result == result

        question_1 = Question('Bonjour')
        expected_result = False
        result = question_1.establishing_user_indecency_data()
        assert expected_result == result

    def test_establishing_user_incomprehension_data(self):
        question_1 = Question('xxxx')
        expected_result = True
        result = question_1.establishing_user_incomprehension_data()
        assert expected_result == result
        
        question_1 = self.user_question_bonjour
        expected_result = False
        result = question_1.establishing_user_incomprehension_data()
        assert expected_result == result
