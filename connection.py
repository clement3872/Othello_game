from tkinter import *
from tkinter import ttk, messagebox
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
        self.mot = Label(self, text="Please log in").grid(row=0, column=1)
        self.ide = Label(self, text="Username").grid(row=2, column=0)
        self.mdp = Label(self, text="Password").grid(row=3, column=0)

        # Entry fields for username and password
        self.identi = Entry(self)
        self.identi.grid(row=1, column=1, padx=10)
        self.mdp1 = Entry(self, show='*')
        self.mdp1.grid(row=2, column=1, padx=10)
    
        # Buttons for login and registration
        conne = ttk.Button(self, text="Log in", command=self.verif).grid(row=4, column=1)
        insc = ttk.Button(self, text="Sign up", command=self.supp_page).grid(row=5, column=1)

    
    def verif(self):
        """handle user registration and login verification in a tkinter application."""
        # Retrieve the username and password from the input fields
        id = self.identi.get()
        mdp1 = self.mdp1.get()

        # Initialize a dictionary to store data from userbase.txt
        dico = {}
        # Read userbase.txt file to load existing data into the dictionary
        with open(os.path.join(sys.path[0], "userbase.txt"), "r") as lire:
            k = lire.readlines()

            for i in k:
                a = i.rstrip("\n").split(":")
                dico[a[0]] = a[-1]
            
            # Check if the mandatory fields are filled
            if id == "" or mdp1 == "":
                Label(self, text="Please fill in the required fields!").place(x =10, y = 130)  
            
            # Check if the username exists in the dictionary
            else :
                if id in dico.keys():
                    if dico[id] != mdp1 :
                        Label(self, text="Your password or username is incorrect.").place(x =10, y = 130) 
                    else:
                        self.destroy()
                        mk.music_player.start_music()
                        a = Main_Interface(id)
                else:   
                    Label(self, text="Check if your username is correct, otherwise please sign up.").place(x =10, y = 130) 

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
        self.a = Label(self, text="Please sign up").grid(row=0, column=1)
        self.ide = Label(self, text="Username").grid(row=2, column=0)
        self.mdp = Label(self, text="Password").grid(row=3, column=0)

        # Entry fields for username and password
        self.ide1 = Entry(self)
        self.ide1.grid(row=1, column=1, padx=10)
        self.mdp2 = Entry(self, show='*')
        self.mdp2.grid(row=2, column=1, padx=10)
        
        # Buttons for registration and return to login
        insc = ttk.Button(self, text="Sign up", command=self.fichier).grid(row=4, column=1)
        conne = ttk.Button(self, text="Back to login", command=self.supp).grid(row=5, column=1)
    
    def fichier(self):
        # Retrieve the username and password from the input fields
        id1 = self.ide1.get()
        mdp2 = self.mdp2.get()
    
        # Initialize an empty dictionary to store existing user data
        dicoff = {}
    
        # Read the userbase.txt file to load existing user data into the dictionary
        with open(os.path.join(sys.path[0], "userbase.txt"), "r") as lire:
            for i in lire.readlines():
                a = i.rstrip("\n").split(":")
                dicoff[a[0]] = a[-1]
        if id1 in dicoff.keys():
            Label(self, text="This username already exists. Please choose another one.").place(x =10, y = 130)  
 
                    
        else:
            # If the username is new, verify that both username and password fields are filled
            if id1 == "" or mdp2 == "":
                Label(self, text="Please fill in the required fields!").place(x =10, y = 130)        
            else :
                dico = {}
                fichiers = open(os.path.join(sys.path[0], "saves", id1 + ".txt"), "w")
                hist = open(os.path.join(sys.path[0], "history_game", id1 + ".txt"), "a")
                with open(os.path.join(sys.path[0], "userbase.txt"), "a") as ouvre:
                    ouv = ouvre.writelines([id1, ":", mdp2, "\n"])
                    ouvre.close()
                

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
