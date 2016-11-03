#MapObject

class MapObject:
    def __init__(self, name, pixel):
        self.name = name
        self.pixel = pixel

    def get_name(self):
        return self.name

    def get_pixel(self):
        return self.pixel

#test object
#objekti = MapObject("maa", ["=", "=", "=", "="])
