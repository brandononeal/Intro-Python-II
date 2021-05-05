class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description 
        self.items = items

    def __str__(self):
        output = f'\n'

        if len(self.items) < 1:
            output = f'\nNo items available in {self.name}\n'
        else:
            for i,item in enumerate(self.items):
                output += f'[{i + 1}] {item}\n'

        return output
