
#----------------------------------------------------------------------------------------------------------------------#
                                                   README
#----------------------------------------------------------------------------------------------------------------------#


1. Présentation de l'éxistant
    Pour consulter les paramètres du ROBO-PONG l'entraineur doit se déplacer jusqu'au pupitre de commande placé sur
    la table de ping-pong.

2. Améliorations souhaitées
    Pour être en mesure e consulter à distance via un LAN, les différents paramètres du robot.
    Vous devez crée une page WEB pour permettre la visualisation des différents paramètres du robot.
    Pour cela, vous devrez présenter :

    - Un bilan des signaux (sur la carte évolutive) qui codent ces différentes informations utiles pour cette évolution.
    - Localiser sur la carte évolutive les connexions possibles pour les différents signaux.
    - Faire les mesures nécesaires afin de caractériser les différents signaux.
    - Caractériser les différents signaux.
    - Choisir une carte d'extension afin que le serveur WEB soit directement connecté à la carte évolutive.
    - Coder la page WEB et la tester.
    - Mettre la page WEB sur le serveur et tester l'accés à la page WEB via le LAN.

3. Cahier des charges

    [Carte évolutive]->Signaux éléctriques->[Serveur avec WEB]->Informations visuelles.

    Entrées:
        Signaux éléctriques: Signaux générés par la carte évolutive ROBO-PONG :
                - Vitesse
                - Cadence
                - Etc ...

    Sortie:
        Informations visuelles: Page WEB avec les différentes informations du ROBO-PONG :
                - Vitesse
                - Cadence
                - Etc ...