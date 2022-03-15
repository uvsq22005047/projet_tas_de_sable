#########################################################
# Groupe LDDBI 6
# Clémence GERMETTE
# Sofia TERKI
# Erwan MAIRE
# Adam JACCOU
# https://github.com/uvsq22005047/projet_tas_de_sable.git
#########################################################

######################################################### Librairie #
import tkinter as tk 
import random

######################################################### Constante #
# Dimension du tas de sable
HAUTEUR, LARGEUR = 500, 500
TAILLE_GRILLE = 30

######################################################### Variables global #
# Configuration
configuration = []
config_predefini = ["vide", "Random", "Pile centrée", "Max Stable", "Double Max Stable", "Identity"]
# Affichage tas de sable
cases_grille = []
type_affichage = "gris"
# Sauvegarde
historique = []

######################################################### Fonctions #

# fonction d'affichage du tas de sable
def affichage(x=type_affichage):
    global type_affichage
    type_affichage = x
    if x == "chiffre":
        affichage_chiffre()
    elif x == "gris":
        affichage_gris()
    elif x == "couleur":
        affichage_couleur()

def affichage_chiffre():
    canvas.delete('all')
    del cases_grille[:]
    for i in range(TAILLE_GRILLE):
        for j in range(TAILLE_GRILLE):
            cases_grille.append(canvas.create_text(((i+1)*LARGEUR/TAILLE_GRILLE)-(LARGEUR/TAILLE_GRILLE)/2,
             ((j+1)*HAUTEUR/TAILLE_GRILLE)-(HAUTEUR/TAILLE_GRILLE)/2, text=configuration[i][j]))

def affichage_gris():
    canvas.delete('all')
    del cases_grille[:] 
    for i in range(TAILLE_GRILLE):
        for j in range(TAILLE_GRILLE):
           cases_grille.append(canvas.create_rectangle(i*(LARGEUR/TAILLE_GRILLE), j*(HAUTEUR/TAILLE_GRILLE),
           (i+1)*(LARGEUR/TAILLE_GRILLE), (j+1)*(HAUTEUR/TAILLE_GRILLE),
           fill = '#{:02x}{:02x}{:02x}'.format(2*configuration[i][j], 2*configuration[i][j], 2*configuration[i][j])))

def affichage_couleur():
    """
    Fonction qui associe à chaque valeur de la configuration une couleur
    """
    canvas.delete('all')
    del cases_grille[:]
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
            cases_grille.append(canvas.create_rectangle(i*(LARGEUR/TAILLE_GRILLE), j*(HAUTEUR/TAILLE_GRILLE),
             (i+1)*(LARGEUR/TAILLE_GRILLE), (j+1)*(HAUTEUR/TAILLE_GRILLE),fill = color, outline = color))

# Fonction de création de configuration
def config_vide():
    global configuration
    if configuration != []:
        configuration = []
    for i in range(TAILLE_GRILLE):
            configuration.append([0 for j in range(TAILLE_GRILLE)])
    return configuration

def config_random():
    global configuration
    if configuration != []:
        configuration = []
    for i in range(TAILLE_GRILLE):
            configuration.append([random.randint(0, 4) for j in range(TAILLE_GRILLE)])
    return configuration

def config_pile_centree():
    """
    Fonction qui attribue N grains de sable à la case du milieu et 0 aux autres
    """
    global configuration
    N = int(input("Entrer un chiffre"))
    for i in range(TAILLE_GRILLE):
        for j in range(TAILLE_GRILLE):
            configuration[i][j] = 0
    configuration[TAILLE_GRILLE//2][TAILLE_GRILLE//2] = N
    return configuration

def config_max_stable():
    global configuration
    if configuration != []:
        configuration = []
    for i in range(TAILLE_GRILLE):
            configuration.append([3 for j in range(TAILLE_GRILLE)])
    return configuration

def config_double_max_stable():
    """"
    Fonction qui additionne la configuration Max stable avec elle-même
    """
    global configuration
    configuration = operation_configurations("Addition", config_max_stable(), config_max_stable())
    return configuration

def config_Identity():
    global configuration
    configuration = operation_configurations("Soustraction",)
    pass

def config_choix():
    pass

# Fonction de selection
def selection_config(event): 
    if affichage_liste_config.get(affichage_liste_config.curselection()) == config_predefini[0]:
        config_vide()
    elif affichage_liste_config.get(affichage_liste_config.curselection()) == config_predefini[1]:
        config_random()
    elif affichage_liste_config.get(affichage_liste_config.curselection()) == config_predefini[2]:
        config_pile_centree()
    elif affichage_liste_config.get(affichage_liste_config.curselection()) == config_predefini[3]:
        config_max_stable()
    elif affichage_liste_config.get(affichage_liste_config.curselection()) == config_predefini[4]:
        config_double_max_stable()
    elif affichage_liste_config.get(affichage_liste_config.curselection()) == config_predefini[5]:
        config_Identity()
    affichage()


# Fonction modifiant la configuration

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
        canvas.after(1, stabilisation)    

def operation_configurations(operation, config1, config2):
    """
    Fonction qui additionne ou soustrait une configuration sélectionné à la configuration courente
    """
    global configuration
    if operation == "Addition":
        for i in range(TAILLE_GRILLE):
            for j in range(TAILLE_GRILLE):
                configuration[i][j] = config1[i][j] + config2[i][j]
    elif operation == "Soustraction":
        for i in range(TAILLE_GRILLE):
            for j in range(TAILLE_GRILLE):
                configuration[i][j] = config1[i][j] - config2[i][j]
    return configuration
  

# Fonction de sauvegarde
def sauvegarder_configuration():
    global historique
    historique.append(configuration)
    print(historique)
    

######################################## Création de la fenetre graphique ########################################

### Création élément graphique

# Fenetre principal
racine = tk.Tk()
racine.title("Simulation d'un tas de sable")

# Liste des configuration à choisir
config = tk.LabelFrame(racine, text="choisir une configuration", bd=0)

affichage_liste_config = tk.Listbox(config, bd=0, activestyle='none')
for i in config_predefini:
    affichage_liste_config.insert('end', i)

# Tas de sable
canvas = tk.Canvas (racine, bg='white', height=HAUTEUR, width=LARGEUR)

# Choix du type d'affichage
parametre_affichage = tk.LabelFrame(racine, text="Parametre d'affichage", bd=0)

# Widgets boutton
button_sauvegarder = tk.Button(text = 'Sauvegarder', command = lambda : sauvegarder_configuration())
button_stabilisation = tk.Button(text="Stabiliser", command = lambda : stabilisation()) 


button_chiffre = tk.Button(parametre_affichage, text="chiffre", command= lambda x="chiffre": affichage(x))
button_gris = tk.Button(parametre_affichage, text="gris", command= lambda x="gris": affichage(x))
button_couleur = tk.Button(parametre_affichage, text="couleur", command= lambda x="couleur": affichage(x))

### Placement des éléments graphique

# Widgets d'affichage
config.grid(column=0, row=0)
canvas.grid(column=1, row=0, rowspan=3) 
parametre_affichage.grid(column=2, row=0)
affichage_liste_config.pack()

# Widgets boutton
button_sauvegarder.grid(column=2, row=1)
button_stabilisation.grid(column=0, row=1)

button_chiffre.pack()
button_gris.pack()
button_couleur.pack()

# Liaison d'évenement à des fonctions
affichage_liste_config.bind("<<ListboxSelect>>", selection_config)

# Parametre par défaut
config_vide()
affichage()

# Lancement de la fenetre graphique
racine.mainloop()