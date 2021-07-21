#coding:utf-8
#!/usr/bin/env python

from main import UserConversation 

class TestMain:
    def setup_method(self):
        self.correct_behavior = UserConversation('bonjour', db_number=1)
        self.incorrect_behavior = UserConversation('vieux', db_number=1)

    def test_user_behavior_after_home_message(self):
        expected_behavior_result = False
        behavior_result = self.correct_behavior.main()
        assert expected_behavior_result == behavior_result

        expected_behavior_result = True
        behavior_result = self.incorrect_behavior.main()
        assert expected_behavior_result == behavior_result

    #def test_number_user_incivility_to_X3(self)
        #number_user_incivility_result = 3
        



