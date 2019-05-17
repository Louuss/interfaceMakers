# import random
# import sys
# from threading import Thread
# import time
# from tkinter import *
# import tkinter.messagebox as mb
#
# class Compteur(Thread):
#
#     """Thread chargé simplement d'afficher une lettre dans la console."""
#
#     def __init__(self, minutes, fenetre):
#         Thread.__init__(self)
#         self.timing = minutes*60 #temps en seconde
#         self.fenetre = fenetre
#         self.label = Label(fenetre, text="")
#         self.label.pack()
#         self.label.place(relx = 0.45, rely = 0.4, height = 140, width = 150)
#         self.label.config(font=("Courier", 44))
#         self.attentionLabel = Label(fenetre, text="EXPLOSION", fg="red")
#         self.attentionLabel.config(font = ("Arial", 44))
#
#
#     def convertTime(self, seconds):
#         secs = "%d" % (seconds % 60)
#         if seconds % 60 < 10:
#             secs = "0" + secs
#
#         mins = "%d:" % (seconds / 60 )
#         if seconds / 60 < 10 :
#             mins = "0" + mins
#
#         return mins+secs
#
#
#     def run(self):
#         """Code à exécuter pendant l'exécution du thread."""
#
#         while self.timing > 0 :
#             self.timing -= 1
#             time.sleep(1)
#             print (self.convertTime(self.timing))
#             self.label["text"]= self.convertTime(self.timing)
#         self.hello()
#
#
#     def hello(self):
#         print("hello")
#         self.attentionLabel.place(relx = 0.4, rely = 0.6)
#         #self.attentionLabel.pack()




import random
import sys
from threading import Thread
import time
from tkinter import *
import tkinter.messagebox as mb

__end = 0

class Compteur(Thread):
    __end = 0
    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, minutes, fenetre):
        Thread.__init__(self)
        self.timing = minutes*60 #temps en seconde
        self.fenetre = fenetre
        self.label = Label(fenetre, text="")
        self.label.pack()
        self.label.place(relx = 0.45, rely = 0.4, height = 140, width = 150)
        self.label.config(font=("Courier", 44))
        self.attentionLabel = Label(fenetre, text="EXPLOSION", fg="red")
        self.attentionLabel.config(font = ("Arial", 44))


    def convertTime(self, seconds):
        secs = "%d" % (seconds % 60)
        if seconds % 60 < 10:
            secs = "0" + secs

        mins = "%d:" % (seconds / 60 )
        if seconds / 60 < 10 :
            mins = "0" + mins

        return mins+secs


    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        global __end
        while self.timing > 0 :
            self.timing -= 1



            if self.updateEnd():
                break

            time.sleep(1)


            print (self.convertTime(self.timing))
            self.label["text"]= self.convertTime(self.timing)

        if self.__end == 0 :
            self.hello()
        else :
            print("safe")


    def updateEnd(self):
        #verifier si un message reçu pour dire bombe desamorcée
        return False
        if False :
            return False

        if True :
            self.__end == 1
            return True



    def changeEnd(self):
        global __end
        self.__end = 1


    def hello(self):
        print("hello")
        self.attentionLabel.place(relx = 0.4, rely = 0.6)
        #self.attentionLabel.pack()
