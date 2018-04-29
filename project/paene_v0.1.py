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
            if players_input[-1] in room_list_returner(current_room):
                current_room = go(current_room, players_input[-1])
            else:
                our_print("I can't go there...")

        elif players_input[0] in ["use"]:
            if players_input[-1] in ["scalpel"]:
                use_item_scalpel()

        elif players_input[0] in ["examine", "x"]:
            item_id = item_id_from_name(players_input[-1])
            our_print(examine(item_id))

        elif players_input[0] in ["pull"]:
            pull_box(players_input[-1], current_room)

        elif players_input[0] in ["quit", "q"]:
            quit()
        elif players_input[0] in ["take", "pick"]:
            take(players_input[-1])
        elif players_input[0] in ["inventory", "i"]:
            our_print(inventory())
        elif players_input[0] in ["look"]:
            our_print(look(current_room))
    


db.rollback()
