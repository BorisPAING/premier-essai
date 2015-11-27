# -* -coding:Utf-8 -*

import os, sys, renpygame
import renpygame as pygame
from renpygame.locals import *

def jeu (fenetre, tailleFenetre) :
	# On définit la durée du jeu
	# dureeJeu = 31260
	dureeJeu = 5000 # valeur de test
	
	# On créé une horloge
	horloge = pygame.time.Clock()
	chronoJeu = 0
	
	# Avec convert() on charge en mémoire l'image du fond
	fond = pygame.image.load("dancefloor.jpg").convert()

	# On définit les coordonnées (x, y)) de la position où sera collé le fond
	positionFond = 0, 0
	
	# On charge le son "bouap" en mémoire
	sonBouapL = pygame.mixer.Sound("bouap_left.wav")
	sonBouapR = pygame.mixer.Sound("bouap_right.wav")
	sonBouap = pygame.mixer.Sound("bouap.wav")

	# Avec convert_alpha() on charge en mémoire lesImages du personnage en activant la transparence PNG
	persoDroite = pygame.image.load("persoDroite.png").convert_alpha()
	persoGauche = pygame.image.load("persoGauche.png").convert_alpha()
	persoHaut = pygame.image.load("persoHaut.png").convert_alpha()
	persoFace = pygame.image.load("persoFace.png").convert_alpha()
	perso = persoFace

	# On définit la taille du personnage
	taillePerso = 320, 240

	# On calcule la position (x, y) du personnage (ici, au centre de la fenêtre)
	positionPerso = 0, 0
	
	# Une boucle infinie pour l'affichage
	continuer = True
	while continuer:
		# Une boucle pour la gestion des évènements
		for event in pygame.event.get():
			# Si le joueur clique sur la croix, on ferme la fenêtre
			if event.type == pygame.QUIT: 
				sys.exit()
			# L'utilisateur presse une touche du clavier
			elif event.type == pygame.KEYDOWN:
				# Si l'utilisateur appuie sur la touche "flèche du haut"
				if event.key == K_UP:
					# on met à jour la position du personnage
					perso = persoHaut
					sonBouap.play()
				# Si l'utilisateur appuie sur la touche "flèche du bas"
				elif event.key == K_DOWN:
					# on met à jour la position du personnage
					perso = persoFace
					sonBouap.play()
				# Si l'utilisateur appuie sur la touche "flèche de gauche"
				elif event.key == K_LEFT:
					# on met à jour la position du personnage
					perso = persoGauche
					sonBouapL.play()
				# Si l'utilisateur appuie sur la touche "flèche de droite"
				elif event.key == K_RIGHT:
					# on met à jour la position du personnage
					perso = persoDroite
					sonBouapR.play()
		# On colle le fond sur la fenêtre
		fenetre.blit(fond, positionFond)
		
		# On colle le personnage sur la fenêtre
		fenetre.blit(perso, positionPerso)
		
		# On rafraichit l'affichage
		pygame.display.flip()
		
		# On met le programme en pause pendant quelques secondes pour économiser du CPU
		pygame.time.wait(5)
		
		# On met à jour le chrono
		chronoJeu += horloge.tick(60)
		
		if chronoJeu >= dureeJeu:
			continuer = False
