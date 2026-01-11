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
