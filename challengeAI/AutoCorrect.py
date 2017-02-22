#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import time
import numpy as np
import random


def replace_line(file_name, line_number, text):
    f = open(file_name,"r+")
    d = f.readlines()
    f.seek(0)
    j = 0
    for i in d:
        if j == line_number -1 :
            f.write(text + "\n")
        else:
            f.write(i)
        j = j + 1
    f.truncate()
    f.close()


start_time = time.time()

file_array = ['AI', 'AI1', 'AI2', 'AI3', 'AI4', 'AI5', 'AI6', 'AI7', 'AI8', 'AI9']

winner_array = []

GAME = 10
done = False
safe = -1

while not done:
    #pick the two AIs according to a tournament logic
    amount = len(file_array)
    if amount % 2 != 0:
        safe = random.randint(0,amount-1)
        winner_array = np.append(winner_array, file_array[safe])
        file_array = np.delete(file_array, safe)
        amount = amount -1
    ai_counter = 0
    while ai_counter < amount:
        #change the code
        replace_line("Game.py", 5,  "from " + file_array[ai_counter]   + " import " + file_array[ai_counter])
        replace_line("Game.py", 6,  "from " + file_array[ai_counter+1] + " import " + file_array[ai_counter+1])
        replace_line("Game.py", 28, "first_player = " + file_array[ai_counter] + "(game_manager,1)")
        replace_line("Game.py", 32, "second_player = " + file_array[ai_counter+1] + "(game_manager,2)")


        #launch the games
        i = 0
        player_1_win = 0
        player_2_win = 0
        even_game = 0
        continu = True
        while i < GAME and continu:
            game_result = subprocess.check_output("python Game.py", shell=True)
            if game_result == "Joueur2 a gagné!\n":
                player_2_win = player_2_win + 1
            else:
                if game_result == "Joueur1 a gagné!\n":
                    player_1_win = player_1_win + 1
                else:
                    even_game = even_game + 1
            if player_1_win > GAME // 2 or player_2_win > GAME // 2 or even_game > GAME // 2:
                continu = False
            i = i + 1

        #find the winner and put it in the winner_array, if there is none, we do not increment thecounter and the same match is played again until a winner is declared
        if player_1_win > player_2_win:
            winner_array = np.append(winner_array, file_array[ai_counter])
            ai_counter = ai_counter + 2
        else:
            if player_2_win > player_1_win:
                winner_array = np.append(winner_array, file_array[ai_counter + 1])
                ai_counter = ai_counter + 2
        if ai_counter >= amount:
            print(winner_array)
            file_array = winner_array
            winner_array = []

    #check if done : if there is only one AI left
    if len(file_array) == 1:
        done = True





#print(file_array[0])

print("--- %s seconds ---" % (time.time() - start_time))





