import os

class Utils:

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')