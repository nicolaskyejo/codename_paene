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
from cutscenes import *

# # # [MAIN PROGRAM] # # #
if __name__ == '__main__':
    cutscene_1()
    current_room = 101
    our_print(show_room(current_room))

    while True:
        players_input = get_user_input(str(input()))

        if players_input[0] in ["go", "enter", "e"]:
            current_room = go(current_room, players_input[-1])

        elif players_input[0] in ["examine", "x"]:
            examine()
        elif players_input[0] in ["quit", "q"]:
            quit()
        elif players_input[0] in ["take", "pick"]:
            take()
        elif players_input[0] in ["inventory", "i"]:
            inventory()
        elif players_input[0] in ["look"]:
            look()
    


db.rollback()
