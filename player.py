class Player:
    def __init__(self, x: int, y:int, char: int = 1):
        self.position_x = x
        self.position_y = y
        self.width = 16
        self.height = 24
        self.imgSrc = 'img/player.png'
        self.frameX = 64
        self.frameY = 24*2
        self.frameRate = 0
        self.framesX = 8-1
        self.framesY = 2
        #1=robot, 2=girl, 3=boi
        self.char = 1

    def animate(self, pressed: bool):
        if pressed:
            if self.frameRate == 60:
                self.frameRate = 0
                if self.frameY >= self.height*self.framesY:
                    self.frameY = 24
                else:
                    self.frameY += self.height*2
            else:
                self.frameRate += 1
        else:
            self.frameY = 24*2
