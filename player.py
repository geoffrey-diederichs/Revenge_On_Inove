class Player:
    def __init__(self, x: int, y:int):
        self.position_x = x
        self.position_y = y
        self.width = 16
        self.height = 16
        self.imgSrc = 'img/player.png'
        self.frameX = 0
        self.frameY = 0
        self.frameRate = 0
