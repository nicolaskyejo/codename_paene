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

"""Vesa's print function for formating printed text"""

def our_print(textline):
    line_length = 80
    list_of_words = textline.split()
    used = 0

    for word in list_of_words:
        if used + len(word) <= line_length:
            if used > 0:
                print(" ", end="")
            print(word, end="")

        else:
            print("")
            used = 0
            print(word, end="")
        used = used + len(word)
    print("")


"""splits the users input into words, puts them in a list. gets rid of weird characters"""

def get_user_input(input: str):
    words = input.lower().split()
    list_of_commands=[]

    for word in words:
       string=""
       for c in word:
           if c.isalnum():
               string += c
       list_of_commands.append(string)

    return list_of_commands

########### Game commands Functions  ##########  
def help():
    list_of_commands = ["Credits. Lists the game credits.","Quit. Quits the game.","Clear (c). Clears console","Directional ↑. Repeats the last command.","Enter(E)/Go {room number}. Enter room.","Up(U)/Down(D). Go up or down the stairs.", "Exit/Leave. Leaves current room.",
                        "Inventory (I). List items that you hold.","Examine (X) {object}. Describes object.","Take {object}. Puts object into your inventory",
                        "Kick {object}.","Use {item}. Uses item found in your inventory.","Push {object}. Pushes object, useful for a short puzzle.",
                        "Look. Looks around your environment and reports what you see.","Search {object}. Probes object to more."]
    print("The game commands are listed in the form Command (shortform) {options}")

    for commands in list_of_commands:
        print(commands)

def commands():
    allcommands = ["credits","quit","clear","c","enter","e","up","u","down","d",
                   "leave","exit", "inventory", "i", "examine",
                   "x", "take", "kick", "use", "push", "look","go", "search"]
    return allcommands

def credits():
    print("This game was a project in our gaming course. It is released under MIT license. Copyright 2018 Oliver Andersson, Nicolas Kyejo and Lauri Outila.")

def license():
    print("\t\tMIT License\n\n", \

    "Copyright (c) 2018 Oliver, Lauri and Nicolas\n\n", \

    "Permission is hereby granted, free of charge, to any person obtaining a copy\n", \
    "of this software and associated documentation files (the \"Software\"), to deal\n", \
    "in the Software without restriction, including without limitation the rights\n", \
    "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n", \
    "copies of the Software, and to permit persons to whom the Software is\n", \
    "furnished to do so, subject to the following conditions:\n\n", \

    "The above copyright notice and this permission notice shall be included in all\n", \
    "copies or substantial portions of the Software.\n\n", \

    "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n", \
    "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n", \
    "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE,\n" \
    "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER,\n" \
    "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n", \
    "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n", \
    "SOFTWARE.\n", sep = '')

def clear():		#Clear console
    print("\n"*100)

def go(current_room: str, room_to_move: str):
    current_room = int(current_room)
    room_to_move = int(room_to_move)

    if room_to_move in room_list_returner(current_room):
        print("You entered room number " + str(room_to_move))
        return room_to_move
    else:
        print("You can't go there.")
        return current_room

#################### GAME COMMANDS END HERE ####################  
def cutscene_1():
    print("(Have to find something to numb the pain...)\n\n"\

    "Unknown man: (inaudible) There is no way out of (inaudible)\n" \

    "\tJust accept your fate.\n\n"\

    "Verner: Wha... ?\n\n"\

    "Unknown man: Someone will come soon to deliver you. Ne metue.\n\n"\
    
    "The Verge© 2018\n"\
    "First time players should type HELP. Credits are available via CREDITS and license via LICENSE.\n")    
    
def cutscene_2():
    print("Guard: Uuuuuurgghhhhh!")

    print("Guard falls down dead\n")

    print("Doctor: Please don’t kill me!!! I am useful alive!\n")
    
def cutscene_3():   
    print("Dr. Buchwald: mmh it seems I underestimated you… I should have put more guards in place but oh well… You are here for revenge aren’t you?\n")

    print("Verner: …\n")

    print("Buchwald: Before you make any rash decision, hear me out first.")    
    
# # # [MAIN PROGRAM] # # #
clear()
if __name__ == '__main__':

    print(show_room(101))
    current_room = 101
    while True:
        players_input = get_user_input(str(input()))
        if players_input[0] in commands():

            current_room = go(current_room, players_input[1])
            print(show_room(current_room))
        else:
            print("huh wat u say man")


#print(room_list_returner(100))
#print(show_room(100))
#help()
#credits()
#license()
#cutscene_1()
#cutscene_2()
#cutscene_3()

db.rollback()
