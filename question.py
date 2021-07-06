#coding:utf-8
#!/usr/bin/env python
"""user question management module"""

class Question:
    """organization of the user's question"""
    # Data for check civility
    CIVILITY_SET_DATA = set(
        [
        'bonjour', 'bonsoir','salut','hello','hi'
        ]
    )
    # Data for check decency
    INDECENCY_SET_DATA = set(
        [
        'vieux','con','ancetre', 'poussierieux','vieillard', 'demoder',
        'dinosaure', 'senille','arrierer', 'decrepit','centenaire', 'rococo',
        'antiquite', 'senille', 'gateux', 'archaique', 'croulant',
        'vieille', 'baderne', 'fossile', 'foutu', 'bjr', 'bsr', 'slt'
        ]
    )

    def __init__(self, question_asked_by_user):
        """constructor for organization of the user's question"""
        self.question_asked_by_user = question_asked_by_user.lower()
        self.user_answer = self.question_asked_by_user.split()
    
    def establishing_user_incivility_data(self):
        """creation of attributes civility"""
        return self.CIVILITY_SET_DATA.isdisjoint(self.user_answer)

    def establishing_user_indecency_data(self):
        """creation of attributes decency"""
        return not self.INDECENCY_SET_DATA.isdisjoint(self.user_answer)
