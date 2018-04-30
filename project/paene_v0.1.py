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
    #p.stop()
    cutscene_1()
    current_room = 101
    our_print(show_room(current_room))

    while True:
        players_input = get_user_input(str(input()))

        if players_input[0] in ["go", "enter", "e"]:
            if players_input[-1] in ["vent", "duct"] and current_room == 101 and door_open(102) == True:
                our_print("I climb to the air duct and begin crawling. After a while I end up in a new room.")
                current_room = 102
                our_print(show_room(current_room))

            elif players_input[-1] in room_list_returner(current_room):
                current_room = go(current_room, players_input[-1])
            else:
                our_print("I can't go there...")

        elif players_input[0] in ["use"]:
            if players_input[-1] in ["scalpel"]:
                use_item_scalpel()

        elif players_input[0] in ["search"]:
            search(players_input[-1], current_room)

        elif players_input[0] in ["examine", "x"]:
            item_id = item_id_from_name(players_input[-1])
            our_print(examine(item_id))

        elif players_input[0] in ["pull"]:
            pull_box(players_input[-1], current_room)

        elif players_input[0] in ["quit", "q"]:
            quit()
        elif players_input[0] in ["take", "pick"]:
            take_item_id = item_id_from_name(players_input[-1])
            our_print("I pick up " + players_input[-1])
            take(take_item_id)
        elif players_input[0] in ["inventory", "i"]:
            our_print(inventory())
        elif players_input[0] in ["look"]:
            our_print(look(current_room))
    


db.rollback()
