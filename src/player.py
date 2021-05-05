class Player:
    def __init__(self, name, starting_room, inventory = []):
        self.name = name
        self.current_room = starting_room
        self.inventory = inventory
    
    def move(self, dir):
        # Checks if we can move in specific direction
        # If not, hits AttributeError in while loop
        getattr(self.current_room, dir)
        if hasattr(self.current_room, dir):
            self.current_room = getattr(self.current_room, dir)

    def take_item(self, item): 
        for x in self.current_room.items:
            if x.name.strip().lower() == item.strip().lower():
                self.inventory.append(x)
                self.current_room.items.remove(x)
                print(f'Added {item} to your inventory\n')
            else:
                print(f'No {item} found in this room\n')
                break
    
    def drop_item(self, item):
        for x in self.inventory:
            if x.name.strip().lower() == item.strip().lower():
                self.inventory.remove(x)
                self.current_room.items.append(x)
                print(f'Dropped {item}\n')
            else:
                print(f'You do not have {item} to drop.\n')
                break

    def __str__(self):
        output = '\n'

        if len(self.inventory) < 1:
            output = 'Nothing currently in your inventory'
        else:
            for i, item in enumerate(self.inventory):
                output += f'[{i + 1}] {item}\n'

        return output
