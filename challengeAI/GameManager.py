#/usr/bin/python3
# -*- coding: utf-8 -*-

from HitGrid import HitGrid
from Boat import Boat
import numpy as np
import random
import copy as cp

class GameManager:

    def __init__(self):
        #Generating the grids
        self.first_hit_grid = HitGrid()
        self.second_hit_grid = HitGrid()
        self.first_boat_array = [None,None,None,None,None]
        self.second_boat_array = [None,None,None,None,None]
        #self.first_boat_array = np.empty(5, dtype=object)
        #self.second_boat_array = np.empty(5, dtype=object)

    def get_hit_grid(self, player_id):
        if player_id == 1:
            temp = cp.deepcopy(self.first_hit_grid)
        else:
            temp = cp.deepcopy(self.second_hit_grid)
        return temp.get_grid()

    def is_game_finished(self):#if one of the array is empty, function is gonna return True
        first_player_dead = True
        second_player_dead = True
        for i in range(0,5):
            first_player_dead = first_player_dead and self.first_boat_array[i].is_wreck()
            second_player_dead = second_player_dead and self.second_boat_array[i].is_wreck()

        return first_player_dead or second_player_dead

#places all the boats in the array indicated by id
    def place_boats(self, player_id):
        new_boat_placed = True
        boat_sizes_array = [5,4,3,3,2]
        boat_count = 0
        if player_id == 1:
            while boat_count < 5:
                orientation = random.randint(0,1)
                if orientation:
                    y_pos = random.randint(0,9)
                    x_pos = random.randint(0,9 - boat_sizes_array[boat_count])
                    orientation_c = 'h'
                else:
                    y_pos = random.randint(0,9 - boat_sizes_array[boat_count])
                    x_pos = random.randint(0,9)
                    orientation_c = 'v'
                new_boat_placed = self.place_single_boat(self.first_boat_array, y_pos, x_pos, boat_sizes_array[boat_count], orientation_c, boat_count)
                if new_boat_placed:
                    boat_count = boat_count + 1
        else:
            while boat_count < 5:
                orientation = random.randint(0,1)
                if orientation:
                    y_pos = random.randint(0,9)
                    x_pos = random.randint(0,9 - boat_sizes_array[boat_count])
                    orientation_c = 'h'
                else:
                    y_pos = random.randint(0,9 - boat_sizes_array[boat_count])
                    x_pos = random.randint(0,9)
                    orientation_c = 'v'
                new_boat_placed = self.place_single_boat(self.second_boat_array, y_pos, x_pos, boat_sizes_array[boat_count], orientation_c, boat_count)
                if new_boat_placed:
                    boat_count = boat_count +1

#tries to place a boat, returns true if placed, false if not
    def place_single_boat(self, b_array, y, x, size, orientation, count):
        is_wrong_spot = False
        #for i in range(0, len(b_array)):
        i = 0
        while not(b_array[i] is None):
            is_wrong_spot = is_wrong_spot or b_array[i].is_colliding(y,x, size, orientation)
            i = i +1
        if not is_wrong_spot:
            b = Boat(y, x, size, orientation)
            #b_array = np.append(b_array, b)
            b_array[count] = b
            return True
        else:
            return False


    #Les arguments sont passes y puis x parce que c'est comme ca au battleship
    #La fonction tir et verifie si un bateau de l'autre joueur a ete touche
    def shoot(self, player_id, y, x):
        if y > 9 or y < 0 or x > 9 or x < 0:
            return False
        is_sank = False
        if player_id == 1 :#shoots as the first player
            is_a_hit = False
            for i in range(0,len(self.second_boat_array)):
                #is_a_hit = is_a_hit or self.second_boat_array[i].is_new_hit(y,x)
                is_a_hit = self.second_boat_array[i].is_new_hit(y,x)
                if is_a_hit:
                    self.second_boat_array[i].get_hit(y,x)
                    is_sank = self.second_boat_array[i].is_wreck()
                    self.first_hit_grid.mark_hit(y,x)
                    is_a_hit = False
                    if is_sank:
                        print("Touché Coulé! ")
        else:#shoots as the second player
            is_a_hit = False
            for i in range(0,len(self.first_boat_array)):
                #is_a_hit = is_a_hit or self.first_boat_array[i].is_new_hit(y,x)
                is_a_hit = self.first_boat_array[i].is_new_hit(y,x)
                if is_a_hit:
                    self.first_boat_array[i].get_hit(y,x)
                    is_sank = self.first_boat_array[i].is_wreck()
                    self.second_hit_grid.mark_hit(y,x)
                    is_a_hit = False
                    if is_sank:
                        print("Touché Coulé!")
        return is_sank

    def print_winner(self):
        first_player_dead = True
        second_player_dead = True
        for i in range(0,5):
            first_player_dead = first_player_dead and self.first_boat_array[i].is_wreck()
            second_player_dead = second_player_dead and self.second_boat_array[i].is_wreck()

        if first_player_dead and not second_player_dead:
            print("Joueur2 a gagné!")
        else:
            if second_player_dead and not first_player_dead:
                print("Joueur1 a gagné!")
            else:
                print("Partie nulle!")

    def print_grids(self):
        print("Joueur1 a touché : ")
        self.first_hit_grid.print_self()
        print("Joueur2 a touché : ")
        self.second_hit_grid.print_self()
