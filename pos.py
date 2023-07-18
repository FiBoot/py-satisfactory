class Pos:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'[{self.x},{self.y}]'
    
    def add(self, rel):
        self.x += rel[0]
        self.y += rel[1]
    