from fight import pve
from classes_spells import classes_attackes
from map_system import creer_map, afficher_map, deplacer_joueur 
from spells import poule_attaque
# ======================
# CONSTANTES
# ======================
RACES = ["Humain", "Elfe", "Nain", "Gnome", "Worgen", "Drainei"]
CLASSES = ["Guerrier", "Mage", "Voleur", "Druide", "Chasseur", "Pretre"]

HP_PAR_CLASSE = {
    "Guerrier": 200,
    "Mage": 100,
    "Voleur": 120,
    "Druide": 130,
    "Chasseur": 140,
    "Pretre": 90
}

# ======================
# CRÉATION DU PERSONNAGE
# ======================
print("Bonjour, créez votre personnage !")

race = input("Choisir une race : ")
while race not in RACES:
    race = input("Race invalide, recommence : ")

classe = input("Choisir une classe : ")
while classe not in CLASSES:
    classe = input("Classe invalide, recommence : ")

nom_joueur = input("Entrez le nom de votre personnage : ")

print(f"\nVotre personnage s'appelle {nom_joueur}, race {race}, classe {classe}.")
print(f"{nom_joueur} possède {HP_PAR_CLASSE[classe]} points de vie.\n")

# ======================
# JOUEUR (STRUCTURE UNIQUE)
# ======================
joueur = {
    "nom": nom_joueur,
    "classe": classe,
    "pv": HP_PAR_CLASSE[classe],
    "pv_max": HP_PAR_CLASSE[classe]
}

# ======================
# PREMIERS COMBATS SCRIPTÉS
# ======================
poule = {"nom": "poule sauvage", "pv": 30, "attaque": poule_attaque}
joueur["pv"] = pve(joueur["nom"], joueur["classe"], joueur["pv"], poule["nom"], poule["pv"])

dinde = {"nom": "dinde enragée", "pv": 45, "attaque": poule_attaque}
joueur["pv"] = pve(joueur["nom"], joueur["classe"], joueur["pv"], dinde["nom"], dinde["pv"])

# ======================
# MAP
# ======================
map_data = creer_map()

# ======================
# MOBS DE LA MAP (INDÉPENDANTS DES CLASSES)
# ======================
mobs = [
    {"nom": "Gobelin", "pv": 50, "attaque": poule_attaque},
    {"nom": "Orc", "pv": 80, "attaque": poule_attaque},
    {"nom": "Troll", "pv": 100, "attaque": poule_attaque}
]

# ======================
# BOUCLE PRINCIPALE
# ======================
while joueur["pv"] > 0:
    afficher_map(map_data)
    print(f"❤️ PV : {joueur['pv']}/{joueur['pv_max']}")
    direction = input("Déplacez votre personnage (z/q/s/d) ou 'x' pour quitter : ").lower()

    if direction == "x":
        print("Merci d'avoir joué !")
        break

    joueur["pv"] = deplacer_joueur(
        map_data,
        direction,
        joueur,
        mobs
    )

print("💀 Fin de l'aventure.")
