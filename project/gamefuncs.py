import random
import sys
from queryfuncs import *
from cutscenes import *
from config import db
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
                        "Drop {object}. Leaves object on the ground.",
                        "Talk {person}. Initiate conversation with person. \n"]
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


def go(current_room, room_to_move):
    current_room = str(current_room)
    room_to_move = str(room_to_move)

    if room_to_move in room_list_returner(current_room):
        our_print(show_room(room_to_move))

        return room_to_move
    else:
        print("You can't go there.")
        return current_room


def commands():
    allcommands = [["enter", "e", "go"],    #done
                   ["examine", "x"],    #done
                   ["leave", "exit"], #done
                   ["quit", "q"],   #done
                   ["push"],    #done 
                   ["take","pick"], #done
                   ["inventory", "i"],  #done
                   #["kick"],
                   ["search"], #done
                   ["look"],    #done
                   ["use"], #requires to implement on all objects that can be used
                   ["up", "u"], #done
                   ["down", "d"],#done
                   ["credits"], #done
                   ["license"], #done
                   ["help"],    #done
                   ["clear", "c"],#done
                   ["drop"], #done
                   ["talk"], #done
                   ["kill"] #supersecret
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
        answer = str(input("Do you really want to quit the game? (Y/N)  "))
        answer = answer.lower()
        if answer == 'y' or answer == 'yes':
            print("Exiting...")
            sys.exit()
        elif answer == 'n' or answer == 'no':
            print("Returning to game...") 
            break    
        else:
            print("Please Enter Y or N")

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

        item_name = item_name_from_id(item_to_find)
        our_print("I found this: \n" + item_name)
        cursor.close()

    else:
        our_print("I didn't find anything.")
        
def up(current_room):
    current_room = str(current_room)
    stairs = room_list_returner(current_room)
    if "200" in stairs and current_room == "100":
        go(current_room,"200")
        return 200
    elif "300" in stairs and current_room == "200":
        go(current_room,"300")
        return 300
    elif "400" in stairs and current_room == "300":
        go(current_room,"400")
        return 400
    else:
        print("I cannot go up from here...")
        return None

def down(current_room):
    current_room = str(current_room)
    stairs = room_list_returner(current_room)
    if "300" in stairs and current_room == "400":
        go(current_room,"300")
        return 300
    elif "200" in stairs and current_room == "300":
        go(current_room,"200")    
        return 200
    elif "100" in stairs and current_room == "200":
        go(current_room,"100")    
        return 100
    else:
        print("I cannot go down from here...")   
        return None       
    
def leave(current_room):
    current_room = str(current_room)
    corridors = ["100","110","200","210","300","310","400","410"]
    rooms = room_list_returner(current_room)
    if current_room not in corridors:
        for room in rooms:
            if room in rooms:
                go(current_room,room)
                return room
            else:
                pass
     
    else:
     print('I cannot leave from here...\n') 
     return None  

def use(item_name, room_id, database=db):
    inventory = get_items_inventory()
    print(item_name)
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
                query1="UPDATE ITEM SET Hidden=TRUE WHERE Item_id=100"
                query2="UPDATE Item SET Hidden=FALSE WHERE Item_id=103"
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
    elif item_name == "simple key" and room_id == "400":
         item_id = item_id_from_name(item_name)

         if item_id in inventory and if_item_used(item_id) == False:
             query1 = "UPDATE Item SET Used=TRUE WHERE Item_id =" + str(item_id)
             query2 = "UPDATE Room SET Locked=FALSE WHERE Room_id = 401"

             cursor = database.cursor()
             cursor.execute(query1)
             cursor.execute(query2)
             cursor.close()
             our_print("A door opens...")
         else:
             our_print("I can't do that.")
    elif item_name == "lion-crested key":
        item_id = item_id_from_name(item_name)

        if item_id in inventory and room_id == "110":
            query1 = "UPDATE Item SET Used=TRUE WHERE Item_id" + str(item_id)

            cursor = database.cursor()
            cursor.execute(query1)
            cursor.close()
            our_print("I twist the key in it's hole and a hollow crackle echoes throughout the hallways." +
                      "The heavy, rusted doors slowly begin to give in to my pushes, and a way to the outside world opens." +
                      "A cool, refreshing wind blows inside, clearing the stuffy air of this damned building.")

    else:
        our_print("I can't do that.")
 
#checks whether player has certain item with them and then chooses lose or win scenario        
def fight_checker(current_room, database=db):
    if current_room == "100":
        value = npc_alive_or_not(current_room)
        
        if value == True:
            cutscene_100()
            cursor = database.cursor()
            query1 = "SELECT Name from Item where Name = 'Scalpel' AND Inventory = TRUE"
            cursor.execute(query1)

            if cursor.rowcount == 1:
                cutscene_100win()
                query2 = "DELETE from NPC WHERE Npc_Id = 1"
                query3 = "UPDATE Item SET Name = 'Broken Scalpel' where Name = 'Scalpel'"
                query4 = "UPDATE Item SET Description = 'It is a broken scalpel. What do I even do with this?' where Name = 'Broken Scalpel'"
                query5 = "UPDATE Texti SET ActualText = 'A normal corridor with five rooms and stairs leading up. There is a dead body of the first guard I killed.\n' WHERE Room_Id = 100"
                print('The scalpel breaks\n') 
                cursor.execute(query2)
                cursor.execute(query3)
                cursor.execute(query4) 
                cursor.execute(query5) 

            else:
                cutscene_100lose()    
                sys.exit()
            cursor.close()
            
        else:
            pass    
            
    elif current_room == "202":
        value = npc_alive_or_not(current_room)
        
        if value == True:
            print('Another guard in black is standing in the room, he looks surprised to see me.\n') 
            cursor = database.cursor()
            query1 = "SELECT Name from Item where Name = 'Metal pipe' AND Inventory = TRUE"
            query2 = "SELECT Name from Item where Name = 'Knife' AND Inventory = TRUE"

            cursor.execute(query1) 

            if cursor.rowcount == 1:
                cutscene_win_generic()
                query3 = "DELETE from NPC WHERE Npc_Id = 2"
                cursor.execute(query3) 
                query4 = "UPDATE Texti SET ActualText = 'Seems like an old patient room. On the floor the guard is dead' WHERE Room_Id = 202"
                cursor.execute(query4) 
            else:
               cursor.execute(query2) 
               if cursor.rowcount == 1:
                    cutscene_win_generic()
                    query3 = "DELETE from NPC WHERE Npc_Id = 2"
                    query4 = "UPDATE Texti SET ActualText = 'Seems like an old patient room. On the floor the guard is dead' WHERE Room_Id = 202"
                    cursor.execute(query4) 
                    cursor.execute(query3) 
               else: 
                    cutscene_lose_generic()
                    sys.exit()

            cursor.close()
            
        else:
            pass    

    elif current_room == "210":
        value = npc_alive_or_not(current_room)
        
        if value == True:
            print('I notice a guard in the corridor, I sneak quietly behind him. Just when I\'m about to reach him')
            print('He turns his head around!\n') 
            cursor = database.cursor()
            query1 = "SELECT Name from Item where Name = 'Metal pipe' AND Inventory = TRUE"
            query2 = "SELECT Name from Item where Name = 'Knife' AND Inventory = TRUE"

            cursor.execute(query1) 

            if cursor.rowcount == 1:
                cutscene_win_generic()
                query3 = "DELETE from NPC WHERE Npc_Id = 3"
                query4 = "UPDATE Texti SET ActualText = 'A corridor with two rooms. On the east side, the building is damaged and broken. A dead body I left still lies on the floor.' WHERE Room_Id = 210"
                cursor.execute(query4) 
                cursor.execute(query3)
                cursor.close()

            else:
               cursor.execute(query2) 
               if cursor.rowcount == 1:
                    cutscene_win_generic()
                    query3 = "DELETE from NPC WHERE Npc_Id = 3"
                    query4 = "UPDATE Texti SET ActualText = 'A corridor with two rooms. On the east side, the building is damaged and broken. A dead body I left still lies on the floor.' WHERE Room_Id = 210"
                    cursor.execute(query4) 
                    cursor.execute(query3)
                    cursor.close()
               else: 
                    cutscene_lose_generic()
                    sys.exit()

            cursor.close()
            
        else:
            pass   

    elif current_room == "306":
        value = npc_alive_or_not(current_room)
        
        if value == True:
            print('Two guards are talking when I enter, the further one notices me.')
            print('Before he can react, I move quickly behind the other one.\n') 
            cursor = database.cursor()
            query1 = "SELECT Name from Item where Name = 'Metal pipe' AND Inventory = TRUE"
            query2 = "SELECT Name from Item where Name = 'Knife' AND Inventory = TRUE"

            cursor.execute(query1) 

            if cursor.rowcount == 1:
                cutscene_win_generic()
                query3 = "DELETE from NPC WHERE Npc_Id = 4"
                query4 = "DELETE from NPC WHERE Npc_Id = 5"
                cursor.execute(query3) 
                cursor.execute(query4) 
                query6 = "UPDATE Texti SET ActualText = 'A room with old machines. Two dead guard bodies are on the floor.' WHERE Room_Id = 210"
                cursor.execute(query6) 

            else:
               cursor.execute(query2) 

               if cursor.rowcount == 1:
                    cutscene_win_generic()
                    query5 = "DELETE from NPC WHERE Npc_Id = 4"
                    query6 = "DELETE from NPC WHERE Npc_Id = 5"
                    cursor.execute(query5) 
                    cursor.execute(query6) 
                    query4 = "UPDATE Texti SET ActualText = 'A room with old machines. Two dead guard bodies are on the floor.' WHERE Room_Id = 210"
                    cursor.execute(query4) 
               else: 
                    cutscene_lose_generic()
                    sys.exit()

            cursor.close()
            
        else:
            pass   

    elif current_room == "305":
        value = npc_alive_or_not(current_room)
        
        if value == True:
            print('When I enter the room, the most strange scene is met. What looks like a doctor is')
            print('standing over a naked man lying on a hospital bed. Beside him is a guard')
            print(', both of them have their backs to me... I sneak closely and then go for the kill.\n') 
            cursor = database.cursor()
            query1 = "SELECT Name from Item where Name = 'Metal pipe' AND Inventory = TRUE"
            query2 = "SELECT Name from Item where Name = 'Knife' AND Inventory = TRUE"
            query3 = "DELETE from NPC WHERE Npc_Id = 6"
            query4 = "DELETE from NPC WHERE Npc_Id = 11"
            query5 = "DELETE from NPC WHERE Npc_Id = 12"
            query6 = "UPDATE Texti SET ActualText = 'An operating room with surgery instruments lying scattered around. The doctor and patient on the table are gone, I wonder where they went...' WHERE Room_Id = 305"

            cursor.execute(query1) 

            if cursor.rowcount == 1:
                cutscene_win_generic()
                cursor.execute(query3) 
                cursor.execute(query4)
                cursor.execute(query5)
                cursor.execute(query6)
                cutscene_2()

            else:
               cursor.execute(query2) 
               if cursor.rowcount == 1:
                    cutscene_win_generic()
                    cursor.execute(query3) 
                    cursor.execute(query4)
                    cursor.execute(query5)
                    cursor.execute(query6)
                    cutscene_2() 
               else: 
                    cutscene_lose_generic()
                    sys.exit()

            cursor.close()
            
        else:
            pass   

    elif current_room == "401":
        value = npc_alive_or_not(current_room)
        if value == True:
            cursor = database.cursor()
            cutscene_3()
            ending_choice = input("(Should I Forgive / Kill him?)\n")
            
            while True:
                if ending_choice == 'Forgive' or 'forgive' or 'f':
                    print('I see... Thank you.')
                    print('Here is the key to lobby door.\n')
                    query1= "UPDATE Item SET Inventory = TRUE, Hidden= False WHERE Name = 'lion-crested key'"
                    query2= "DELETE from NPC WHERE Name = 'Doctor Ingolf Buchwald'"
                    query3 = "UPDATE Texti SET ActualText = 'A room full of pictures of the brain. Dr. Buchwald is busy continuing his work.' WHERE Room_Id = 401"
                    cursor.execute(query1)
                    cursor.execute(query2)
                    cursor.execute(query3)
                    return True
                    break
                    
                elif ending_choice == 'Kill' or 'kill' or 'k':
                    print('I see... I don\'t regret the things I\'ve done.')  
                    print('...\n\n')
                    print('(He drops down with a final thud on the ground. What looks like')
                    print('a key drops appears near his dead body\n')
                    query1 = "UPDATE Item SET Hidden= False WHERE Name = 'lion-crested key'"
                    query2 = "DELETE from NPC WHERE Name = 'Doctor Ingolf Buchwald'"
                    query3 = "UPDATE Texti SET ActualText = 'A room full of pictures and diagrams of the brain. Dr. Buchwald is on the floor dead.' WHERE Room_Id = 401"
                    cursor.execute(query1)
                    cursor.execute(query2)
                    cursor.execute(query3)
                    return False
                    break
                
                else: 
                    print('(Should he pay for what he has done? (Forgive/Kill)')   
                    continue
                       
            os.system('SomedayAgain.mp3')
            cursor.close()
            
        else:
            pass    
        
    
    else:
        pass
        
 
# check to see if friendly npc exists and talks to them        
def npc_converser(name,database=db):
    cursor = database.cursor()
    query = "SELECT Talked FROM Npc WHERE Name = " 
    
    if name == "Jake":
        query1 = query + str(name) 
        value = cursor.execute(query1)
        
        if value == True:
            npc_Jake()
            query2 = "UPDATE Npc SET Talked = TRUE WHERE Name = " + str(name)  
            
        else:
            query3 = "SELECT Conversation FROM NPC WHERE Name = " + str(name)
            repeating_converse =  cursor.execute(query3)
            print(repeating_converse)   
            

    elif name == "Lawrence":  
        query1 = query + str(name) 
        value = cursor.execute(query1)
        
        if value == True:
            npc_Lawrence()
            query2 = "UPDATE Npc SET Talked = TRUE WHERE Name = " + str(name)  
            
        else:
            query3 = "SELECT Conversation FROM NPC WHERE Name = " + str(name)
            repeating_converse =  cursor.execute(query3)
            print(repeating_converse)   
            
      
    elif name == "Cromwell":  
        query1 = query + str(name) 
        value = cursor.execute(query1)
        
        if value == True:
            npc_Oliver()
            query2 = "UPDATE Npc SET Talked = TRUE WHERE Name = " + str(name)  
            
        else:
            query3 = "SELECT Conversation FROM NPC WHERE Name = " + str(name)
            repeating_converse =  cursor.execute(query3)
            print(repeating_converse)   
       
    elif name == "Gebhard":  
        query1 = query + str(name) 
        value = cursor.execute(query1)
        
        if value == True:
            npc_Jonathan()
            query2 = "UPDATE Npc SET Talked = TRUE WHERE Name = " + str(name)  
            
        else:
            query3 = "SELECT Conversation FROM NPC WHERE Name = " + str(name)
            repeating_converse =  cursor.execute(query3)
            print(repeating_converse)   
#HANGMAN
def hangman():
    def guess_letter(word, letter, guessed_list):

        if letter not in guessed_list:
            guessed_list.append(letter)
            for c in word:
                if letter == c:
                    return True
        return False

    def check_if_solved(guessed_list: list, correct_list: list) -> bool:
        if guessed_list == correct_list:
            return True
        else:
            return False

    def show_puzzle(word, correct_list):
        hidden_word = ""
        for c in word:
            if c in correct_list:
               hidden_word += c
               hidden_word += ' '
            else:
                hidden_word += '_ '
        return hidden_word

    def ask_letter():
        letter = str(input("Guess a letter: "))
        return letter

    words = open('words.txt')
    ff = words.read()
    d = ff.splitlines()
    lista = []

    for word in d:
        if len(word) > 5:
            lista.append(word)

    guess_word = lista[random.randint(0, len(lista)-1)]
    letters = []

    for c in guess_word:
       if c not in letters:
           letters.append(c)
    letters.sort()

    guess_count = 0
    guessed_list = []
    correct_list = []

    while guess_count < 6 and correct_list != letters:
        print("The word is: \n", show_puzzle(guess_word, correct_list))
        let = ask_letter()

        if let.isalpha() and len(let) == 1:

            if guess_letter(guess_word, let, guessed_list):
                correct_list.append(let)
                correct_list.sort()

                if check_if_solved(correct_list, letters):
                    print("you guessed right, YOU WIN!")
                    return True
            else:
                guess_count += 1
                ss = "You guessed wrong... STRIKE"
                print(ss, guess_count)
        else:
            print("Not a letter.")
            
        return False

def kill(name, database=db):         ## kill function. Only works for self not npcs.
    if name == 'Myself' or 'myself' or 'Verner' or 'verner':
      
     cursor = database.cursor()
     ## check if user has Scalpel or Knife ##
     query1 = "SELECT Name from Item where Name = 'Scalpel' AND Inventory = TRUE"
     query2 = "SELECT Name from Item where Name = 'Knife' AND Inventory = TRUE"
     cursor.execute(query1)
     if cursor.rowcount == 1:
        ending_5()      ## call one of the endings
        sys.exit() 
     else: 
      cursor.execute(query2)
      if cursor.rowcount == 1:
        ending_5()
        sys.exit()
      else:
          print('I can\'t do that...\n')    
     cursor.close()
 
    else: 
     print('I do not want to do that...\n') 

def talk(name): #talks to npc
    npc_converser(name)
