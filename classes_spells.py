from spells import attaque_auto, coupret_hit, execute, boule_de_feu, lance_de_glace, nova_arcane, kriss, flageler, coup_d_epee, colere, eclat_lunaire, nova_solaire, tir_rapide, tir_explosif, morsure_du_serpent
from spells import fouet_mental, lumiere_vascillante, jugement


classes_attackes = {
    "guerrier": [attaque_auto, coupret_hit, execute],
    "mage": [boule_de_feu, lance_de_glace, nova_arcane],
    "voleur": [kriss, flageler, coup_d_epee],
    "druide": [colere, eclat_lunaire, nova_solaire],
    "chasseur": [tir_rapide, tir_explosif, morsure_du_serpent],
    "pretre": [fouet_mental, lumiere_vascillante, jugement]
}
    