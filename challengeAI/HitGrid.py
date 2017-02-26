#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np


class HitGrid:

    def __init__(self):
        self.printable_grid = np.chararray((10, 10))
        self.printable_grid[:] = '~'

    def mark_hit(self, y, x):
        self.printable_grid[y, x] = '#'

    def print_self(self):
        print('  0 1 2 3 4 5 6 7 8 9')
        chaine = np.array_str(self.printable_grid)
        # for i in range(0,10):
        #     for j in range(0,10):
        #         print(i)
        #         print(self.printable_grid[i,j])
        #     print('')
        chaine = chaine.replace("'", "")
        chaine = chaine.replace('[', '')
        chaine = chaine.replace(']', '')
        chaine = '0 ' + chaine
        chaine = chaine[:22] + '1' + chaine[22:]
        chaine = chaine[:44] + '2' + chaine[44:]
        chaine = chaine[:66] + '3' + chaine[66:]
        chaine = chaine[:88] + '4' + chaine[88:]
        chaine = chaine[:110] + '5' + chaine[110:]
        chaine = chaine[:132] + '6' + chaine[132:]
        chaine = chaine[:154] + '7' + chaine[154:]
        chaine = chaine[:176] + '8' + chaine[176:]
        chaine = chaine[:198] + '9' + chaine[198:]
        print(chaine)

    def get_grid(self):
        return self.printable_grid
