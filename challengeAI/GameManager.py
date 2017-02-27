#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This module contains the GameManager class which is the class that controls
 the different stages of the game"""

import random
import copy as cp
from HitGrid import HitGrid
from Boat import Boat


class GameManager(object):
    """ The main class that controls almost everything about the game
     With it, you can shoot, place your boats, tell if the game is finished
     Basically implements the game without the turn based logic"""

    def __init__(self):
        """ Generating the grids"""
        self._hit_grid = [HitGrid(), HitGrid()]
        self._boat_array = [[None, None, None, None, None],
                            [None, None, None, None, None]]

    def get_hit_grid(self, player_id):
        """ Returns the hit grid according to the player_id"""
        temp = cp.deepcopy(self._hit_grid[player_id])
        return temp.get_grid()

    def is_game_finished(self):
        """ Verifies if the game is finished
         if one of the array is empty, function is gonna return True"""
        first_player_dead = True
        second_player_dead = True
        for i in range(0, 5):
            first_player_dead = (first_player_dead and
                                 self._boat_array[0][i].is_wreck())
            second_player_dead = (second_player_dead and
                                  self._boat_array[1][i].is_wreck())

        return first_player_dead or second_player_dead

    def place_boats(self, player_id):
        """ Places all the boats in the array indicated by player_id"""
        new_boat_placed = True
        boat_sizes_array = [5, 4, 3, 3, 2]
        boat_count = 0

        while boat_count < 5:
            orientation = random.randint(0, 1)
            if orientation:
                y_pos = random.randint(0, 9)
                x_pos = random.randint(0, 9 - boat_sizes_array[boat_count])
                orientation_c = 'h'
            else:
                y_pos = random.randint(0, 9 - boat_sizes_array[boat_count])
                x_pos = random.randint(0, 9)
                orientation_c = 'v'

            boat_descriptor = {'y_pos': y_pos, 'x_pos': x_pos,
                               'size': boat_sizes_array[boat_count],
                               'orientation': orientation_c}
            new_boat_placed = self.place_single_boat(
                self._boat_array[(player_id + 1) % 2],
                boat_descriptor, boat_count)
            if new_boat_placed:
                boat_count += 1

    @classmethod
    def place_single_boat(cls, b_array, boat_descriptor, count):
        """ Tries to place a boat on the map, returns true if placed,
        false if not"""
        is_wrong_spot = False
        i = 0
        while not b_array[i] is None:
            is_wrong_spot = (is_wrong_spot or
                             b_array[i].is_colliding(
                                 boat_descriptor['y_pos'],
                                 boat_descriptor['x_pos'],
                                 boat_descriptor['size'],
                                 boat_descriptor['orientation']))
            i += 1
        if not is_wrong_spot:
            b_array[count] = Boat(boat_descriptor['y_pos'],
                                  boat_descriptor['x_pos'],
                                  boat_descriptor['size'],
                                  boat_descriptor['orientation'])
            return True
        else:
            return False

    def shoot(self, player_id, y_pos, x_pos):
        """ Shoots at the other player according to the player_id
         You must give your own player_id
         Coodinates are given as y then x"""
        if y_pos > 9 or y_pos < 0 or x_pos > 9 or x_pos < 0:
            return False
        is_sank = False
        # shoots as the first player
        for i in range(len(self._boat_array[(player_id + 1) % 2])):
            if self._boat_array[(player_id + 1) % 2][i].is_new_hit(y_pos,
                                                                   x_pos):
                self._boat_array[(player_id + 1) % 2][i].get_hit(y_pos, x_pos)
                is_sank = self._boat_array[(player_id + 1) % 2][i].is_wreck()
                self._hit_grid[player_id].mark_hit(y_pos, x_pos)
                if is_sank:
                    print "Touché Coulé! "
        return is_sank

    def print_winner(self):
        """ Prints the game winner"""
        first_player_dead = True
        second_player_dead = True
        for i in range(5):
            first_player_dead = (first_player_dead and
                                 self._boat_array[0][i].is_wreck())
            second_player_dead = (second_player_dead and
                                  self._boat_array[1][i].is_wreck())

        if first_player_dead and not second_player_dead:
            print "Joueur2 a gagné!"
        elif second_player_dead and not first_player_dead:
            print "Joueur1 a gagné!"
        else:
            print "Partie nulle!"

    def print_grids(self):
        """ Prints the grids"""
        print "Joueur1 a touché : "
        self._hit_grid[0].print_self()
        print "Joueur2 a touché : "
        self._hit_grid[1].print_self()
