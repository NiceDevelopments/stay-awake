"""Textes en français (pilote 24.11.2026). Faits uniquement issus de l’appli (voir docstring de build.py).

Recherches (suggestions Google, 24.11.2026) : "alarme toutes les 30 minutes" (+ comment mettre),
"alarme toutes les heures android", "comment rester éveillé" (+ toute une nuit, la nuit au
travail, quand on a sommeil).

Noms de l’appli comme dans app/src/main/res/values-fr : Illimité, Minuteur, Démarrer la session,
Êtes-vous toujours éveillé ?, Terminer la session, Plannings, Fiabilité, Tester l’alarme.
Paramètres (pas « Réglages »), Contrôle manqué, Prêt.
Les captures montrent l’appli en anglais. Vouvoiement, comme la fiche Google Play.
Interdit : la conduite (sauf la phrase des limites, reprise mot pour mot de la fiche Google Play),
promesses de sécurité au travail, « empêche de s’endormir », conseils médicaux.
"""

import re

APP = "Stay Awake"
NOTE_EN = " (capture de l’appli en anglais)"

C = {
    "app_name": APP,
    "lang_name": "Français",
    "og_locale": "fr_FR",
    "ui": {
        "skip": "Aller au contenu",
        "nav": "Navigation principale",
        "guides": "Guides",
        "privacy": "Confidentialité",
        "imprint": "Mentions légales",
        "faq": "Questions fréquentes",
        "toc": "Sur cette page",
        "crumbs": "Fil d’Ariane",
        "updated": "Mis à jour :",
        "with_app": "Avec l’appli",
        "more_guides": "Autres guides",
        "play_cta": "Disponible sur Google Play",
        "play_note": "Gratuit pour Android · sans compte",
        "moreapps": "Autres applis de Nice Developments",
        "footer_tag": "L’alarme qui vous demande si vous êtes toujours éveillé. Pour Android.",
        "trademark": "Google Play et Android sont des marques de Google LLC.",
    },

    "home": {
        "title": "Stay Awake : l’alarme qui vous demande si vous êtes toujours éveillé",
        "desc": "Un réveil sonne une fois, vous l’éteignez et vous vous rendormez. Stay Awake demande encore et encore si vous êtes éveillé – et sonne jusqu’à votre réponse.",
        "kicker": "Pour tous ceux qui doivent rester éveillés",
        "h1": "Un réveil sonne une fois. Stay Awake continue de demander.",
        "lead": "Vous connaissez ça : le réveil sonne, vous l’éteignez – et cinq minutes plus tard vous dormez de nouveau. Stay Awake ne s’arrête pas après une sonnerie. Toutes les 30 minutes, ou à l’intervalle de votre choix, il demande : **Êtes-vous toujours éveillé ?** Secouez le téléphone ou touchez Oui, et le tour suivant commence. Pas de réponse ? Il vibre après 10 secondes, et après 20 une alarme sonne – jusqu’à ce que vous répondiez.",
        "who": "Travail de nuit · astreintes · nuits de révision · attente pendant la nuit",
        "why_h2": "Pourquoi un simple réveil ne suffit pas",
        "why_lead": "Un réveil est fait pour vous réveiller une fois. Rester éveillé, c’est tenir heure après heure – et le plus dur, c’est le moment où personne ne vérifie si vous êtes encore là.",
        "why": [["Un simple réveil", ["Sonne une fois – à l’heure fixée à l’avance.", "Vous l’éteignez à moitié endormi, et plus rien ne suit.", "Ne demande jamais si vous êtes toujours éveillé."]], ["Stay Awake", ["Demande encore et encore, toute la nuit – à l’intervalle de votre choix, d’une minute à douze heures.", "Demande d’abord en silence. Il ne vibre, puis ne sonne, que si vous ne répondez pas.", "L’alarme sonne jusqu’à votre réponse. Puis le tour suivant commence."]]],
        "hero_shot": "en-session.webp",
        "shots": {
            "en-session.webp": "Session en cours : un anneau ambre autour du compte à rebours 29:50, en dessous « avant le prochain contrôle », « Illimité », « Intervalle : 30 minutes · Toucher ou secouer », le bouton « Je suis éveillé » et « Terminer la session ».",
            "en-home.webp": "Écran d’accueil : Illimité ou Minuteur, un sélecteur rond sur 30 minutes et le bouton Démarrer la session" + NOTE_EN + ".",
            "en-check.webp": "Le contrôle : « Êtes-vous toujours éveillé ? », en dessous « ou secouez le téléphone », une fine ligne de progression et un grand bouton Oui, puis Terminer la session" + NOTE_EN + ".",
            "en-alarm.webp": "Après 20 secondes sans réponse : le même contrôle, maintenant avec la mention « Contrôle manqué » et une ligne rouge ; l’alarme sonne" + NOTE_EN + ".",
            "en-schedules.webp": "Plannings : de 22 h à 6 h, du lundi au vendredi, toutes les 30 minutes, activé" + NOTE_EN + ".",
            "en-reliability.webp": "Vérification de fiabilité : « Prêt » avec neuf points verts, des notifications à la batterie" + NOTE_EN + ".",
            "en-timer.webp": "Mode Minuteur : pendant 2:00 h, contrôle toutes les 30 minutes" + NOTE_EN + ".",
            "en-settings.webp": "Paramètres : toucher Oui fonctionne toujours ; en plus, secouer le téléphone, le retourner ou un bouton de volume" + NOTE_EN + ".",
        },
        "steps_h2": "Ce qui se passe quand un contrôle arrive",
        "steps_lead": "D’abord en douceur, fort seulement si nécessaire. Chaque étape s’arrête dès que vous répondez.",
        "steps": [
            ["0 s", "La question", "L’écran s’allume – aussi par-dessus l’écran de verrouillage – et demande : Êtes-vous toujours éveillé ?"],
            ["10 s", "Vibration", "Toujours pas de réponse ? Le téléphone se met à vibrer."],
            ["20 s", "Alarme", "Toujours rien : une vraie alarme avec le son d’alarme de votre téléphone."],
            ["Oui", "Tour suivant", "Un appui ou une secousse : tout s’arrête et l’intervalle complet recommence."],
        ],
        "features_h2": "Démarrer, confirmer, planifier, vérifier",
        "features": [
            {"kicker": "Démarrer", "h2": "Deux choix, un bouton",
             "body": ["**Illimité** ou **Minuteur**, et à quelle fréquence vous voulez être interrogé. Tournez le sélecteur – d’une minute à douze heures, 30 minutes pour commencer. L’appli retient votre dernier choix.",
                      "Le minuteur dure un temps fixe (« pendant 2 heures ») ou jusqu’à une heure donnée (« jusqu’à 5 h 30 »)."],
             "shot": "en-home.webp"},
            {"kicker": "Confirmer", "h2": "Toucher, secouer, retourner – à vous de choisir",
             "body": ["Le grand bouton **Oui** fonctionne toujours. Dans les paramètres, vous pouvez ajouter secouer le téléphone, le retourner ou un bouton de volume, dans n’importe quelle combinaison. Secouer et retourner fonctionnent aussi écran éteint.",
                      "Inutile d’attendre la question : confirmez quand vous voulez, et l’intervalle recommence à partir de ce moment."],
             "shot": "en-check.webp"},
            {"kicker": "Horaires", "h2": "Des plannings qui démarrent seuls",
             "body": ["Pour les nuits qui se répètent : heure de début et de fin, jours de la semaine facultatifs, intervalle. La session démarre seule à l’heure prévue et se termine à l’heure de fin.",
                      "Sans jour sélectionné, le planning ne s’exécute qu’une fois, au prochain début."],
             "shot": "en-schedules.webp"},
            {"kicker": "Fiabilité", "h2": "Sait ce que votre téléphone autorise",
             "body": ["Les téléphones Android peuvent retarder ou bloquer des alarmes – économie de batterie, Ne pas déranger, autorisations manquantes. La vérification de **Fiabilité** passe chaque point en revue en langage clair et montre comment corriger ce qui ne va pas.",
                      "Avec **Tester l’alarme**, vous entendez et sentez l’alarme pendant cinq secondes, avant la première vraie nuit."],
             "shot": "en-reliability.webp"},
        ],
        "limits_h2": "Limites honnêtes",
        "limits": "Stay Awake vous aide à rester éveillé. L'appli ne remplace ni le sommeil ni les pauses, et ce n'est pas un système de sécurité pour le travail ou la conduite. Qu’un contrôle arrive à l’heure dépend aussi du téléphone – la vérification de fiabilité montre ce que le vôtre autorise.",
        "nots_h2": "Aucune inscription",
        "nots": [
            "**Ni compte ni connexion.** Sessions, plannings et paramètres restent sur votre téléphone.",
            "**Fonctionne hors ligne.** Les contrôles et l’alarme n’ont pas besoin d’internet.",
            "**Les sessions survivent à un redémarrage** du téléphone.",
            "**Gratuit avec une petite bannière.** Pas de publicité sur le contrôle ni sur l’alarme. Stay Awake Pro supprime la bannière – par abonnement mensuel ou achat unique.",
            "**20 langues**, de l’arabe au vietnamien.",
        ],
        "privacy_link": "Lire la politique de confidentialité (en anglais)",
        "guides_h2": "Guides pour les longues nuits",
        "guides_lead": "Utiles même sans l’appli : une alarme toutes les 30 minutes, le travail de nuit et une nuit entière sans dormir.",
        "faq": [
            ["Quelle différence avec un réveil normal ?",
             ["Un réveil sonne à une heure, que vous soyez éveillé ou non. Stay Awake demande d’abord et ne sonne fort que si vous ne répondez pas. Il est fait pour rester éveillé, pas pour se réveiller le matin."]],
            ["Dois-je laisser l’écran allumé ?",
             ["Non. Posez le téléphone, verrouillez-le, laissez l’écran s’éteindre. Le contrôle apparaît par-dessus l’écran de verrouillage. Si vous avez choisi de secouer, une secousse suffit pour confirmer, même écran éteint."]],
            ["Quel son d’alarme utilise-t-il ?",
             ["Par défaut, le son d’alarme de votre propre téléphone. Dans les paramètres, vous pouvez passer à la mélodie Stay Awake ou choisir un autre son."]],
            ["Fonctionne-t-il sans internet ?",
             ["Oui. Les contrôles, la vibration et l’alarme fonctionnent entièrement sur le téléphone."]],
            ["Combien ça coûte ?",
             ["Tout ce qui vous garde éveillé est gratuit. La version gratuite affiche une petite bannière sur les écrans normaux, jamais sur le contrôle ni sur l’alarme. Stay Awake Pro la supprime, par abonnement mensuel ou achat unique ; le prix est indiqué sur Google Play."]],
            ["Existe-t-il une version iPhone ?",
             ["Non, Stay Awake n’est disponible que pour Android."]],
        ],
        "final_h2": "Si vous devez rester éveillé, c’est votre appli.",
        "final_body": "Démarrez une session et posez le téléphone. Stay Awake continue de demander jusqu’à ce que vous terminiez la session.",
    },

    "guides_index": {
        "title": "Guides : alarme toutes les 30 minutes, travail de nuit, nuit blanche",
        "desc": "Guides pratiques pour les longues nuits : mettre une alarme toutes les 30 minutes sur Android, rester éveillé la nuit au travail et tenir toute une nuit.",
        "h1": "Guides pour les longues nuits",
        "lead": "Des réponses courtes et pratiques, utiles avec ou sans appli.",
        "app": "**Stay Awake** vous demande, à l’intervalle de votre choix, si vous êtes toujours éveillé et fait sonner une alarme si aucune réponse ne vient.",
    },

    "guides": [
        {
            "id": "every30",
            "slug": "alarme-toutes-les-30-minutes-android",
            "title": "Comment mettre une alarme toutes les 30 minutes sur Android",
            "desc": "L’horloge d’Android n’a pas d’option « toutes les 30 minutes ». Trois méthodes : plusieurs alarmes, un minuteur relancé ou une appli à intervalle.",
            "h1": "Comment mettre une alarme toutes les 30 minutes sur Android",
            "teaser": "Plusieurs alarmes, un minuteur relancé ou une appli à intervalle – trois méthodes.",
            "answer": "Les applis Horloge de la plupart des téléphones Android ne répètent une alarme que **par jour de la semaine**, pas toutes les X minutes. Vous avez trois possibilités : **créer plusieurs alarmes**, **relancer un minuteur** à chaque fois ou utiliser une **appli d’alarme à intervalle**.",
            "updated": "2026-11-24",
            "updated_label": "24 novembre 2026",
            "sections": [
                ["several", "Méthode 1 : plusieurs alarmes", [
                    "Créez dans l’appli Horloge une alarme pour chaque demi-heure. Pour une soirée, ça va ; pour une nuit entière, ça devient long :",
                    {"table": [
                        ["Durée", "Intervalle", "Alarmes nécessaires"],
                        ["2 heures", "30 min", "4"],
                        ["8 heures (22 h–6 h)", "30 min", "16"],
                        ["8 heures", "15 min", "32"],
                    ]},
                    "Inconvénients : beaucoup de manipulations, et les alarmes continuent de sonner à heures fixes même si vous êtes bien réveillé. Ensuite, il faut toutes les désactiver.",
                ]],
                ["timer", "Méthode 2 : relancer un minuteur", [
                    {"steps": [
                        "Ouvrez l’appli Horloge et allez dans **Minuteur**.",
                        "Réglez **30:00** et lancez-le.",
                        "Quand il sonne, arrêtez-le et relancez-le.",
                    ]},
                    "Simple, mais il faut le relancer à chaque fois. Si vous oubliez une seule fois, il ne se passe plus rien pour le reste de la nuit.",
                ]],
                ["app", "Méthode 3 : une appli d’alarme à intervalle", [
                    "Les applis d’alarme à intervalle se répètent toutes seules. Avant d’en choisir une, vérifiez trois choses :",
                    {"list": [
                        "**Sonne-t-elle écran éteint et téléphone verrouillé ?** Beaucoup d’applis ne fonctionnent qu’au premier plan.",
                        "**Utilise-t-elle des alarmes exactes ?** Sinon, Android peut la retarder en mode économie d’énergie.",
                        "**Que se passe-t-il si vous ne réagissez pas ?** Une simple alarme répétée sonne un moment, puis s’arrête.",
                    ]},
                ]],
            ],
            "app": {
                "h2": "Une alarme à intervalle qui demande d’abord",
                "body": [
                    "Stay Awake se répète à l’intervalle de votre choix – n’importe quelle valeur d’une minute à douze heures – et utilise des alarmes exactes. Il ne sonne pas d’emblée : il demande d’abord en silence si vous êtes toujours éveillé. Répondez, et l’intervalle recommence à partir de ce moment. Sans réponse : vibration après 10 secondes, alarme après 20.",
                    "Ainsi, il ne vous fait pas sursauter quand vous êtes éveillé – et ne vous laisse pas seul quand vous ne l’êtes plus.",
                ],
                "shot": "en-home.webp",
                "alt": "Sélecteur sur 30 minutes, Illimité ou Minuteur, Démarrer la session" + NOTE_EN + ".",
            },
            "faq": [
                ["L’horloge d’Android peut-elle répéter une alarme toutes les 30 minutes ?",
                 ["Les applis Horloge de la plupart des téléphones Android ne répètent que par jour de la semaine. Pour toutes les 30 minutes, il faut plusieurs alarmes, un minuteur ou une appli à part."]],
                ["Pourquoi mon alarme à intervalle ne sonne-t-elle pas écran éteint ?",
                 ["Souvent, l’optimisation de la batterie ou l’autorisation manquante pour les alarmes exactes en est la cause. Vérifiez dans les paramètres Android que l’utilisation de la batterie par l’appli n’est pas restreinte."]],
                ["Peut-on régler un intervalle de 15 ou 45 minutes ?",
                 ["Dans Stay Awake, oui : le sélecteur va d’une minute à douze heures. Sans appli, une alarme toutes les 15 minutes en demanderait 32 pour une nuit de 8 heures."]],
            ],
        },
        {
            "id": "nightshift",
            "slug": "rester-eveille-la-nuit-au-travail",
            "title": "Comment rester éveillé la nuit au travail : 9 conseils pratiques",
            "desc": "Rester alerte pendant un poste de nuit : lumière, mouvement, petites tâches pour les heures creuses vers 3 h du matin, repas et un rythme de contrôles.",
            "h1": "Comment rester éveillé la nuit au travail",
            "teaser": "Lumière, mouvement et un plan pour les heures creuses de la nuit.",
            "answer": "Le plus dur d’un poste de nuit est rarement le début – c’est le creux de la nuit, quand il ne se passe rien. Ce qui aide le plus : **la lumière, le mouvement et un rythme**. Découpez la nuit en blocs courts, donnez à chaque bloc quelque chose à faire, et ne restez pas longtemps immobile dans la pénombre.",
            "updated": "2026-11-24",
            "updated_label": "24 novembre 2026",
            "sections": [
                ["dead-hours", "Un plan pour les heures creuses", [
                    "Ceux qui travaillent de nuit connaissent ce moment : quelque part entre 2 h et 5 h, tout devient calme, le café ne fait plus effet et les paupières s’alourdissent. Ne laissez pas ce passage au hasard.",
                    {"list": [
                        "**Gardez les tâches actives pour ce moment.** Réapprovisionner, classer, faire des rondes, vérifier le matériel – tout ce qui vous fait vous lever et marcher.",
                        "**Découpez la nuit en blocs** de 30 à 60 minutes. Chaque bloc se termine par une petite action : se lever, boire de l’eau, écrire une ligne dans le registre.",
                        "**Évitez les longs moments passifs**, comme lire ou regarder un écran enfoncé dans un fauteuil.",
                    ]},
                ]],
                ["tips", "9 conseils qui marchent pour beaucoup de gens", [
                    {"steps": [
                        "**Gardez la pièce bien éclairée.** La pénombre endort. Allumez l’éclairage principal plutôt qu’une seule lampe, si votre poste le permet.",
                        "**Bougez toutes les demi-heures.** Un tour dans le couloir, quelques marches, des étirements – quelques minutes suffisent.",
                        "**Faites le travail de routine debout.** Assis, on s’assoupit facilement.",
                        "**Buvez de l’eau régulièrement.** Cela donne aussi une raison de se lever.",
                        "**Mangez par petites portions.** Beaucoup de gens se sentent lourds après un gros repas en pleine nuit ; quelques petites collations passent mieux.",
                        "**Utilisez l’eau froide.** Sur le visage ou les mains quand le coup de barre arrive.",
                        "**Parlez à quelqu’un.** Une courte conversation avec un collègue casse le moment calme – pour vous deux.",
                        "**De l’air frais.** Quelques minutes à une fenêtre ouverte ou dehors.",
                        "**Faites des contrôles à heures fixes.** Un rappel régulier – toutes les 20 ou 30 minutes – qui demande une réponse consciente vous aide à remarquer quand les minutes commencent à devenir une heure sans que vous vous en rendiez compte.",
                    ]},
                ]],
                ["before", "Avant et après le poste", [
                    "Un poste de nuit commence plus tôt que ne l’indique l’horloge : si vous arrivez déjà fatigué, aucun conseil ne vous fera tenir. Planifiez votre sommeil avant la première nuit et protégez-le après le poste – chambre sombre, téléphone en silencieux, entourage prévenu.",
                    {"note": "Si vous remarquez que vous piquez du nez à répétition, c’est un signal à prendre au sérieux. Parlez-en à votre équipe ou à votre employeur – aucune appli et aucun conseil ne remplacent le sommeil."},
                ]],
            ],
            "app": {
                "h2": "Un contrôle toutes les 30 minutes",
                "body": [
                    "Stay Awake transforme le conseil 9 en routine : il vous demande, à l’intervalle de votre choix, si vous êtes toujours éveillé. Secouez le téléphone ou touchez Oui, et le tour suivant commence. Si vous ne répondez pas, il vibre après 10 secondes et fait sonner une alarme après 20.",
                    "Pour des postes qui se répètent, créez un **planning** – par exemple de 22 h à 6 h, du lundi au vendredi. La session démarre et s’arrête toute seule.",
                ],
                "shot": "en-schedules.webp",
                "alt": "Planning de 22 h à 6 h, du lundi au vendredi, toutes les 30 minutes" + NOTE_EN + ".",
            },
            "faq": [
                ["Quand est-il le plus difficile de rester éveillé la nuit au travail ?",
                 ["Pour beaucoup de gens, au creux de la nuit, à peu près entre 2 h et 5 h. Prévoyez des tâches actives pour ce moment."]],
                ["Le café aide-t-il pendant un poste de nuit ?",
                 ["Beaucoup de gens boivent un café en début de poste. Il ne remplace pas la lumière, le mouvement et un rythme – et la quantité qui vous convient, un site web ne peut pas vous la dire."]],
                ["Comment rester éveillé une nuit calme où il n’y a rien à faire ?",
                 ["Fixez-vous de petites tâches toutes les 30 à 60 minutes, levez-vous régulièrement et gardez la pièce éclairée. Un rappel de contrôle régulier vous aide à remarquer quand vous commencez à décrocher."]],
            ],
        },
        {
            "id": "allnight",
            "slug": "rester-eveille-toute-une-nuit",
            "title": "Comment rester éveillé toute une nuit : un plan heure par heure",
            "desc": "Quand vous devez passer une nuit blanche : un plan pour la soirée, minuit, les heures creuses et le matin – et comment remarquer si vous vous assoupissez.",
            "h1": "Comment rester éveillé toute une nuit",
            "teaser": "Un plan pour la soirée, minuit, les heures creuses et le matin.",
            "answer": "Une nuit entière se passe mieux avec un plan qu’avec de la volonté. Commencez la nuit reposé, gardez **la lumière allumée et le corps actif**, réservez les tâches les plus actives pour après 2 h – et prévoyez quelque chose qui **vérifie régulièrement** que vous êtes toujours éveillé et sonne fort si la réponse ne vient pas.",
            "updated": "2026-11-24",
            "updated_label": "24 novembre 2026",
            "sections": [
                ["plan", "Un plan pour la nuit", [
                    {"table": [
                        ["Quand", "Ce qui aide"],
                        ["Soirée", "Commencez reposé si possible. Mangez normalement, pas un repas lourd tard le soir."],
                        ["Jusqu’à minuit", "Faites maintenant le travail qui demande d’avoir les idées claires."],
                        ["De minuit à 2 h", "Travaillez par blocs ; levez-vous et bougez entre deux."],
                        ["De 2 h à 5 h", "Le passage le plus dur pour beaucoup : tâches actives, lumière vive, air frais."],
                        ["Matin", "La lumière du jour aide beaucoup de gens pour la dernière ligne droite. Ne faites rien qui exige une pleine concentration."],
                    ]},
                ]],
                ["tricks", "Ce qui vous fait tenir", [
                    {"list": [
                        "**La lumière :** éclairage principal allumé, écran assez lumineux.",
                        "**Le mouvement :** quelques minutes toutes les demi-heures.",
                        "**L’eau froide** sur le visage et les mains.",
                        "**Quelque chose à faire avec les mains** plutôt que de regarder passivement.",
                        "**De la compagnie :** un appel ou une discussion avec quelqu’un qui est aussi debout.",
                    ]},
                ]],
                ["notice", "Remarquer quand vous vous assoupissez", [
                    "Le danger d’une longue nuit n’est pas de s’écrouler d’un coup, mais les petits moments : vous fermez les yeux « juste une minute », et soudain une heure a passé. Vous ne vous en rendez compte que si quelque chose vous interroge de l’extérieur.",
                    "Sans appli : un minuteur que vous relancez à chaque sonnerie, ou un ami qui prend de vos nouvelles par message. Avec une appli : voir plus bas.",
                ]],
                ["after", "Le lendemain", [
                    "Une nuit sans sommeil se paie. Prévoyez une journée légère le lendemain et rattrapez le sommeil dès que possible.",
                    {"note": "Savoir si passer une nuit blanche est une bonne idée pour vous, seul vous – ou un médecin – pouvez en juger. Ce guide parle de tenir une nuit que vous avez déjà décidé de passer éveillé."},
                ]],
            ],
            "app": {
                "h2": "Quelqu’un qui demande toutes les 30 minutes",
                "body": [
                    "Stay Awake vous demande, à l’intervalle de votre choix, si vous êtes toujours éveillé. Secouez le téléphone ou touchez Oui, et le tour suivant commence. Si la réponse ne vient pas, le téléphone vibre après 10 secondes et une alarme sonne après 20 – avec la sonnerie d’alarme de votre propre téléphone.",
                    "Démarrez une session en mode **Illimité** pour une nuit sans fin prévue, ou un **Minuteur** « jusqu’à 6 h ».",
                ],
                "shot": "en-alarm.webp",
                "alt": "Contrôle après 20 secondes : Contrôle manqué, Êtes-vous toujours éveillé ?, un grand bouton Oui" + NOTE_EN + ".",
            },
            "faq": [
                ["À quelle heure est-il le plus difficile de rester éveillé ?",
                 ["Beaucoup de gens trouvent le passage entre 2 h et 5 h du matin environ le plus difficile. Gardez les tâches les plus actives pour ce moment."]],
                ["Une courte sieste aide-t-elle ?",
                 ["Certaines personnes prévoient une courte sieste. Le risque est de dormir bien plus longtemps que prévu – si vous le faites, réglez une alarme impossible à ignorer."]],
                ["Comment être sûr de me réveiller si je m’assoupis ?",
                 ["Utilisez quelque chose qui prend régulièrement de vos nouvelles et sonne fort si vous ne répondez pas – un ami, un minuteur répété ou une appli qui vous demande si vous êtes toujours éveillé."]],
            ],
        },
    ],
}


# Typographie française : espace insécable avant ? ! : ; » et après « – sinon le signe peut se
# retrouver seul en début de ligne. Les textes ci-dessus s’écrivent avec des espaces normales.
def _insecables(x):
    if isinstance(x, str):
        return re.sub(r" (?=[?!:;»])", "\u00a0", x).replace("« ", "«\u00a0")
    if isinstance(x, list):
        return [_insecables(y) for y in x]
    if isinstance(x, dict):
        return {k: v if k in ("id", "slug", "shot", "hero_shot", "updated") else _insecables(v)
                for k, v in x.items()}
    return x


C = _insecables(C)
