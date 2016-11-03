#2D sidescroll game where graphics are graphics.
#Player can jump, move forward and backward.
#Print objects using characters.
#Player object size 1 character.
#Map objects around 4 character size per pixel

#from player import Player
#from map import Map

class Dgame:
    def __init__(self, title):
        self.title = title

    def set_title(self, newtitle):
        self.title = newtitle

    def get_title(self):
        return self.title
        
newgame = Dgame("titteli")
