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
from config import db

# # # [MAIN PROGRAM] # # #
if __name__ == '__main__':
    
    cutscene_1()
    current_room = 101    #Position in game, indicated by current_room
    our_print(show_room(current_room))
    while True: #Actual process of the game, loops until quit
        two_words_input=""
        players_input = get_user_input(str(input(":> ")))   #list of inputs. [0] is the command, [-1] is the object.
        if len(players_input) > 2:
            two_words_input = players_input[-2] + " " + players_input[-1]
            
        if players_input[0] in ["quit", "q"]:
            quit()
        
        elif players_input[0] in ["help"]:
            help()
            
        elif players_input[0] in ["license"]:
            license()  
        
        elif players_input[0] in ["credits"]:
            credits()
               
        elif players_input[0] in ["inventory", "i"]:
            our_print(inventory())

        elif players_input[0] in ["look"]:
            our_print(show_room(current_room))
            our_print(look(current_room))

        elif players_input[0] in ["up","u"]:
            ret = up(current_room)
            if ret != None:
                current_room = ret

        elif players_input[0] in ["down","d"]:
            ret = down(current_room)
            if ret != None:
                current_room = ret

        elif players_input[0] in ["clear","c"]:
            clear()   
            
        elif players_input[0] in ["leave","exit"]:
            ret = leave(current_room)
            if ret != None:
                current_room = ret
                      
        elif players_input[0] in ["kill"]:     
            kill(players_input[-1])
        

        elif players_input[0] in ["go", "enter", "e"]:
            result = door_open(666)
            
            if door_open(666) == True:
                ending_checker(ending_choice)    
            
            elif players_input[-1] in ["vent", "duct"] and current_room == 101 and door_open(102) == True: #Vent problem, can pass if these things are correct
                our_print("I climb to the air duct and begin crawling. After a while I end up in a new room.\n")
                current_room = 102
                os.system('Blindspot.mp3')
                our_print(show_room(current_room))
                         
     
            elif players_input[-1] in room_list_returner(current_room) and door_open(players_input[-1]) == True:
                current_room = go(current_room, players_input[-1])
                ending_choice = fight_checker(current_room)
            
            else:
                our_print("I can't go there...")

        elif players_input[0] in ["use"]:
            if item_id_from_name(players_input[-1]) in get_items_inventory():
                use(players_input[-1], current_room)

            elif item_id_from_name(two_words_input) in get_items_inventory():
                use(two_words_input, current_room)

            else:
                our_print("I can't do that.")

        elif players_input[0] in ["search"]:
            if item_id_from_name(players_input[-1]) in get_id_items_of_room(current_room):
                search(players_input[-1], current_room)

            elif item_id_from_name(two_words_input) in get_id_items_of_room(current_room):
                search(two_words_input, current_room)
            else:
                our_print("There is nothing to search from...")
                
        elif players_input[0] in ["examine", "x"]:
            if item_id_from_name(players_input[-1]) in get_id_items_of_room(current_room):
                item_id = item_id_from_name(players_input[-1])
                our_print(examine(item_id))

            elif item_id_from_name(two_words_input) in get_id_items_of_room(current_room):
                item_id = item_id_from_name(two_words_input)
                our_print(examine(item_id))

            else:
                our_print("I don't see anything important.")

        elif players_input[0] in ["push"]:
            push_box(players_input[-1], current_room)

        
        elif players_input[0] in ["take", "pick"]:
            if item_id_from_name(players_input[-1]) in get_id_items_of_room(current_room):
                take_item_id = item_id_from_name(players_input[-1])
                take(take_item_id,players_input[-1],current_room)

            elif item_id_from_name(two_words_input) in get_id_items_of_room(current_room):
                take_item_id = item_id_from_name(two_words_input)
                take(take_item_id,two_words_input,current_room)

        elif players_input[0] in ["drop"]:
            if item_id_from_name(players_input[-1]) in get_items_inventory():
                drop(players_input[-1], current_room)

            elif item_id_from_name(two_words_input) in get_items_inventory():
                drop(two_words_input, current_room)

            else:
                our_print("I don't have that.")
        elif players_input[0] in ["talk"]:
            if npc_alive_or_not(current_room):
                name_of_npc = npc_name_from_room(current_room)
                talk(name_of_npc)
            else:
                our_print("There is no one to talk to...")
       
        else:
            our_print("Not a valid command. Type HELP for help.\n")
            
db.rollback()
