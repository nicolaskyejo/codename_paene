#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 
#  
#  Copyright 2018 Oliver, Nicolas & Lauri
#
##### PREAMBLE #####  
from gamefuncs import *
from queryfuncs import *

# # # [MAIN PROGRAM] # # #
if __name__ == '__main__':

    print(show_room(101))
    current_room = 101
    while True:
        players_input = get_user_input(str(input()))
        if players_input[0] in commands():

            current_room = go(current_room, players_input[1])
            print(show_room(current_room))
        else:
            print("huh wat u say man")

#print(room_list_returner(100))
#print(show_room(100))
#help()
#credits()
#license()
#cutscene_1()
#cutscene_2()
#cutscene_3()

db.rollback()
