#King Jones-Frazier

from time import sleep
'''
Scenario/theme
You've been grounded for pulling a scary prank on one of your teachers.
But you want to go to a halloween party.  You must look for the items to 
complete your halloween costume and sneak out the house without being 
noticed

'''
#global variables
DIRECTIONS = ['north', 'south', 'east', 'west']
EXIT_COMMAND = "exit"
VALID_INPUTS = DIRECTIONS + [EXIT_COMMAND]
INVALID_DIRECTION = "That is not a valid direction. You need to enter one of: " +\
    str(VALID_INPUTS) + "."
CANNOT_GO_THAT_WAY = "You bumped into a wall."
GAME_OVER = "Thanks for playing."
EXIT = "exit"
backPack = []
current_room = 'bedroom'

#print text slowly. cool
def print_slow(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.03)
    print() # go to new line

#pause for effect
def pause():
    pause = input("\n press any key to continue\n")

#dictionary of rooms and moves
rooms = {
         'bedroom': {'south': '', 'east': 'attic', 'item':''},
         'attic': {'south': 'masterbedroom', 'west': 'bedroom', 'item':'costume'},
         'masterbedroom': {'east': 'hall', 'north': 'attic', 'item': 'police vest'},
         'hall': {'north':'bathroom', 'south':'kitchen','west':'masterbedroom','item':'scissors'},
         'bathroom':{'south':'hall','item':'makeup'},
         'kitchen':{'north':'hall', 'south':'garage','item':'ketchup'},
         'garage':{'north':'kitchen', 'item':'wd-40'},
         'living room': 'game over'
}
# items needed are costume,police vest, scissors, makeup, ketchup, and wd-40

#navigation
def navigate(user_input):
    global current_room
    global backPack

    if user_input == 'full':
        print_slow('inventory full')
        backPack = ['costume','police vest','scissors','makeup','ketchup','wd-40']
    err_msg = ''
   
    #to check inventory
    if user_input == 'check':
        inventory_check(backPack)
        return current_room
    else:
        pass
   
    
    #direction is valid and not exit
    if (user_input in DIRECTIONS):
        
        
        #check if direction is available in that room then assigns the room in that direction to next_room
        if user_input in rooms[current_room]:
            
            #looks in rooms, looks for the current_room then takes the direction from user_input to find the next room
            
            if (rooms[current_room][user_input]):
                next_room = rooms[current_room][user_input]
            else:
                print_slow('\nYou made it to the living room where your parents are watching a scary movie.\n They look at you.\n Parents: "You know you done f***** up right?"')
                return 'exit'
        #if that direction doesn't lead to a room send error message  
        else:
            
            next_room = current_room
            print( CANNOT_GO_THAT_WAY)
            
        	# if want to exit
    elif user_input == EXIT_COMMAND:
        return 'exit'


    else:  #if the direction is invalid
    
        next_room = current_room
        print_slow( INVALID_DIRECTION)
    
    #inventory update
    
    current_room = next_room
    inventory_update(current_room,backPack)
    
    
    #pause()
    return current_room

#takes the room then looks up the item if there is one, then looks up if its already in inventory
def inventory_update(room, lst):
    #if that room has an item assigns item that item
    if (rooms[room]["item"]):

        item = rooms[room]['item']
        
    else:
        return
    
    #if item is not in back pack then adds it to back pack and tells player
    if not item in lst:
        purpose = item_purpose(item)
        print_slow(f'\n You find yourself in {current_room} and you see {item}! {purpose}')
        lst.append(item)
        
        
        return lst
    else:
        pass
   
# say a different thing depending on what item is found
def item_purpose(item):
    purpose = ''
    if item == 'costume':
        purpose = 'The police costume. The most important item.\n'
    elif item == 'police vest':
        purpose = 'Your mother\'s police vest to add a little authenticity to your costume.\n'
    elif item =='scissors':
        purpose = 'Scissors to cut up your costume.\n'
    elif item =='makeup':
        purpose = 'Makeup to give you that gaunt look\n'
    elif item =='ketchup':
        purpose = 'Ketchup to simulate blood\n'
    elif item == 'wd-40':
        purpose = 'wd-40 to make a silent get away\n'

    return purpose

#allows the player to check their back pack
def inventory_check(lst):
    if len(lst) == 0:
        print_slow('\n You look in your back pack. You haven\'t got anything.You need 6 items. \n' )
    else:

        print_slow(f'\nYou look in your back pack. You have acquired {lst}; {len(lst)} item(s). You need {6 -len(lst)} more items\n')
    if len(lst) == 6:
        print_slow('You now have everything you need for your zombie police officer costume \n and everything you need to escape unnoticed. \n Return to your room to escape to the party\n')

#present the scenario
print_slow('You\'ve been grounded for pulling a scary prank on one of your teachers.\n But you want to go to a halloween party.\n  You must look for the items to complete your halloween costume and sneak out the house without being noticed...\n')

#Main loop
while current_room != EXIT:
     #game winning condition
    if current_room == 'bedroom' and len(backPack) == 6:
        print_slow('You\'ve made it to your room with all your stuff.  You use the wd-40 to grease your window and escape in silence.')
        print_slow(GAME_OVER)
        exit()
    else: 
        pass
    print_slow(f'You are currently in the {current_room}...')
    print_slow("Which direction will you go?\n or type 'check' to check back pack: ")
    user_input = input().strip().lower()
    choice = navigate( user_input)
    if choice == 'exit':
        print_slow(GAME_OVER)  
        exit()
   