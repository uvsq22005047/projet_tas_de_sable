#########################################################
# Groupe LDDBI 6
# Clémence GERMETTE
# Sofia TERKI
# Erwan MAIRE
# Adam JACCOU
# https://github.com/uvsq22005047/projet_tas_de_sable.git
#########################################################

#librairie
import tkinter as tk 
import random

#Constante
HAUTEUR, LARGEUR = 500, 500
TAILLE_GRILLE = 3

#variables global
configuration = []
liste_widgets = []
historique = []


#fonctions


def affichage():
    canvas.delete('all')
    del liste_widgets[:]
    for i in range(TAILLE_GRILLE):
        for j in range(TAILLE_GRILLE):
            liste_widgets.append(canvas.create_text(((i+1)*LARGEUR/TAILLE_GRILLE)-(LARGEUR/TAILLE_GRILLE)/2,
             ((j+1)*HAUTEUR/TAILLE_GRILLE)-(HAUTEUR/TAILLE_GRILLE)/2, text=configuration[i][j]))
    print(liste_widgets)


def config_aleatoire():
    global configuration
    if configuration != []:
        configuration = []

    for i in range(TAILLE_GRILLE):
            configuration.append([random.randint(0,10) for j in range(TAILLE_GRILLE)])
    print(configuration)

    affichage()

    
           
def sauvegarder_configuration():
    global historique
    historique.append(configuration)
    print(historique)


def instable():
    global configuration, liste_instable
    liste_instable = []
    for i in range(TAILLE_GRILLE):
            for j in range(TAILLE_GRILLE):
                if configuration[i][j] > 3:
                    liste_instable.append(configuration[i][j])


def stabilisation():
    global configuration
    for i in range(TAILLE_GRILLE):
        for j in range(TAILLE_GRILLE):
            if configuration[i][j] > 3:
                configuration[i][j] -= 4
                if i == 0:
                    configuration[i+1][j] += 1
                elif i == TAILLE_GRILLE-1:
                    configuration[i-1][j] += 1
                else:
                    configuration[i+1][j] += 1
                    configuration[i-1][j] += 1    
                if j == 0:
                    configuration[i][j+1] += 1
                elif j == TAILLE_GRILLE-1:
                    configuration[i][j-1] += 1
                else:
                    configuration[i][j+1] += 1
                    configuration[i][j-1] += 1
    affichage()
    instable()  
    if liste_instable != []:
        canvas.after(1000, stabilisation)         
        




#création de la fenetre graphique
racine = tk.Tk()
canvas = tk.Canvas (racine, bg='white', height=HAUTEUR, width=LARGEUR)


#création des widgets
button_creation_configuration = tk.Button (text ='Création', command = lambda : config_aleatoire())
button_sauvegarder = tk.Button(text = 'Sauvegarder', command = lambda : sauvegarder_configuration())
button_stabilisation = tk.Button(text="Stabiliser", command = lambda : stabilisation()) 

#placement des widgets
canvas.grid(column=0, columnspan=3)
button_creation_configuration.grid(column=0, row = 1)
button_sauvegarder.grid(column=2, row = 1)
button_stabilisation.grid(column=1, row = 1)

#lancement de la fenetre
racine.mainloop()






#test 1