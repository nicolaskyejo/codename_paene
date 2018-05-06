import mysql.connector
from gamefuncs import *
from cutscenes import *
from config import db

#QUERY FUNCTIONS
def room_list_returner(room_number, database=db):
    try:
        cursor = database.cursor()
        query = ("SELECT * FROM room_list WHERE Room_id = " + str(room_number))

        cursor.execute(query)

        rooms = []
        for row in cursor.fetchall():
            rooms.append(str(row[1]))

        return rooms

    except mysql.connector.Error as e:
        print(e)

    finally:
        cursor.close()


"""Gets a rooms Door description, used in show_room to get both numbered and named rooms together. """


def room_description(room, database=db):
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

    
def item_pick(id, database=db):
    result = False
    try:
        cursor = database.cursor()
        # Picks only items that are not hidden and are pickable #
        query1 = "UPDATE Item SET Inventory = TRUE, HIDDEN = TRUE WHERE Item_id = " + str(id) + " AND Pickable = TRUE AND Hidden = FALSE"
        query2 = "SELECT Inventory FROM Item WHERE Item_id = " + str(id)
        cursor.execute(query1)
        cursor.execute(query2)

        fetch = cursor.fetchone()
        if fetch[0] == 1:
            result = True
        else:
            result = False   
        
             
    except mysql.connector.Error as e:
        print(e)

    finally:
        cursor.close()
        return result
            
 
def get_items_of_room(room_id, database=db):
    try:
        query = "SELECT Name FROM Item WHERE Room_id = " + str(room_id) + " AND Hidden = FALSE"
        cursor = database.cursor()
        cursor.execute(query)

        item_names=[]
        for name in cursor.fetchall():
            item_names.append(name[0].lower())

    except mysql.connector.Error as e:
        print(e)

    finally:
        cursor.close()
        return item_names

def get_all_items_of_room(room_id, database=db):
    try:
        query = "SELECT Name FROM Item WHERE Room_id = " + str(room_id)
        cursor = database.cursor()
        cursor.execute(query)

        item_names=[]
        for name in cursor.fetchall():
            item_names.append(name[0])

    except mysql.connector.Error as e:
        print(e)

    finally:
        cursor.close()
        return item_names

def get_id_items_of_room(room_id, database=db):
    try:
        query = "SELECT item_id FROM Item WHERE Room_id = " + str(room_id)
        cursor = database.cursor()
        cursor.execute(query)

        item_names=[]
        for name in cursor.fetchall():
            item_names.append(name[0])

    except mysql.connector.Error as e:
        print(e)

    finally:
        cursor.close()
        return item_names
     
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

def get_items_inventory(database=db):
    try:
        query = "SELECT Item_id FROM Item WHERE Inventory = TRUE"
        cursor = database.cursor()
        cursor.execute(query)

        inventory=[]
        for item in cursor.fetchall():
            inventory.append(item[0])


    except mysql.connector.Error as e:
        print(e)

    finally:
        cursor.close()
        return inventory

def if_item_used(id, database=db):
    result = False
    try:
        query = "SELECT Used FROM Item WHERE item_id =" + str(id) + " AND Used = True"
        cursor = database.cursor()
        cursor.execute(query)

        if cursor.rowcount == 1:
            result = True
        else:
            result = False

    except mysql.connector.Error as e:
        print(e)

    finally:
        cursor.close()
        return result

def item_id_from_name(name, database=db):
    try:
        query='SELECT item_id FROM Item WHERE name = "'+ str(name) + '"'
        cursor = database.cursor()
        cursor.execute(query)

        id = cursor.fetchone()
    except mysql.connector.Error as e:
        print(e)

    finally:
        cursor.close()
        if id != None:
            return id[0]
        else:
            return None

def item_name_from_id(item_id, database=db):
    try:
        query='SELECT name FROM Item WHERE item_id =' + str(item_id)
        cursor = database.cursor()
        cursor.execute(query)

        id = cursor.fetchone()

    except mysql.connector.Error as e:
        print(e)

    finally:
        cursor.close()
        if id != None:
            return id[0]
        else:
            return None

def use_item(item_id, current_room,database=db): #Changes Used to True if item not hidden, in the same room, item id matches
    try:
        query = "UPDATE Item SET Used = TRUE WHERE Used = FALSE AND room_id = {0} AND Hidden = FALSE AND item_id = {1};".format(
            str(current_room), str(item_id))
        cursor = database.cursor()
        cursor.execute(query)

    except mysql.connector.Error as e:
        print(e)

    finally:
        cursor.close()


def drop_item(item_id, room_id, database=db):
    try:
        query1 = "UPDATE Item SET Inventory = FALSE, Hidden = FALSE  WHERE Item_id = " + str(item_id) 
        query2 = "UPDATE Item SET room_id = " + str(room_id) + " WHERE Item_Id = " + str(item_id)
        cursor = database.cursor()
        cursor.execute(query1)
        cursor.execute(query2)

    except mysql.connector.Error as e:
        print(e)

    finally:    
        cursor.close() 

# checks if door is locked from dbase #
def door_open(room_id, database=db):
    result = True
    try:
        query = "SELECT Locked FROM Room WHERE room_id =" + str(room_id)
        cursor = database.cursor()
        cursor.execute(query)

        open_or_not = cursor.fetchone()
        if open_or_not[0] == 1:
            result = False
        else:
            return True

    except mysql.connector.Error as e:
        print(e)

    finally:
        cursor.close()
        return result
        
# Returns boolean whether an enemy in that room is dead or not #  checks only 1 enemy #    
def npc_alive_or_not(room_id, database=db):
    result = False
    try:
        query = "SELECT Npc_Id FROM Npc WHERE room_id =" + str(room_id)
        cursor = database.cursor()
        cursor.execute(query)

        if cursor.rowcount >= 1:
            result = True
        else:
            result = False

    except mysql.connector.Error as e:
        print(e)

    finally:
        cursor.close()
        return result      
        
#checks the various ending parameters and calls an ending        
def ending_checker(ending_choice, database=db):           
    query1 = "SELECT Inventory FROM ITEM WHERE Name = 'Lighter'"
    query2 = "SELECT Inventory FROM ITEM WHERE Name = 'Gasoline tank'"
    cursor = database.cursor()
    item1 = cursor.execute(query1)
    item2 = cursor.execute(query2)
    
    if item1 == 1 and item2 == 1:
        while True:
            answer = input('Should I light this building on fire?')
            if answer == 'Yes' or 'yes' or 'Y' or 'y' or 'YES':
                ending_3()
                the_end()
                sys.exit()
                
            else:
                break
    else:             #True = forgive, False = Kill   
        if ending_choice == True:   
            ending_2()
            the_end()
            sys.exit()
        
        else:
            ending_1() 
            the_end()   
            sys.exit()
            
#check secret ending if the player has pipe    
def secretending_checker(database=db): 
    query = "SELECT Inventory FROM ITEM WHERE Name = 'Metal pipe'"  
    cursor = database.cursor()
    cursor.execute(query) 
    
    if cursor.rowcount == 1:
        ending_4()
        the_end()
        sys.exit()
    else:
        pass

def npc_name_from_room(current_room, database=db):
    fetch=[""]
    try:
        query = "SELECT Name FROM Npc WHERE Room_id = " + str(current_room)

        cursor = database.cursor()
        cursor.execute(query)
        fetch = cursor.fetchone()

    except mysql.connector.Error as e:
        print(e)

    finally:
        return fetch[0]
