#coding:utf-8
#!/usr/bin/env python

from main import GeneralBehavior as script

class TestMain:
    def setup_method(self):
        self.correct_behavior = script('bonjour')
        self.incorrect_behavior = script('vieux')

    def test_user_behavior_after_home_message(self):
        expected_behavior_result = False
        behavior_result = self.correct_behavior.main()
        assert expected_behavior_result == behavior_result

        expected_behavior_result = True
        behavior_result = self.incorrect_behavior.main()
        assert expected_behavior_result == behavior_result




