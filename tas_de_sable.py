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
TAILLE_GRILLE = 30

#variables global
configuration = []
liste_widgets = []
historique = []

#############
# fonctions #
#############

#fonction d'affichage


def affichage_gris():
    canvas.delete('all')
    del liste_widgets[:] 
    for i in range(TAILLE_GRILLE):
        for j in range(TAILLE_GRILLE):
           liste_widgets.append(canvas.create_rectangle(i*(LARGEUR/TAILLE_GRILLE), j*(HAUTEUR/TAILLE_GRILLE),
           (i+1)*(LARGEUR/TAILLE_GRILLE), (j+1)*(HAUTEUR/TAILLE_GRILLE),
           fill = '#{:02x}{:02x}{:02x}'.format(2*configuration[i][j], 2*configuration[i][j], 2*configuration[i][j])))


"""Fonction qui associe à chaque valeur de la configuration une couleur"""
def affichage_couleur():
    canvas.delete('all')
    del liste_widgets[:]
    for i in range(TAILLE_GRILLE):
        for j in range(TAILLE_GRILLE):
            if configuration[i][j] == 0:
                color = "blue"
            elif configuration[i][j] == 1:
                color = "green"
            elif configuration[i][j] == 2:
                color = "yellow"
            elif configuration[i][j] == 3:
                color = "orange"
            elif configuration[i][j] > 3:
                color = "red"
            liste_widgets.append(canvas.create_rectangle(i*(LARGEUR/TAILLE_GRILLE), j*(HAUTEUR/TAILLE_GRILLE),
             (i+1)*(LARGEUR/TAILLE_GRILLE), (j+1)*(HAUTEUR/TAILLE_GRILLE),fill = color, outline = color))


def affichage_chiffre():
    canvas.delete('all')
    del liste_widgets[:]
    for i in range(TAILLE_GRILLE):
        for j in range(TAILLE_GRILLE):
            liste_widgets.append(canvas.create_text(((i+1)*LARGEUR/TAILLE_GRILLE)-(LARGEUR/TAILLE_GRILLE)/2,
             ((j+1)*HAUTEUR/TAILLE_GRILLE)-(HAUTEUR/TAILLE_GRILLE)/2, text=configuration[i][j]))
    print(liste_widgets)


#création configuration

def config_aleatoire():
    global configuration
    if configuration != []:
        configuration = []
    for i in range(TAILLE_GRILLE):
            configuration.append([random.randint(0, 4) for j in range(TAILLE_GRILLE)])
    print(configuration)
    affichage_couleur()

def config_max():
    global configuration
    if configuration != []:
        configuration = []
    for i in range(TAILLE_GRILLE):
            configuration.append([4 for j in range(TAILLE_GRILLE)])
    affichage_couleur()


"""Fonction qui attribue N grains de sable à la case du milieu et 0 aux autres"""
def config_Pile_centree():
    global configuration
    N = int(input("Entrer un chiffre"))
    for i in range(TAILLE_GRILLE):
        for j in range(TAILLE_GRILLE):
            configuration[i][j] = 0
    configuration[TAILLE_GRILLE/2][TAILLE_GRILLE/2] = N
    affichage_couleur()


""""Fonction qui additionne la configuration Max stable avec elle-même"""
def config_double_max_stable():
    pass

def config_Identity():
    pass



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
    affichage_couleur()
    instable()  
    if liste_instable != []:
        canvas.after(1, stabilisation)    

"""Fonction qui permet d'additionner les éléments case par case deux configurations """
def addition_configurations():
    pass

        

#création de la fenetre graphique
racine = tk.Tk()
canvas = tk.Canvas (racine, bg='white', height=HAUTEUR, width=LARGEUR)


#création des widgets
button_creation_configuration = tk.Button (text ='Création', command = lambda : config_aleatoire())
button_sauvegarder = tk.Button(text = 'Sauvegarder', command = lambda : sauvegarder_configuration())
button_stabilisation = tk.Button(text="Stabiliser", command = lambda : stabilisation()) 
button_max = tk.Button(text="max", command = lambda : config_max()) 
button_pile_centree = tk.Button(text = "Pile centrée", command = lambda : config_Pile_centree() )
button_double_max = tk.Button(text = "Double max")

#placement des widgets
canvas.grid(column=0, columnspan=6) 
button_creation_configuration.grid(column=0, row = 1)
button_sauvegarder.grid(column=2, row = 1)
button_stabilisation.grid(column=1, row = 1)
button_max.grid(column=3, row = 1)
button_pile_centree.grid(column = 4, row = 1)
button_double_max.grid(column=5, row=1)

#lancement de la fenetre
racine.mainloop()



#change


#test 1