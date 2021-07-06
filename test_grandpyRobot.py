#coding:utf-8
#!/usr/bin/env python

import grandpyRobot

class TestGrandpyRobot:
    def setup_method(self):
        self.grandpy = grandpyRobot.GrandpyRobot()

    def test_grandpy_data_message(self):
        expected_response_result = "Bonjour Mon petit, en quoi puis-je t'aider ?"
        response_result = self.grandpy.grandpy_data_of_message('home')
        assert expected_response_result == response_result

        expected_response_result = 'As tu une nouvelle question a me demander ?'
        response_result = self.grandpy.grandpy_data_of_message('user_question')
        assert expected_response_result == response_result

        expected_response_result = 'Voici Ta Réponse à la question !'
        response_result = self.grandpy.grandpy_data_of_message('response')
        assert expected_response_result == response_result

        expected_response_result = 'houla, maintenant ma memoire commence a fatiguer !'
        response_result = self.grandpy.grandpy_data_of_message('tired')
        assert expected_response_result == response_result

    def test_grandpy_incorrect_message(self):
        expected_response_result = "Ha, Je ne comprends pas, essaye d'être plus précis ... !"
        response_result = self.grandpy.grandpy_data_of_message('incomprehension')
        assert expected_response_result == response_result

        expected_response_result = "s'il te plait, reformule ta question en étant plus polis ... !"
        response_result = self.grandpy.grandpy_data_of_message('mannerless')
        assert expected_response_result == response_result

        expected_response_result = "Hola, sois plus RESPECTUEUX ENVERS TES AINES 'MON PETIT' ... !"
        response_result = self.grandpy.grandpy_data_of_message('disrespectful')
        assert expected_response_result == response_result

    def test_grandpy_limit_message(self):
        expected_response_result = 'cette impolitesse me FATIGUE ... !'
        response_result = self.grandpy.grandpy_data_of_message('incivility_limit')
        assert expected_response_result == response_result

        expected_response_result = 'cette grossierete me FATIGUE ... !'
        response_result = self.grandpy.grandpy_data_of_message('indecency_limit')
        assert expected_response_result == response_result

        expected_response_result = 'cette incomprehension me FATIGUE ... !'
        response_result = self.grandpy.grandpy_data_of_message('incomprehension_limit')
        assert expected_response_result == response_result

        expected_response_result = 'je suis fatigué reviens me voir demain !'
        response_result = self.grandpy.grandpy_data_of_message('exhausted')
        assert expected_response_result == response_result
