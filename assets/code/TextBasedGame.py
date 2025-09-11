# Text Based Game by Erica Boterf

# Function to display user instructions
def user_instructions():
    print('-------------------')
    print('Welcome to nap time!')
    print('Your goal is to clean the house and feed yourself without waking up the sleeping toddler!')
    print('\nMove through the rooms using the commands North, South, East, West.')
    print('Each room contains an item you must retrieve. Use the item name and "retrieve" to pick up the item.')
    print('\nGood Luck!')

# Function to display the current room and its items
def current_room(room, rooms, items):
    print(f'You are in the {room}.')
    if room in rooms:
        print('In this room you see: ')
        for item, room_in_item in items.items():
            if room == room_in_item:
                print(f'- {item}')

# Function to display the player's inventory
def current_inventory(inventory):
    if len(inventory) > 0:
        print('Your inventory contains: ')
        for item in inventory:
            print(f'- {item}')
    else:
        print('Your inventory is empty.')

# Function to prompt the player for input
def get_command():
    return input('What would you like to do? ')


# Main gameplay function
def game_play():
    # Rooms with possible directions
    rooms = {
        'Foyer': {'East': 'Pantry', 'North': 'Living room', 'South': 'Dinning room', 'West': 'Kitchen'},
        'Pantry': {'North': 'Porch', 'West': 'Foyer'},
        'Porch': {'South': 'Pantry'},
        'Dinning room': {'East': 'Laundry', 'North': 'Foyer'},
        'Laundry': {'West': 'Dinning room'},  # Villain here
        'Kitchen': {'East': 'Foyer'},
        'Living room': {'South': 'Foyer', 'West': 'Bathroom'},
        'Bathroom': {'West': 'Living room'}
    }

    # Items and the rooms they are in
    items = {
        'laundry': 'Bathroom',
        'vacuum': 'Living room',
        'sandwich': 'Kitchen',
        'dirty dish': 'Dinning room',
        'soda': 'Porch',
        'broom': 'Pantry'
    }

    # Player's inventory
    inventory = []

    # Starting room
    current_room_name = 'Foyer'

    # Show instructions
    user_instructions()

    # Total items to collect
    total_items = len(items)

    # Game loop
    while True:
        # Show current room, inventory, and items
        current_room(current_room_name, rooms, items)
        current_inventory(inventory)

        # Print a blank line for better input formatting
        print()  # Empty line for user input

        # Prompt user for command
        command = get_command().lower().strip()

        # Command to move between rooms (without "go")
        if command.capitalize() in rooms[current_room_name]:  # Check if the direction is valid
            # Move to the new room
            current_room_name = rooms[current_room_name][command.capitalize()]
            print(f'You moved to the {current_room_name}.')
        elif command.startswith('get ') or command.startswith('retrieve '):  # Item retrieval logic
            item_name = command[4:] if command.startswith('get ') else command[9:]  # Extract item name
            item_name = item_name.strip()  # Clean the item name input

            if item_name in items and items[item_name] == current_room_name:  # Check if item is in the current room
                if item_name not in inventory:
                    inventory.append(item_name)
                    del items[item_name]  # Remove the item from the game after it's retrieved
                    print(f'You have retrieved the {item_name}.')

                    # Check if the player has collected all items
                    if len(inventory) == total_items:
                        print("Congratulations! You've collected all the items and won the game!")
                        break  # Player wins
                else:
                    print(f'You already have the {item_name}.')
            else:
                print(f'No item named "{item_name}" in this room.')
        elif command == 'exit':  # Exit command (optional for stopping the game)
            print("Exiting the game.")
            break
        else:
            print("Invalid command. Try again.")

        # Check if the player entered the Laundry room (villain room)
        if current_room_name == 'Laundry':
            print("Oh no! You woke up the toddler! Game Over.")
            break  # Player loses


if __name__ == "__main__":
    game_play()
