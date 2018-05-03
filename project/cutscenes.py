#npc conversation#
from gamefuncs import *
from queryfuncs import *


def npc_Jake():
    our_print("(A hunch-backed man with bloodshot eyes is incessantly staring at the wall. He doesn't look very well..)\n")
    our_print("Unknown Man: Th-the w-w-walls are spying on me... T-THOSE BASTARDS ARE UP TO SOMETHING BAD I KNOW IT! I-i-i got to keep on eye on them...\n")
    our_print("Verner: Hey, are you okay..?\n")
    our_print("Unknown Man: Leav-v-v me alone! I don't need anything from you!\n")
    our_print("(Maybe it's best for me to leave before something bad happens.)\n")

    
    
    
def npc_Lawrence():    
    our_print("(There's a wretched looking man is sitting in a rusted wheelchair)\n")
    our_print("Unknown Man: Hello young man.\n")
    our_print("Hello..?\n")
    our_print("I'm bored! Do you want to play a game of hangman? If you win I'll give you a reward.\n")
    while True:
        answer = str(input("Do you want to play his game? (Y/N)  "))
        answer = answer.lower()
        if answer == 'y' or answer == 'yes':
            print("Haha, this will be fun!")
            value = hangman()
            if value == True:
                print('Congratulations boy.')
                print('Here is your reward\n')
                print("(You recieve a lighter)")
                query1= "UPDATE Item SET Inventory = TRUE, Hidden= TRUE WHERE Name = 'Lighter'"
                cursor.execute(query1)
            else:
                pass
        cursor.close()    
        if answer == 'n' or answer == 'no':
            print("Shame...") 
            break    
        else:
            print("Please Enter Y or N")
    

def npc_Oliver():    
    our_print("There's a ghostly-looking pale man lying on a hospital bed. His face is filled with sweat")
    our_print("Unknown Man: Hey, are you the doctor? You don't look like one.\n")
    our_print("Verner: Sorry but I'm not.\n")
    our_print("Unknown Man: Can you find the doctor for me? I feel sick after taking the pills he gave me.\n")
    our_print("Verner: Uh... sure, leave it for me.\n")
    our_print("Unknown Man: Just tell him it's Oliver Cromwell asking, s-s-surely he'll remember me.")

def npc_Jonathan():    
    our_print("I can see a confused looking man is walking in circles muttering to himself")
    our_print("Unknown Man: Hey! Heheh... I know you.\n")
    our_print("Verner: Uh, I don't think we have met, you must have mistaken me for someone else.\n")
    our_print("Unknown Man: Hehhehe...\n")
    our_print("(I don't think I will get much out of this conversation.)")
    answer = str(input("Maybe I should ask him something? (Y/N) "))
    answer = answer.lower()
    if answer == 'y' or answer == 'yes':
            our_print("Verner: Hey do you think you could tell me something about this place?")
            our_print("Unknown Man: uh ah... I know oh yes I know... It is the Aliens!")
            our_print("(Yeah, I think I'm done here.)")   
    elif answer == 'n' or answer == 'no':
            print("(I should probably go, this man seems dangerously unstable.)") 
    else :
        print("(I should probably go, this man seems dangerously unstable.)")
    

    

def cutscene_1():
    print("Aaah...")
    print("(Have to find something to numb the pain...)\n\n" 
 
          "Unknown man: (inaudible) There is no way out of (inaudible)\n" 
 
          "\tJust accept your fate.\n\n" 
 
          "Verner: Wha... ?\n\n" 
 
          "Unknown man: Someone will come soon to deliver you. Ne metue.\n\n" 
          
          "\t.\n\t.\n\t.\n\n"
 
          "The Verge© 2018\n" 
          "First time players should type HELP. Credits are available via CREDITS and license via LICENSE.\nType QUIT to quit the game.\n\n\n\n")


def cutscene_2():
    print("Guard: Uuuuuurgghhhhh!")

    print("Guard falls down dead\n")

    print("Doctor: Please don’t kill me!!! I'm useful alive!")
    print("Doctor: I know this looks bad but We are actually helping people here. I don't know why Buchwald chose you, perhaps He thinks you wasted your life with sin.\n")
    
    print('(He spoke with a hint of german accent)\n')
    
    print("Verner: Buchwald?\n")
    
    print("Doctor: Doctor Buchwald is our leader here, he is the one who gave the order to bring you for ah... I mean you know ah... " \
    "First let me introduce myself, my name is Doctor Eisenberg, Reinhold Eisenberg. \n")

    print('(He looks nervous)\n')
    
    print("Eisenberg: I think it is better if you speak with him rather than me. He is at the top floor of this building, but you can't enter without a key."\
    "Luckily I have one of the keys too. Here take it! No need to thank me!\n")
    
    print('(He hands me a simple key)\n')
    
    print('Eisenberg: Well uuh... I can\'t offer anymore help. I must continue my work. \n')

def cutscene_100():
    print("There is man in black patrolling. OH SHIT! He saw me and IS coming after ME! Gotta defend myself!\n")
    
def cutscene_100win():      #After you win the first fight
    print('Verner: Do you have any last words before I end your miserable life?\n')
    print('Guard: Quiet fool! You will regret leaving that room.\n')
    print("Verner: We will see about that! \n")
    print('(I end the fight with a couple swift strikes.)\n')
    print('What a pushover..\n')

def cutscene_100lose():      #After you lose the first fight
    print('Ughh.. Am I really this weak?')
    print('I find myself laying on the ground.')
    print('I cannot move my legs. Maybe this is the end... \n')

    
    print("\t\tRest in peace...\n")
    print("\t\tGAME OVER\n")

def cutscene_win_generic():
    print("That guard was no match for me...\n")
    print("I recompose myself and continue forward.\n")
    
def cutscene_lose_generic():
    print("Arghh! I'm too weak...")
    print("This is too much for me without a weapon.\n")
    print("This is surely the end of me.\n")

    
    print("\t\tRest in peace...\n")
    print("\t\tGAME OVER\n")      
    
def cutscene_3():
    print("Dr. Buchwald: mmh it seems I underestimated you… I should have put more guards in place but oh well… You are here for revenge aren’t you?\n")

    print("Verner: …\n")

    print("Buchwald: Before you make any rash decision, hear me out first.\n")
    
def ending_1():         #kill B
    print("Verner: I know we all do questionable things to survive in this god forsaken wasteland.. But even then, a filth like you doesn't deserve to live.\n")
    print("Dr. Buchwald: NOOoo don't do it!\n")
    print("Verner: This is the end of the line for you Doctor.\n")
    
    
def ending_2():         #forgive B
    print("I wish to get out of this depressive land. Perhaps I'll go to the east and have a fresh start there.") 
    print("Perhaps live an honest life for once. Won't that be great?\n")
    
def ending_3():         #light building on F
    print("They paid for their crimes in full. The fire will wash their souls clean")  
    print("The innocent are guilty too, guilty of accepting what is not theirs.\n")   
    
def ending_4():         #Escape before X
    print("Necessity is the mother of ingeniousness. You solve your problems with a touch of craftiness. \n") 
        
def ending_5():         #harakiri
    print("Sometimes the most interesting thing you can do with your life is end it. It is your own choice. May death bring you peace you never had.\n")         

def death_msg():
    print("\t\tRest in peace...\n")
    print("\t\tGAME OVER\n")
    
def the_end():
    print('\t\tCongratulations!\n')
    print('\t\tYou finished the game. Explore additional endings by trying alternative paths\n')

