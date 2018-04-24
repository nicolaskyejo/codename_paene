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


# # # [MAIN PROGRAM] # # #

print(room_list_returner(100))

db.rollback()
