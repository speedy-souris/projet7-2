#coding:utf-8
#!/usr/bin/env python
"""grandpyRobot management module"""

from frozendict import frozendict

class GrandpyRobot:
    """class for the organization of grandpyRobot according to user behavior"""

    @staticmethod
    def grandpy_data_of_message(key_data):
        """management of all responses from grandpy"""
        grandpy_message = frozendict({
            'home': "Bonjour Mon petit, en quoi puis-je t'aider ?",
            'user_question': 'As tu une nouvelle question a me demander ?',
            'response': 'Voici Ta Réponse à la question !',
            'tired': 'houla, maintenant ma memoire commence a fatiguer !',
            'incomprehension':\
                "Ha, Je ne comprends pas, essaye d'être plus précis ... !",
            'mannerless':\
                "s'il te plait, reformule ta question en étant plus polis ... !",
            'disrespectful':\
                "Hola, sois plus RESPECTUEUX ENVERS TES AINES 'MON PETIT' ... !",
            'incivility_limit': 'cette impolitesse me FATIGUE ... !',
            'indecency_limit': 'cette grossierete me FATIGUE ... !',
            'incomprehension_limit': 'cette incomprehension me FATIGUE ... !',
            'exhausted': 'je suis fatigué reviens me voir demain !'
        })
        return grandpy_message[key_data]
