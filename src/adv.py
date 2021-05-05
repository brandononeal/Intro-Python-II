from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('Sword', 'God\'s mighty weapon'), Item('Shovel', 'The digger supreme')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[Item('Bow', 'God\'s traveling arrow shooter'), Item('Ruby', 'A dull crystal')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('Helmet', 'Protect thy head'), Item('Redstone', 'Used to build mechanisms')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('Cube', 'Dull cube'), Item('Bandaid', 'Used to heal')]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Main

game = True
player = Player('Brandon', room['outside'], [Item('Apple', 'A tasty snack'), Item('Boots', 'Protection galore')])

def movement(dir):
    player.move(attribute)
    print(f'\n{player.name} moved {dir} to {player.current_room.name}')
    print(f'{player.current_room.description}\n')
    print(f'Items in room: {player.current_room.__str__()}')
    print(f'Items in inventory: {player.__str__()}')

while game:
    try:
        selection = input('Input an action: ')
        attribute = selection + '_to'
        take = selection.replace('take ', '')
        drop = selection.replace('drop ', '')

        if selection == 'n':
            movement('north')
            continue
        if selection == 's':
            movement('south')
            continue
        if selection == 'e':
            movement('east')
            continue
        if selection == 'w':
            movement('west')
            continue
        if selection == 'q':
            print('Game over')
            game = False
        if 'take' in selection:
            player.take_item(take)
            continue
        if 'drop' in selection:
            player.drop_item(drop)
            continue
        else:
            print('\nPlease input a valid command:\nn, s, e, w, q, take [item], or drop [item]\n')
    
    except AttributeError:
        print(f'You can\'t go that direction\n')
