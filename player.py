import playsound
from banner import PLAYER
class player:
    def __init__(self):
        print(PLAYER)
        self.link = input('\nPlease Enter The Link :')
    def play_sound(self):
        playsound.playsound(self.link)

music = player()
music.play_sound()
