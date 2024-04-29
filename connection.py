from tkinter import *
from tkinter import ttk
import os
import sys
from launcher import *
import musik as mk

# Class for the base interface of login and registration
class Con_inscr(Tk):
    """
    Class for creating the login interface.
    """
    def __init__(self):
        super().__init__()
        self.title("Connexion")  # Window title
        self.geometry('300x300')  # Sets the initial size of the window
        self.minsize(350, 190)  
        self.maxsize(350, 190)  
        self.eval('tk::PlaceWindow . center')  # Center the window on the screen

# Class for login using the base interface
class Connexion(Con_inscr):
    """
    Class to log in by retrieving usernames and passwords
    stored in a txt file.
    """
    def __init__(self):
        Con_inscr.__init__(self)
        
        # Widgets configuration
        self.mot = Label(self, text="Veuillez-vous connecter").grid(row=0, column=1)
        self.ide = Label(self, text="Identifiant").grid(row=2, column=0)
        self.mdp = Label(self, text="Mot de passe").grid(row=3, column=0)

        # Entry fields for username and password
        self.identi = Entry(self)
        self.identi.grid(row=2, column=1)
        self.mdp1 = Entry(self, show='*')
        self.mdp1.grid(row=3, column=1)
    
        # Buttons for login and registration
        conne = ttk.Button(self, text="Connexion", command=self.verif).grid(row=4, column=1)
        insc = ttk.Button(self, text="Inscription", command=self.supp_page).grid(row=5, column=1)
      
    def verif(self):
        # Retrieving entered data
        id = self.identi.get()
        mdp1 = self.mdp1.get()
        dico = {}
        with open(os.path.join(sys.path[0], "userbase.txt"), "r") as lire:
            k = lire.readlines()

        # Building a dictionary from the file
        for i in k:
            a = i.rstrip("\n").split(":")
            dico[a[0]] = a[-1]
        
        # Checking the entered information
        if id == "" or mdp1 == "":
            Label(self, text="Veuillez écrire dans les champs obligatoires !").place(x=10, y=130)
        else:
            if id in dico.keys():
                if dico[id] != mdp1:
                    Label(self, text="Votre mot de passe ou identifiant est faux.").place(x=10, y=130)
                else:
                    self.destroy()
                    mk.music_player.start_music()
                    a = Main_Interface(id)
            else:
                Label(self, text="Vérifier si votre identifiant est bon, sinon veuillez-vous inscrire.").place(x=10, y=130)

    def supp_page(self):
        """
        Method to close the current window and open a new one for registration.
        """
        self.destroy()
        der = Inscr()
        der.mainloop()
        
# Class for registration using the base interface
class Inscr(Con_inscr):
    """
    Class for registering by saving a new username and password
    in a txt file.
    """
    def __init__(self):
        Con_inscr.__init__(self)

        # Widgets configuration
        self.a = Label(self, text="Veuillez-vous inscrire").grid(row=0, column=1)
        self.ide = Label(self, text="Identifiant").grid(row=2, column=0)
        self.mdp = Label(self, text="Mot de passe").grid(row=3, column=0)

        # Entry fields for username and password
        self.ide1 = Entry(self)
        self.ide1.grid(row=2, column=1)
        self.mdp2 = Entry(self, show='*')
        self.mdp2.grid(row=3, column=1)
        
        # Buttons for registration and return to login
        insc = ttk.Button(self, text="S'inscrire", command=self.fichier).grid(row=4, column=1)
        conne = ttk.Button(self, text="Retour connexion", command=self.supp).grid(row=5, column=1)
    
    def fichier(self):
        # Retrieving entered data
        id1 = self.ide1.get()
        mdp2 = self.mdp2.get()
        dicoff = {}
        with open(os.path.join(sys.path[0], "userbase.txt"), "r") as lire:
            k = lire.readlines()

        # Building a dictionary from the file
        for i in k:
            a = i.rstrip("\n").split(":")
            dicoff[a[0]] = a[-1]
        
        # Checking and recording the new data
        if id1 in dicoff.keys():
            Label(self, text="Cet identifiant existe déjà. Veuillez-en choisir un autre.").place(x=10, y=130)
        else:
            if id1 == "" or mdp2 == "":
                Label(self, text="Veuillez écrire dans les champs obligatoires !").place(x=10, y=130)
            else:
                with open(os.path.join(sys.path[0], "userbase.txt"), "a") as ouvre:
                    ouvre.writelines([id1, ":", mdp2, "\n"])
                self.supp()

    def supp(self):
        """
        Method to close the current window and open a new one for login.
        """
        self.destroy()
        av = Connexion()
        av.mainloop()

if __name__ == "__main__":
    a = Connexion()
    a.mainloop()
