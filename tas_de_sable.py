#########################################################
# Groupe LDDBI 6
# Clémence GERMETTE
# Sofia TERKI
# Erwan MAIRE
# https://github.com/uvsq22005047/projet_tas_de_sable.git
#########################################################

import tkinter as tk 
import numpy as np

#création des variables global
longueur = 500
largeur = 500
configuration = []

#création de la fenetre graphique
racine = tk.Tk()
canvas = tk.Canvas (racine, bg='white', height=longueur, width=largeur)
canvas.grid()

#création des fonctions
def creation_configuration():
    """fonction qui crée un configuration"""
    global configuration
    configuration = np.random.randint(10, size=(3,3))
    print(configuration)



#création des widgets
button_creation_configuration = tk.Button (text ='Création', command = lambda : creation_configuration())


#placement des widgets
button_creation_configuration.grid(column=0, row = 1)

#lancement de la fenetre
racine.mainloop()






