# -* -coding:Utf-8 -*

import os, sys, renpygame
import renpygame as pygame
from renpygame.locals import *
from jeu import *

def dancingguy () :
	# On définit la durée de la présentation
	# Le jeu commence à 32 secondes et 440 milisecondes
	# debutJeu = 32440
	debutJeu = 500 # valeur de test
	
	# On initialise la SDL
	pygame.init()

	# On initialise SDL_mixer
	# - frequency
	# - size : nb de bits par échantillon
	# - channels : 1 pour mono, 2 pour stereo, 
	# - buffer : nombre de samples dans le mixer : 
	#            diminuer ce nombre réduit la latence (mais des arrêts de son peuvent se produire)
	#            l'augmenter empêche l'arrêt, mais augmente la latence
	pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=128)
	
	# On initialise SDL_ttf
	# pygame.font.init()

	# On charge la musique en mémoire
	# pygame.mixer.music.load("nico-20150823.mp3")


	# On créé les objets pour le texte
	# maFont = pygame.font.Font("FRGROT.TTF", 16)
	# maFont2 = pygame.font.Font("FRGROT.TTF", 14)
	# couleur = 255, 0, 0
	# texte = maFont.render("Bienvenue dans le jeu \"Dancing Guy\"", True, (255,0,0))
	# texte2 = maFont.render("Bienvenue dans le jeu \"Dancing Guy\"", True, (0,0,0))

	# On créé une liste pour enregistrer la position du texte
	positionTexte = 0, 0
	positionTexte2 = 1, 1

	# On créé une horloge
	horloge = pygame.time.Clock()

	# On créé un entier pour retenir la durée (en miliseconde) écoulée depuis le début du jeu
	duree = 0

	# On joue la musique
	pygame.mixer.music.play()

	# On créé une variable booléenne 
	# pour enregistrer le statut de la musique (en pause ou pas)
	musiqueEnPause = False

	# On définit la taille de notre fenêtre
	tailleFenetre = 800, 600

	# On créé la fenêtre :
	# charger les images après cette ligne
	# initialiser le mixer avant cette ligne
	fenetre = pygame.display.set_mode(tailleFenetre)
	
	# Avec convert() on charge en mémoire l'image du fond
	fond = pygame.image.load("dancefloor.jpg").convert()
	
	# On définit les coordonnées (x, y)) de la position où sera collé le fond
	positionFond = 0, 0
	
	# On définit une variable mode
	mode = 0
	
	# Une boucle infinie pour l'affichage
	while mode == 0:
		# Une boucle pour la gestion des évènements
		for event in pygame.event.get():
			# Si le joueur clique sur la croix, on ferme la fenêtre
			if event.type == pygame.QUIT: 
				sys.exit()
			# L'utilisateur presse une touche du clavier
			elif event.type == pygame.KEYDOWN:
				# Si l'utilisateur appuie sur Echap
				if event.key == K_ESCAPE:
					# on ferme la fenêtre
					sys.exit()
				# Si l'utilisateur appuie sur la touche "espace"
				elif event.key == K_SPACE:
					# Si la musique joue
					if not musiqueEnPause :
						# on arrête la musique
						pygame.mixer.music.pause()
					# Si elle ne joue pas
					else:
						# on la relance depuis le début
						pygame.mixer.music.unpause()
					# on inverse la valeur du booléen
					musiqueEnPause = not musiqueEnPause
		
		# On colle le fond sur la fenêtre
		fenetre.blit(fond, positionFond)
		
		# On colle le texte sur la fenêtre
		# fenetre.blit(texte2, positionTexte2)
		# fenetre.blit(texte, positionTexte)
		
		# On met le programme en pause pendant quelques secondes pour économiser du CPU
		pygame.time.wait(5)
		
		# On met à jour l'horloge
		duree += horloge.tick(60)
		
		# On affiche l'horloge
		if duree < debutJeu :
			decompte = debutJeu - duree
			# if decompte > 4000 :
				# texte4 = "Votre jeu va démarrer dans " + str((debutJeu - duree)/1000) + " secondes"
			# else :
				# texte4 = "Votre jeu va démarrer dans " + str(debutJeu - duree) + " milisecondes"
			# texte3 = maFont2.render(texte4, True, (255,0,0))
			# fenetre.blit(texte3, (0, 18))
		elif duree >= debutJeu :
			mode = 1
		
		# On rafraichit l'affichage
		pygame.display.flip()
	
	if mode == 1 :
		jeu(fenetre, tailleFenetre)

