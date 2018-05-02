import sys
from queryfuncs import *

#GAME FUNCTIONS

"""Vesa's print function for formating printed text"""


def our_print(textline):
    line_length = 70
    list_of_words = textline.split(" ")
    used = 0

    for word in list_of_words:
        if used + len(word) <= line_length:
            if "\n" in word:
                used = 0
                print(" ", end="")
            elif used > 0:
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
    list_of_commands = []

    for word in words:
        string = ""
        for c in word:
            if c.isalnum():
                string += c
        list_of_commands.append(string)

    return list_of_commands


########### Game commands Functions  ##########
def help():
    list_of_commands = ["Credits. Lists the game credits.", "Quit. Quits the game.", "Clear (c). Clears console",
                        "Directional ↑. Repeats the last command.", "Enter(E)/Go {room number}. Enter room.",
                        "Up(U)/Down(D). Go up or down the stairs.", "Exit/Leave. Leaves current room.",
                        "Inventory (I). List items that you hold.", "Examine (X) {object}. Describes object.",
                        "Take {object}. Puts object into your inventory",
                        #"Kick {object}.", "Use {item}. Uses item found in your inventory.",
                        "Push {object}. Pushes object, useful for a short puzzle.",
                        "Look. Looks around your environment and reports what you see.",
                        "Search {object}. Searches object to find if there is something.",
                        "Drop {object}. Leaves object on the ground.\n"]
    print("The game commands are listed in the form Command (shortform) {options}\n")

    for commands in list_of_commands:
        print(commands)




def credits():
    print(
        "This game was a project in our gaming course. It is released under MIT license\n. Copyright 2018 Oliver Andersson, Nicolas Kyejo and Lauri Outila.")


def license():
    print("\t\tMIT License\n\n", \
 \
          "Copyright (c) 2018 Oliver, Lauri and Nicolas\n\n", \
 \
          "Permission is hereby granted, free of charge, to any person obtaining a copy\n", \
          "of this software and associated documentation files (the \"Software\"), to deal\n", \
          "in the Software without restriction, including without limitation the rights\n", \
          "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n", \
          "copies of the Software, and to permit persons to whom the Software is\n", \
          "furnished to do so, subject to the following conditions:\n\n", \
 \
          "The above copyright notice and this permission notice shall be included in all\n", \
          "copies or substantial portions of the Software.\n\n", \
 \
          "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n", \
          "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n", \
          "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE,\n" \
          "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER,\n" \
          "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n", \
          "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n", \
          "SOFTWARE.\n", sep='')


def clear():  # Clear console
    print("\n" * 100)


def go(current_room: str, room_to_move: str):
    current_room = current_room
    room_to_move = room_to_move

    if room_to_move in room_list_returner(current_room):
        our_print(show_room(room_to_move))

        return room_to_move
    else:
        print("You can't go there.")
        return current_room


def commands():
    allcommands = [["enter", "e", "go"],    #done
                   ["examine", "x"],    #done
                   ["leave", "exit"], 
                   ["quit", "q"],   #done
                   ["push"],    #done 
                   ["take","pick"], #done
                   ["inventory", "i"],  #done
                   #["kick"],
                   ["search"], #done
                   ["look"],    #done
                   ["use"], #requires to implement on all objects that can be used
                   ["up", "u"],
                   ["down", "d"],
                   ["credits"], #done
                   ["license"], #done
                   ["help"],    #done
                   ["clear", "c"],#done
                   ["drop"] #done
                  ]  

    return allcommands


def examine(item_id):
    txt = item_description(item_id)

    return txt

def take(item_id, item_name, room_id):
    list_of_items_in_current_room = get_items_of_room(room_id) 

    if item_name in list_of_items_in_current_room:
        value=item_pick(item_id)
        if value == True:
            print("Picked it up.")    
        else:
         print("I cannot take that...\n")
    else:
        print("I cannot take that...\n") 

def quit():
    while True:
        answer = input("Do you really want to quit the game? (Y/N)  ")    
        answer.lower()
        if answer == 'y' or answer == 'yes':
            print("Exiting...")
            sys.exit()
        elif answer == 'n' or answer == 'no':
            print("Returning to game...") 
            break    
        else:
            print("Please Enter Y or N")
            break    
        
def look(room_id):

    txt = "I see these things around me: \n"
    items = get_items_of_room(room_id)
    if items:
        for name in items:
            txt = txt + name + "\n"

    return txt

def inventory():
    txt = "I am carrying these items: \n"
    inventory = get_items_inventory()

    for item in inventory:
        item_name = item_name_from_id(item)
        description = item_description(item)

        txt = txt + item_name + " - " + description + "\n"

    return txt

def use_item_scalpel(database=db):

    items = get_items_inventory()
    scalpel_id = item_id_from_name("scalpel")

    if scalpel_id in items:
        box_id = item_id_from_name("box")
        print(if_item_used(box_id))

        if if_item_used(box_id) == True:
            query1="DELETE FROM Item WHERE Item_id=100"
            query2="UPDATE Item SET Hidden=FALSE WHERE Item_id=101"
            query3="UPDATE Room SET Locked=FALSE WHERE Room_id=102"
            query4="UPDATE Room SET Locked=FALSE WHERE Room_id=100"

            cursor = database.cursor()

            cursor.execute(query1)
            cursor.execute(query2)
            cursor.execute(query3)
            cursor.execute(query4)
            our_print("I get on top of the box, and use the scalpel as a screw driver to open the air vent. "\
                      "I could enter here...")
            cursor.close()
        else:
            our_print("I have nothing to use it on...")
    else:
        our_print("I do not have that item.")

