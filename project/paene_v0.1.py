#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 
#  
#  Copyright 2018 Oliver, Nicolas & Lauri
#  
import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        user="dbuser",
        passwd="dbpass",
        db="theverge",
        buffered=True)


# # #  [FUNCTIONS] # # #
def room_list_returner():
        a = 222222
        return a

	#This will return the room list in order to know how many rooms are available to enter



# # # [MAIN PROGRAM] # # #

lauri = 2
was = 5
here = 1337

def ask(item_name, npc_id):
    if item_name == npc.item_name:
        return info_from_npc










db.rollback()
