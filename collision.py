class Collision:
    allCollisions = []
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 16
        #fixed are var that will stay at the original pos on the other hand, x and y will move to match the background movements
        self.fixedX = x
        self.fixedY = y
        Collision.allCollisions.append(self)
        
