from tkinter import *
from tkinter.messagebox import *
import time
from compteur import Compteur




fenetre = Tk()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
# use the next line if you also want to get rid of the titlebar
fenetre.overrideredirect(1)
fenetre.geometry("%dx%d+0+0" % (w, h))


thread = Compteur(0.2, fenetre)
thread.start()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
