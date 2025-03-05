from Objects import Objects
from copy import copy, deepcopy
class Gracz(Objects):
    def __init__(self, x, y, szerokość, wysokość, obraz, prędkość):
        super().__init__(x, y, szerokość, wysokość, obraz)
        self.prędkość = prędkość

    def __copy__(self):
        raise TypeError("Shallow copy is not allowed for this object")

    def __deepcopy__(self, memo):
        raise TypeError("Deep copy is not allowed for this object")

