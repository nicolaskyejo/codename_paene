import mysql.connector
from gamefuncs import *
db = mysql.connector.connect(
    host="localhost",
    user="dbuser",
    passwd="dbpass",
    db="theverge",
    buffered=True)

#QUERY FUNCTIONS
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

        return description[0]
    except mysql.connector.Error as e:
        print(e)


""" Shows the text of the room the player is in, and the rooms that can be entered from there."""


def show_room(current_room: int, database=db):
    try:
        showable_text = "[Room " + str(current_room) + ":" + str(room_description(current_room)) + "]" + "\n"
        available_rooms = room_list_returner(current_room)
        cursor = database.cursor()
        query = "SELECT ActualText FROM Texti WHERE Room_id=" + str(current_room)
        cursor.execute(query)

        for text in cursor.fetchone():
            showable_text = showable_text + text

        showable_text += "\n\nI can enter rooms:\n"
        for room_num in available_rooms:
            door_description = room_description(room_num)

            if door_description == None:
                showable_text += str(room_num) + "\n"

            else:
                showable_text += str(room_num) + ": " + str(door_description) + "\n"

    except mysql.connector.Error as e:
        print(e)

    finally:
        cursor.close()

    return showable_text
    
def item_pick(id: int, database=db):
    try:
        cursor = database.cursor()
        query = "UPDATE Item SET Character_id = 1 WHERE Item_id = " + str(id)
        cursor.execute(query)
        
    except mysql.connector.Error as e:
        print(e)

    finally:
        cursor.close()       
     
def item_description(id: int, database=db):
    try:
        cursor = database.cursor()
        query = "SELECT Description FROM Item WHERE Item_id = " + str(id)

        cursor.execute(query)
        description = cursor.fetchone()
        
    except mysql.connector.Error as e:
        print(e)

    finally:
        cursor.close()
        
    return description[0]       


