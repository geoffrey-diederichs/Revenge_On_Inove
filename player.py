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

    def animate(self):
        if self.frameRate == 50:
            self.frameRate = 0
            if self.frameX >= 32:
                self.frameX = 0
            else:
                self.frameX += 16
        else:
            self.frameRate += 1
