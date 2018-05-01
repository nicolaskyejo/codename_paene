#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 
#  
#  Copyright 2018 Oliver, Nicolas & Lauri
#
##### PREAMBLE #####
import os  
from gamefuncs import *
from queryfuncs import *
from cutscenes import *
# # # [MAIN PROGRAM] # # #
if __name__ == '__main__':
    os.system('Blindspot.mp3')
    cutscene_1()
    current_room = 101    #Position in game, indicated by current_room
    our_print(show_room(current_room))

    while True: #Actual process of the game, loops until quit

        players_input = get_user_input(str(input(":>")))   #list of inputs. [0] is the command, [-1] is the object.

        if players_input[0] in ["quit", "q"]:
            quit()
        elif players_input[0] in ["inventory", "i"]:
            our_print(inventory())

        elif players_input[0] in ["look"]:
            our_print(look(current_room))

        elif len(players_input) != 2:
            our_print("Not a valid input. Commands work like this: \n [command] [object]")

        elif players_input[0] in ["go", "enter", "e"]:
            print(type(players_input[-1]))
            print(room_list_returner(current_room))
            print(door_open(players_input[-1]))
            if players_input[-1] in ["vent", "duct"] and current_room == 101 and door_open(102) == True: #Vent problem, can pass if these things are correct
                our_print("I climb to the air duct and begin crawling. After a while I end up in a new room.")
                current_room = 102
                our_print(show_room(current_room))

            elif players_input[-1] in room_list_returner(current_room) and door_open(players_input[-1]) == True:
                current_room = go(current_room, players_input[-1])
            else:
                our_print("I can't go there...")

        elif players_input[0] in ["use"]:
            use(players_input[-1], current_room)

        elif players_input[0] in ["search"]:
            search(players_input[-1], current_room)

        elif players_input[0] in ["examine", "x"]:
            item_id = item_id_from_name(players_input[-1])
            our_print(examine(item_id))

        elif players_input[0] in ["push"]:
            pull_box(players_input[-1], current_room)


        #elif players_input[0] in ["take", "pick"]:
        #    if players_input[-1] in get_items_of_room(current_room):
        #        take(item_id_from_name(players_input[-1]))
        #    else:
        #        our_print("I can't do that.")

        #elif players_input[0] in ["drop"]:
        #    drop(players_input[-1])

 
        elif players_input[0] in ["take", "pick"]:
            take_item_id = item_id_from_name(players_input[-1])
            our_print("I pick up " + players_input[-1])
            take(take_item_id,players_input[-1],current_room)
        
        elif players_input[0] in ["drop"]:
            drop(players_input[-1], current_room)
            
        elif players_input[0] in ["help"]:
            help()
            
        elif players_input[0] in ["license"]:
            license()   
        
        #elif players_input[0] in ["up","u"]:
        #    up(current_room)
            
        #elif players_input[0] in ["down","d"]:
        #    down(current_room)  
          
        else:
            our_print("Not a valid command. Type HELP for help.\n")
db.rollback()
