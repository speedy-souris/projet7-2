#coding:utf-8
#!/usr/bin/env python

import main

class TestMain:
    def setup_method(self):
        self.correct_behavior = main.main('bonjour')

    def test_user_behavior_after_home_message(self):
        expected_behavior_result = True
        behavior_result = self.correct_behavior.user_behavior()

        assert expected_behavior_result == behavior_result