def push_box(item, current_room):
    if item == "box":
        box_id = item_id_from_name("box")
        if current_room == 101 and if_item_used(box_id) == False:
            use_item(box_id, 101)
            our_print("I push the box under the air vent.")

    else:
        our_print("Nothing happens...")


def drop(item, current_room):
    item_id = item_id_from_name(item)
    if item_id in get_items_inventory():
        drop_item(item_id,current_room)
        print ("" + str(item) + " dropped...\n")
    else:
        print("I cannot drop that.\n") 



def search(item, current_room, database=db):
    item_id = item_id_from_name(item)
    items = get_id_items_of_room(current_room)
    item_to_find = item_id+1

    if item_to_find in items:
        query = "UPDATE Item SET Hidden = FALSE AND Pickable = TRUE WHERE Item_id = " + str(item_to_find)
        cursor = database.cursor()
        cursor.execute(query)
        our_print("I found something...")
        cursor.close()

    else:
        our_print("I didn't find anything.")
        
def up(current_room):
    stairs = room_list_returner(current_room)
    if 200 in stairs:
        go(current_room,200)
    elif 300 in stairs:
        go(current_room,300)    
    elif 400 in stairs:
        go(current_room,400)    
    else:
        print("I cannot go up from here...")
    
def down(current_room):
    stairs = room_list_returner(current_room)
    if 400 in stairs:
        go(current_room,300)
    elif 300 in stairs:
        go(current_room,200)    
    elif 200 in stairs:
        go(current_room,100)    
    else:
        print("I cannot go down from here...")          
    
#def leave(current_room):  
#    corridors = [100,110,200,210,300,310,400,410]
#    rooms = room_list_returner(current_room)
#    if current_room not in corridors:
#            go(current_room,)

def use(item_name, room_id, database=db):
    inventory = get_items_inventory()

    if item_name == "painkillers":
        item_id = item_id_from_name(item_name)

        if item_id in inventory:
            if if_item_used(item_id) == False:
                our_print("I swallowed the painkillers. I'm starting to feel a bit better...")
                query1 = "UPDATE Item SET Used = TRUE WHERE item_id = " + str(item_id)
                query2 = "UPDATE Item SET Hidden = TRUE WHERE item_id = " + str(item_id)

                cursor = database.cursor()

                cursor.execute(query1)
                cursor.execute(query2)
                cursor.close()

    elif item_name == "scalpel":
        item_id = item_id_from_name(item_name)

        if item_id in inventory:
            box_id = item_id_from_name("box")

            if if_item_used(box_id) == True:
                query1="DELETE FROM Item WHERE Item_id=100"
                query2="UPDATE Item SET Hidden=FALSE WHERE Item_id=101"
                query3="UPDATE Room SET Locked=FALSE WHERE Room_id=102"
                query4="UPDATE Room SET Locked=FALSE WHERE Room_id=100"

                cursor = database.cursor()

                cursor.execute(query1)
                cursor.execute(query2)
                cursor.execute(query3)
                cursor.execute(query4)
                our_print("I get on top of the box, and use the scalpel as a screw driver to open the air vent. "\
                          "I could enter here...")
                cursor.close()
            else:
                our_print("I have nothing to use it on...")
        else:
            our_print("I do not have that item.")
    else:
        our_print("I can't do that.")
 
#checks whether player has certain item with them and then chooses lose or win scenario        
def fight_checker(current_room):
    if current_room == 100:
        value = npc_alive_or_not(current_room)
        
        if value == True:
            cutscene_100()
            cursor = database.cursor()
            query1 = "SELECT Name from Item where Name = 'Scalpel' AND Inventory = TRUE"
            cursor.execute(query1) 
            if cursor.rowcount == 1:
                cutscene_100win()
                query2 = "DELETE from NPC WHERE Npc_Id = 1"
                cursor.execute(query2)
            else:
                cutscene_100lose()    
                sys.exit()
            cursor.close()
            
        else:
            pass    
            
    #elif current_room == 202:
    #elif current_room == 210:
    #elif current_room == 306:
    #elif current_room == 305:
    elif current_room == 401:
        value = npc_alive_or_not(current_room)
        if value == True:
            cursor = database.cursor()
            cutscene_3()
            ending_choice = input("(Should I Forgive / Kill him?)\n")
            
            while True:
                if ending_choice == 'Forgive' or 'forgive' or 'f':
                    print('I see... Thank you.')
                    print('Here is the key to lobby door.\n')
                    query1= "UPDATE Item SET Inventory = TRUE, Hidden= False WHERE Name = A lion-crested key"
                    query2= "DELETE from NPC WHERE Name = Doctor Ingolf Buchwald"
                    cursor.execute(query1)
                    
                    break
                    
                elif ending_choice == 'Kill' or 'kill' or 'k':
                    print('I see... I don\'t regret the things I\'ve done.')  
                    print('...\n\n')
                    print('(He drops down with a final thud on the ground. What looks like')
                    print('a key drops appears near his dead body\n')
                    query3 = "UPDATE Item SET Hidden= False WHERE Name = A lion-crested key"
                    query4 = "DELETE from NPC WHERE Name = Doctor Ingolf Buchwald"
                    cursor.execute(query3)
                    break
                
                else: 
                    print('(Should he pay for what he has done? (Forgive/Kill)')   
                       
            os.system('SomedayAgain.mp3')
            cursor.close()
            
        else:
            pass    
        
    
    else:
        pass
        
 
# check to see if friendly npc exists and talks to them        
def npc_converser(current_room):
    if current_room == 100:
        value = npc_alive_or_not(current_room)
        
        if value == True:
            pass
            
        else:
            pass   
            
    else:
        pass         






    
    

