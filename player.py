from playsound import playsound
from banner import PLAYER
import multiprocessing
class player:
    def __init__(self):
        print(PLAYER)
        self.link = input('Please Enter The Link :')
        if self.link.lower() == 'x':
            exit()
    def play_sound(self):
        self.music = multiprocessing.Process(target=playsound, args=(self.link,))
        self.music.start()
    def change_music(self):
        input('\nPress Enter For Play Next Music !')
        self.music.terminate()
def run():
    music = player()
    music.play_sound()
    music.change_music()

while True:
    run()
