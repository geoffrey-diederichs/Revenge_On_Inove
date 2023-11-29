class Player:
    def __init__(self, x: int, y:int, char: int = 1):
        self.position_x = x
        self.position_y = y
        self.width = 16
        self.height = 24
        self.imgSrc = 'img/player.png'
        self.frameX = 64
        self.frameY = 0
        self.frameRate = 0
        self.framesX = 8-1
        self.framesY = 2-1
        self.char = 1
        self.sprint = 0
        self.totalFrames = 60

    def animate(self, pressed: bool):
        if self.sprint == 0:
            self.totalFrames = 50
        elif self.sprint != 0:
            self.totalFrames = 30
            if self.frameRate > 30:
                self.frameRate = 0

        if self.char == 1:
            self.charFrame = 24
            self.frame = 24
        elif self.char == 2:
            self.charFrame = 24*5
            #self.frame = 24*5
        elif self.char == 3:
            self.charFrame = 24*9
            self.frame = 24*9

        if pressed:
            if self.frameRate == self.totalFrames:
                if self.frameY < self.framesY*self.height+self.height+self.charFrame:
                    self.frameY += self.height
                else:
                    self.frameY = self.charFrame
                self.frameRate = 0
            else:
                self.frameRate+=1
        else:
            self.frameY = self.charFrame+self.height
