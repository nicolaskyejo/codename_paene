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
def room_list_returner:
	#This will return the room list in order to know how many rooms are available to enter



# # # [MAIN PROGRAM] # # #










db.rollback()
