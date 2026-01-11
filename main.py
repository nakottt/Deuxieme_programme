from spells import attaque_auto, coupret_hit, execute
from spells import poule_attaque
# constantes
RACES = ["Humain", "Elfe", "Nain", "Gnome", "Worgen", "Drainei"]
CLASSES = ["Guerrier", "Mage", "Voleur", "Druide", "Chasseur", "Pretre"]
# les points de vie dépendent de la classe
hp_joueur = {"Guerrier": 200, "Mage": 100, "Voleur": 120, "Druide": 130, "Chasseur": 140, "Pretre": 90}

# etape 1 : acceuillir le joueur
print ("Bonjour, créez votre personnage !")


# etape 2 : creer le personnage


# etape 2a : choisir une race
race = input ("choisir une race parmi les suivantes : Humain, Elfe, Nain, Gnome, Worgen, Drainei : ")

while race not in RACES: 
    race = input ("Non, choisir parmi les races diponnibles : Humain, Elfe, Nain, Gnome, Worgen, Drainei:")

print ("Merci d'avoir choisi", race)



#etape 2b : choisir une classe
classe = input ("choisir une classe parmi les suivantes : Guerrier, Mage, Voleur, Druide, Chasseur, Pretre : ")

while classe not in CLASSES:
    classe = input ("Non, choisir parmi les classes disponibles : Guerrier, Mage, Voleur, Druide, Chasseur, Pretre : ")

print ("Merci d'avoir choisi", classe)



# etape 2c : choisir un nom
nom_joueur = input("Entrez le nom de votre personnage : ")


# etape 2d : afficher le personnage
print ("Votre personnage s'appelle", nom_joueur ,"est de race", race ,"et de classe", classe ,". Bonne aventure !")

print (nom_joueur,"possède", hp_joueur[classe], "points de vie.")

#############################################
#Premier combat
#############################################
from fight import pve
from classes_spells import classes_attackes

poule = {"nom": "poule sauvage","pv":30, "attaque":poule_attaque}
hp_joueur[classe] = pve(nom_joueur, classe, hp_joueur[classe], poule["nom"], poule["pv"])

dinde = {"nom": "dinde enragée","pv":45, "attaque":poule_attaque}
hp_joueur[classe] = pve(nom_joueur, classe, hp_joueur[classe], dinde["nom"], dinde["pv"])



# print ("Une poule sauvage de barbarie, seche et nerveuse apparaît !")
# # ennemi : poule sauvage
# poule_nom = "Poule sauvage"
# poule_hp = 30

# print (poule_nom, "possède", poule_hp, "points de vie.")
# # combat
# while poule_hp >0 and hp_joueur[classe]>0:
#     # le joueur attaque
#     attaque = input ("Appuyez sur A pour attaquer la poule...")
#     if attaque == "A":
#         print (nom_joueur, "attaque la", poule_nom,"!")
#         poule_hp = attaque_auto (poule_hp, nom_joueur)
#         if poule_hp <=0:
#             print ("La", poule_nom, "est vaincue !")
#             break
#         print (poule_nom, "possède encore", poule_hp, "points de vie.")
#         # la poule attaque
#         print (poule_nom, "attaque", nom_joueur,"!")
#         damages = poule_attaque(hp_joueur[classe])
#         hp_joueur[classe] -= damages
        
#         if hp_joueur[classe] <=0:
#             print (nom_joueur, "est vaincu ! Game Over.")
#             break
#         print (nom_joueur, "possède encore", hp_joueur[classe], "points de vie.")
#     else:
#         print ("Vous vous enfuyez comme une merde et le combat est terminé")