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
    # Data for parser (deleted for research)
    UNNECESSARY_SET_DATA = set(
        [
        'a','abord','absolument','afin','ah','ai','aie','ailleurs','ainsi','ait',
        'allaient','allo','allons','allô','alors','ancetre','ancetre demode',
        'anterieur','anterieure','anterieures','antiquite','apres','après',
        'arriere rococo','as','assez','attendu','au','aucun','aucune','aujourd',
        "aujourd'hui",'aupres','auquel','aura','auraient','aurait','auront','aussi',
        'autre','autrefois','autrement','autres','autrui','aux','auxquelles',
        'auxquels','avaient','avais','avait','avant','avec','avoir','avons','ayant',
        'b','bah','bas','basee','bat','beau','beaucoup','bien','bigre','bonjour',
        'bonjour grandpy','comment vas tu','bonsoir grandpy','boum', 'bravo','brrr',
        'c','car','ce','ceci','cela','celle','celle-ci','celle-là', 'celles',
        'celles-ci','celles-là','celui','celui-ci','celui-là','cent',
        'centenaire senille','cependant','certain','certaine','certaines','certains',
        'certes','ces','cet','cette','ceux','ceux-ci','ceux-là','chacun','chacune',
        'chaque','cher','chers','chez','chiche','chut','chère','chères','ci','cinq',
        'cinquantaine','cinquante','cinquantième','cinquième','clac','clic','combien',
        'comme','comment','comment allez vous, grandpy','comparable','comparables',
        'compris','concernant','contre','couic','crac','d','da','dans','de','debout',
        'dedans','dehors','deja','delà','depuis','dernier','derniere','derriere',
        'derrière','des','desormais','desquelles','desquels','dessous','dessus','deux',
        'deuxième','deuxièmement','devant','devers','devra','different','differentes',
        'differents','différent','différente','différentes','différents',
        'dinosaure decrepit','dire','directe','directement','dit','dite','dits',
        'divers','diverse','diverses','dix','e','effet','egale','egalement','egales',
        'eh','elle','elle-même','elles','elles-mêmes','en','encore','enfin','entre',
        'envers','environ','es','est','et','etant','etc','etre','eu','euh','eux',
        'eux-mêmes','exactement','excepté','extenso','exterieur','f','fais',
        'faisaient','faisant','fait','façon','feront','fi','flac','floc','font','g',
        'gens','grandpy','h','ha','hello grandpy','hein','hem','hep','hey','hi','ho',
        'holà','hop','hormis','hors','hou','houp','hue','hui','huit','huitième','hum',
        'hurrah','hé','hélas','i','il','ils','importe','j','je','jusqu','jusque',
        'juste','k','l','la','laisser','laquelle','las','le','lequel','les',
        'lesquelles','lesquels','leur','leurs','longtemps','lors','lorsque','lui',
        'lui-meme','lui-même','là','lès','m','ma','maint','maintenant','mais','malgre',
        'malgré','maximale','me','meme','memes','merci','mes','mien',"m'indiquer",
        "m'orienter",'mienne','miennes','miens','mille','mince','minimale','moi',
        'moi-meme','moi-même','moindres','moins','mon','moyennant','multiple',
        'multiples','même','mêmes','n','na','naturel','naturelle','naturelles','ne',
        'neanmoins','necessaire','necessairement','neuf','neuvième','ni','nombreuses',
        'nombreux','non','nos','notamment','notre','nous','nous-mêmes','nouveau','nul',
        'néanmoins','nôtre','nôtres','o','oh','ohé','ollé','olé','on','ont','onze',
        'onzième','ore','ou','ouf','ouias','oust','ouste','outre','ouvert','ouverte',
        'ouverts','o|','où','p','paf','pan','papi','papy','par','parce','parfois',
        'parle','parlent','parler','parmi', 'parseme','partant','particulier',
        'particulière','particulièrement','pas','passé','pendant','pense','permet',
        'personne','peu','peut','peuvent','peux','pff','pfft','pfut','pif','pire',
        'plein','plouf','plus','plusieurs','plutôt','possessif','possessifs',
        'possible','possibles','pouah','pour','pourquoi','pourrais','pourrait',
        'pouvait','prealable','precisement','premier','première','premièrement','pres',
        'probable','probante','procedant','proche','près','psitt','pu','puis',
        'puisque','pur','pure','q','qu','quand','quant','quant-à-soi','quanta',
        'quarante','quatorze','quatre','quatre-vingt','quatrième','quatrièmement',
        'que','quel','quelconque','quelle','quelles',"quelqu'un",'quelque','quelques',
        'quels','qui','quiconque','quinze','quoi','quoique','r','rare','rarement',
        'rares','relative','relativement','remarquable','rend','rendre','restant',
        'reste','restent','restrictif','retour','revoici','revoilà','rien','s','sa',
        'sacrebleu','sait','salut','salut grandpy, comment ca va','sans','sapristi',
        'sauf','se','sein','seize','selon','semblable','semblaient','semble',
        'semblent','sent','sept','septième','sera','seraient','serait','seront','ses',
        'seul','seule','seulement','si','sien','sienne','siennes','siens','sinon',
        'situe','situé','six','sixième','soi','soi-même','soit','soixante','son',
        'sont','sous','souvent','specifique','specifiques','speculatif','stop',
        'strictement','subtiles','suffisant','suffisante','suffit','suis','suit',
        'suivant','suivante','suivantes','suivants','suivre','superpose','sur',
        'surtout','t','ta','tac','tant','tardive','te','tel','telle','tellement',
        'telles','tels','tenant','tend','tenir','tente','tes','tic','tien','tienne',
        'tiennes','tiens','toc','toi','toi-même','ton','touchant','toujours','tous',
        'tout','toute','toutefois','toutes','treize','trente','tres','trois',
        'troisième','troisièmement','trop','trouve','très','tsoin','tsouin','tu','té',
        'u','un','une','unes','uniformement','unique','uniques','uns','v','va','vais',
        'vas','vers','via','vieillard senille','vieille baderne','vieillot archaique',
        'vieux','vieux croulant','vieux fossile','vieux gateux','vieux poussierieux',
        'vif','vifs','vingt','vivat','vive','vives','vlan','voici','voilà','vont',
        'vos','votre','vous','vous-mêmes','vu','vé','vôtre','vôtres','w','x','y','z',
        'zut','à','â','ça','ès','étaient','étais','était','étant','été','être','ô',',',
        ';','.','?','!','donner',"l'adresse",'du','connais','donnez','connaissez'
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

    def establishing_user_incomprehension_data(self):
        """creation of attributes comprehension"""
        # search comprehension
        if self.CIVILITY_SET_DATA.isdisjoint(self.user_answer) and\
            self.INDECENCY_SET_DATA.isdisjoint(self.user_answer) and\
            self.UNNECESSARY_SET_DATA.isdisjoint(self.user_answer):
            return True
        else:
            return False
