class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description 
        self.items = items

    def __str__(self):
        output = f'\n'

        if len(self.items) < 1:
            output = f'No items available in {self.name}'
        else:
            for i in self.items:
                output += f'{i}\n'

        return output
