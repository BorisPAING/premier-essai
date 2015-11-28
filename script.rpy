# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

init python:
    import dancingguy as dancingguy

# Déclarez les personnages utilisés dans le jeu.
image bg ville = "bg_ville.png"
image bg burnt = "bg_burnt.png"
image jerome interrogatif_PP = "jerome_interrogatif_PP.png"
image jerome souriant = "jerome_souriant.png"
image jerome pensif = "jerome_pensif.png"
image jerome bagouillant = "jerome_bagouillant.png"
image jerome colerique = "jerome_colerique.png"
image fille avenante = "fille_avenante.png"
image fille hesitante = "fille_hesitante.png"
image fille parlante = "fille_parlante.png"

define j = Character('Jérôme', color="#ffff00")
define f = Character('Truquillela', color="#ff00aa")
    

# Le jeu commence ici
label start:
    play music "YouMakeMeFeel_20151127.mp3"
    scene bg ville
    
    show jerome souriant
    j "Bonjour"
    
    hide jerome
    show fille avenante
    f "Bonjour"
    
    hide fille
    show jerome bagouillant
    j "Euh..."
    
    hide jerome
    show fille hesitante
    "(silence géné)"
    
    show fille avenante
    f "Bonjour ?"
    
label suite :
    hide fille
    show jerome souriant
    j "Ah je suis amoureux !"
    show jerome pensif
    j "Mais comment vais-je faire pour draguer cette déesse ?"
    j "Il faut que je choisisse bien ma phrase d'accroche..."
    show jerome interrogatif_PP
    j "Tu crois que tu pourrais m'aider ?"
    j "Qu'est-ce que je lui dis ?"
    
menu moto:
    "Tu aimerais monter à l'arrière de ma moto ?":
        jump moto
    
    "On se connait non ?":
        jump dejaVu

label dejaVu:
    hide jerome
    show fille parlante
    with dissolve
    f "Euh, peut-être... je me souviens pas."
    
    hide fille
    show jerome souriant
    j "Dans un cours de lindy hop peut-être ?"
    
    hide jerome
    show fille avenante
    f "Ce serait possible dans la mesure où j'en fait"
    
    show fille parlante
    f "Mais tu n'as vraiment pas une tête à faire du lindyhop"
    
    hide fille
    show jerome colerique
    j "Quoi ??? WTF ?!!"
    
    hide jerome
    show fille parlante
    f "Je parie que tu es super mauvais, genre jamais en rythme."
    
    hide fille
    show jerome bagouillant
    j "Tu te trompes et je vais te le prouver !"

python:
    dancingguy.dancingguy()

label laClasse:
    hide jerome
    show fille parlante
    f "Ah oui, je constate que tu as la classe."
    
    show fille parlante
    f "La classe internationale je dirais même."
    
    f "Je te paye un verre ?"
    
    return
    
label moto:
    hide jerome
    show fille parlante
    with dissolve
    f "Wouah ! C'est la phrase d'accroche la plus pourrie que j'ai jamais entendue."

    scene bg burnt
    with dissolve
    show jerome colerique
    "(Jérôme est véxay)"
    
    hide jerome
    show fille hesitante
    f "Non mais te vexe pas, je disais ça pour rigoler, hein !"
    
    hide fille
    show jerome colerique
    j "Ouais, c'est ça ! Si c'est bien ce que je crois, ça me fait pas rire."
    
    hide jerome
    show fille hesitante
    f "Non mais le prends pas comme ça Jérôme, vraiment je t'aime bien en vrai."
    
    scene bg ville
    hide fille
    show jerome souriant
    j "Ah, désolé, j'avais pas compris que c'était ironique."
    
    j "Lol"

    jump byebye

label byebye:
    scene bg ville
    show fille parlante
    
    f "Bon."
    f "Ah, il faut que j'y aille."
    f "Salut, à plus."

    return 
