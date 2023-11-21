class Collision:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 16
        allCollisions.append(self)
        
allCollisions = []
