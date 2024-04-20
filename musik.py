from playsound import playsound
import multiprocessing as mp
# Module de musique
# Pas optimise
# Il faudra soit changer de library pour changer de musique soit trouver une meilleur
# solution pour gerer les threads
class Musik:
    music_on = True
    no_inter = 0 # 0 == Main ; 1 == Board
    def __init__(self):
        self.path_main = "Ressources/music/Airship_Thunderchild_opensource.mp3"
        self.path_board = "Ressources/music/ingame.mp3"
        
    def start_music(self):
        self.proc = mp.Process(target = self.main)
        self.proc.start()

    # Detruit la musique
    def destroy(self):
        if self.music_on:
            self.proc.terminate()
    
    # Fonction pour le bouton mute de la main interface
    def switch_main(self):
        if self.no_inter == 0:
            if self.music_on:
                self.proc.terminate()
                self.music_on = False
            else:
                self.proc = mp.Process(target = self.main)
                self.proc.start()
                self.music_on = True
        
    # Fonction pour le bouton mute du board
    def switch_board(self):
        if self.no_inter == 1:
            if self.music_on:
                self.proc.terminate()
                self.music_on = False
            else:
                self.proc = mp.Process(target = self.board)
                self.proc.start()
                self.music_on = True
    
    # Changement de menu
    def swap_interface(self):
        # main to board
        if self.no_inter == 0:
            self.no_inter = 1
            if self.music_on:
                self.proc.terminate()
                self.proc = mp.Process(target = self.board)
                self.proc.start()
        # board to main
        else:
            self.no_inter = 0
            if self.music_on:
                self.proc.terminate()
                self.proc = mp.Process(target = self.main)
                self.proc.start()

    def main(self):
        while True:
            playsound(self.path_main)

    def board(self):
        while True:
            playsound(self.path_board)


music_player = Musik()
