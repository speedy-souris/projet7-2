#coding:utf-8
#!/usr/bin/env python

from question import Question

class TestQuestion:
    def setup_method(self):
        self.user_question_bonjour = Question('bonjour')

    def test_establishing_user_incivility_data(self):
        question_1 = self.user_question_bonjour
        expected_result = False
        result = question_1.establishing_user_incivility_data()
        assert expected_result == result
