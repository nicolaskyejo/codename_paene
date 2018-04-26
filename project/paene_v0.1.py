#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 
#  
#  Copyright 2018 Oliver, Nicolas & Lauri
#
##### PREAMBLE #####  
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="dbuser",
    passwd="dbpass",
    db="theverge",
    buffered=True)


# # #  [FUNCTIONS] # # #

"""Returns list of rooms you can enter from room_number"""

def room_list_returner(room_number: int, database=db):
    try:
        cursor = database.cursor()
        query = ("SELECT * FROM room_list WHERE Room_id = " + str(room_number))

        cursor.execute(query)

        rooms = []
        for row in cursor.fetchall():
            rooms.append(row[1])

        return rooms

    except mysql.connector.Error as e:
        print(e)

    finally:
        cursor.close()

"""Gets a rooms Door description, used in show_room to get both numbered and named rooms together. """

def room_description(room: int, database=db):

    try:
        cursor = database.cursor()
        query = "SELECT Door_description FROM Room WHERE Room_id = " + str(room)

        cursor.execute(query)
        description = cursor.fetchone()

    except mysql.connector.Error as e:
        print(e)
    return description[0]


""" Shows the text of the room the player is in, and the rooms that can be entered from there."""

def show_room(current_room: int, database=db):
    try:
        showable_text = ""
        available_rooms = room_list_returner(current_room)
        cursor = database.cursor()
        query = "SELECT ActualText FROM Texti WHERE Room_id=" + str(current_room)
        cursor.execute(query)

        for text in cursor.fetchone():
            showable_text = showable_text + text

        showable_text += "\nI can enter rooms: "
        for room_num in available_rooms:
            door_description = room_description(room_num)

            if door_description == None:
                showable_text += str(room_num) + ", "

            else:
                showable_text += str(door_description) + ", "

    except mysql.connector.Error as e:
        print(e)

    finally:
        cursor.close()

    return showable_text




# # # [MAIN PROGRAM] # # #

	
#print(room_list_returner(100))

print(show_room(100))

db.rollback()
