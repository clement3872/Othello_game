from tkinter import *
from tkinter import ttk
import os
import sys
from launcher import *
import musik as mk

# Classe pour l'interface de base des connexions et inscriptions
class Con_inscr(Tk):
    """
    Classe permettant d'instancier l'interface de connexion.
    """
    def __init__(self):
        super().__init__()
        self.title("Connexion")  # Titre de la fenêtre
        self.geometry('300x300')  # Définit la taille initiale de la fenêtre
        self.minsize(350, 190)  
        self.maxsize(350, 190)  
        self.eval('tk::PlaceWindow . center')  # Centrer la fenêtre à l'écran

# Classe pour la connexion utilisant l'interface de base
class Connexion(Con_inscr):
    """
    Classe permettant de se connecter en récupérant les identifiants et mots de passe
    enregistrés dans un fichier txt.
    """
    def __init__(self):
        Con_inscr.__init__(self)
        
        # Configuration des widgets
        self.mot = Label(self, text="Veuillez-vous connecter").grid(row=0, column=1)
        self.ide = Label(self, text="Identifiant").grid(row=2, column=0)
        self.mdp = Label(self, text="Mot de passe").grid(row=3, column=0)

        # Champs de saisie pour l'identifiant et le mot de passe
        self.identi = Entry(self)
        self.identi.grid(row=2, column=1)
        self.mdp1 = Entry(self, show='*')
        self.mdp1.grid(row=3, column=1)
    
        # Boutons pour la connexion et l'inscription
        conne = ttk.Button(self, text="Connexion", command=self.verif).grid(row=4, column=1)
        insc = ttk.Button(self, text="Inscription", command=self.supp_page).grid(row=5, column=1)
      
    def verif(self):
        # Récupération des données saisies
        id = self.identi.get()
        mdp1 = self.mdp1.get()
        dico = {}
        with open(os.path.join(sys.path[0], "userbase.txt"), "r") as lire:
            k = lire.readlines()

        # Construction d'un dictionnaire à partir du fichier
        for i in k:
            a = i.rstrip("\n").split(":")
            dico[a[0]] = a[-1]
        
        # Vérification des informations saisies
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
        Méthode pour fermer la fenêtre actuelle et ouvrir une nouvelle pour l'inscription.
        """
        self.destroy()
        der = Inscr()
        der.mainloop()
        
# Classe pour l'inscription utilisant l'interface de base
class Inscr(Con_inscr):
    """
    Classe permettant de s'inscrire en enregistrant un nouvel identifiant et mot de passe
    dans un fichier txt.
    """
    def __init__(self):
        Con_inscr.__init__(self)

        # Configuration des widgets
        self.a = Label(self, text="Veuillez-vous inscrire").grid(row=0, column=1)
        self.ide = Label(self, text="Identifiant").grid(row=2, column=0)
        self.mdp = Label(self, text="Mot de passe").grid(row=3, column=0)

        # Champs de saisie pour l'identifiant et le mot de passe
        self.ide1 = Entry(self)
        self.ide1.grid(row=2, column=1)
        self.mdp2 = Entry(self, show='*')
        self.mdp2.grid(row=3, column=1)
        
        # Boutons pour l'inscription et le retour à la connexion
        insc = ttk.Button(self, text="S'inscrire", command=self.fichier).grid(row=4, column=1)
        conne = ttk.Button(self, text="Retour connexion", command=self.supp).grid(row=5, column=1)
    
    def fichier(self):
        # Récupération des données saisies
        id1 = self.ide1.get()
        mdp2 = self.mdp2.get()
        dicoff = {}
        with open(os.path.join(sys.path[0], "userbase.txt"), "r") as lire:
            k = lire.readlines()

        # Construction d'un dictionnaire à partir du fichier
        for i in k:
            a = i.rstrip("\n").split(":")
            dicoff[a[0]] = a[-1]
        
        # Vérification et enregistrement des nouvelles données
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
        Méthode pour fermer la fenêtre actuelle et ouvrir une nouvelle pour la connexion.
        """
        self.destroy()
        av = Connexion()
        av.mainloop()

if __name__ == "__main__":
    a = Connexion()
    a.mainloop()
