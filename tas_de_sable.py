#########################################################
# Groupe LDDBI 6
# Clémence GERMETTE
# Sofia TERKI
# Erwan MAIRE
# Adam JACCOU
# https://github.com/uvsq22005047/projet_tas_de_sable.git
#########################################################

import tkinter as tk 
import random
#import numpy as np

#création des variables global
LONGUEUR = 500
LARGEUR = 500
TAILLE_GRILLE = 3
configuration = []
historique = []

#création de la fenetre graphique
racine = tk.Tk()
canvas = tk.Canvas (racine, bg='white', height=LONGUEUR, width=LARGEUR)


#création des fonctions

def creation_configuration_aleatoire():
    """fonction qui crée un configuration"""
    """
    global configuration
    configuration = np.random.randint(10, size=(3,3))
    print(configuration)
    """
    global configuration
    if configuration != []:
        configuration = []

    for i in range(TAILLE_GRILLE):
            configuration.append([random.randint(0,10) for j in range(TAILLE_GRILLE)])
    print(configuration)

    canvas.delete('all')
    for a in range(TAILLE_GRILLE):
        for b in range(TAILLE_GRILLE):
            canvas.create_text(((a+1)*LARGEUR/TAILLE_GRILLE)-(LARGEUR/TAILLE_GRILLE)/2,
             ((b+1)*LONGUEUR/TAILLE_GRILLE)-(LONGUEUR/TAILLE_GRILLE)/2, text=configuration[a][b])
           
def sauvegarder_configuration():
    global historique
    historique.append(configuration)
    print(historique)



#création des widgets
button_creation_configuration = tk.Button (text ='Création', command = lambda : creation_configuration_aleatoire())
button_sauvegarder = tk.Button(text = 'Sauvegarder', command = lambda : sauvegarder_configuration())

#placement des widgets
canvas.grid(column=0, columnspan=2)
button_creation_configuration.grid(column=0, row = 1)
button_sauvegarder.grid(column=1, row = 1)

#lancement de la fenetre
racine.mainloop()






