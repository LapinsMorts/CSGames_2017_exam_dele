#!/usr/bin/python3
import numpy as np
from Boat.py import Boat

class BoatGrid:

#La boat grid contient les bateaux d'un joueur.
#L'eau est representee dans la grid par un 0
#Les bateaux sont representes par une serie de 1 ou de 2
#Un 1 represente un bateau non touche par l'adversaire
#Un 2 represente un bateau touche par l'adversaire

    SIZE = 10
    WATER = 0
    BOAT = 1
    HIT = 2


    def __init__(self):
        self.main_grid = np.zeros(SIZE,SIZE)
        boat_generator
        boat_list = 

#boat_direction can only be v (vertival) or h (horizontal)
    def place_boat(self, boat):
        if boat.direction() == 'h': #horizontal (x)
            if boat.size() + boat.x() <= SIZE:
                for i in range(boat.x():boat.x()+boat.size()):
                    if self.main_grid[boat.y(),i]
                        return False
                self.main_grid[,boat.x():boat.x()+boat.size()] = BOAT#place le boat dans la grid

        if boat.direction() == 'v': #vertical (y)
            if boat.size() + boat.y() <= SIZE:
                for i in range(boat.y(),boat.y()+boat.size())
                    if self.main_grid[i,boat.x()]
                        return False
                self.main_grid[boat.y():boat.y()+boat.size(),] = BOAT
        return True

    def is_new_hit(self, y, x):
        if self.main_grid[y,x]:
            result = True and not (main_grid[y,x] == 2)
            self.main_grid[y,x] = HIT
            return result
        else:
            return False

    def contains_wreck(self):

    def clean_wreck(self):

    def is_empty(self):
        for i in range(0,9):
            for j in range(0,9):
                if self.main_grid[i,j]:
                    return False;
        return True;

