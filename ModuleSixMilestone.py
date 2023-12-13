#King Jones-Frazier
# Starter Code
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}
DIRECTIONS = ['North', 'South', 'East', 'West']
EXIT_COMMAND = "Exit"
VALID_INPUTS = DIRECTIONS + [EXIT_COMMAND]
INVALID_DIRECTION = "That is not a valid direction. You need to enter one of: " +\
    str(VALID_INPUTS) + "."
CANNOT_GO_THAT_WAY = "You bumped into a wall."
GAME_OVER = "Thanks for playing."
EXIT_ROOM_SENTINEL = "exit"

# IMPORTANT: When submitting to Sense, do not modify any code above this line or the function signature below.

def navigate(current_room: str, user_input: str):
    """
    Given a current_room in rooms and a user_input, return a tuple (next_room, err_msg) with
    next_room -- where you are after or EXIT_ROOM_SENTINEL
    err_msg -- message to print, if any, empty, GAME_OVER, INVALID_DIRECTION, or CANNOT_GO_THAT_WAY
    """
    next_room = current_room
    err_msg = ''
    
    # YOUR CODE HERE
    
    #cleaning up the input
    current_room = current_room.strip().title()
    user_input = user_input.strip().title()
    
    		
    
    #direction is valid and not exit
    if (user_input in DIRECTIONS):
        #check if direction is available in that room then assigns the room in that direction to next_room
        if user_input in rooms[current_room]:
            next_room = rooms[current_room][user_input]
        #if that direction doesn't lead to a room send error message  
        else:
            next_room = current_room
            err_msg = CANNOT_GO_THAT_WAY
            
        	# if want to exit
    elif user_input == EXIT_COMMAND:
        print('user_input is', user_input)
        next_room = EXIT_ROOM_SENTINEL
        err_msg = GAME_OVER
    else:  #if the direction is invalid
        next_room = current_room
        err_msg = INVALID_DIRECTION
        
    
    # Do not modify anything below this line. 
    
    return next_room, err_msg

room = input('room:')
direction = input('direction:')
navigate(room, direction)