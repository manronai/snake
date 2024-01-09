class snake:
    import time
    time = time
    def __int__(self):

        pass
    black = (0, 0, 0)
    xaxis = 1
    yaxis = 1
    test = 9
    left = False
    right = False
    vertical = False
    horizontal = True
    up = False
    down = False
    def movement(self):
        if self.test ==1:
            self.xaxis = -1*self.xaxis
        if self.test ==2:
            self.xaxis = abs(self.xaxis)
        if self.test ==3:
            self.yaxis = abs(self.yaxis)
        if self.test == 4:
           self.yaxis = -1*self.yaxis
    def createBody(self, pygame, scr):
        self.screen = scr
        self.pygame = pygame
        if self.horizontal:
            self.pygame.draw.rect(self.screen, self.black, [0 + 1 * self.xaxis, self.yaxis, 10, 10])
            self.pygame.draw.rect(self.screen, self.black, [11 + 1 * self.xaxis, self.yaxis, 10, 10])
            self.pygame.draw.rect(self.screen, self.black, [11*2 + 1 * self.xaxis, self.yaxis, 10, 10])
        if self.vertical:
            self.pygame.draw.rect(self.screen, self.black, [self.xaxis, 0 + 1 * self.yaxis, 10, 10])
            self.pygame.draw.rect(self.screen, self.black, [self.xaxis, 11 + 1 * self.yaxis, 10, 10])
            self.pygame.draw.rect(self.screen, self.black, [self.xaxis, 11*2 + 1 * self.yaxis, 10, 10])
    def moveLeft(self):
        if self.left:
            self.xaxis-=1
            self.time.sleep(0.02)
            self.vertical = False
            self.horizontal = True
    def moveRight(self):
        if self.right:
            self.time.sleep(0.02)
            self.xaxis+=1
            self.vertical = False
            self.horizontal = True
    def moveUp(self):
        if self.up:
            self.yaxis -= 1
            self.time.sleep(0.02)
            self.vertical = True
            self.horizontal = False
    def moveDown(self):
        if self.down:
            self.time.sleep(0.02)
            self.yaxis += 1
            self.vertical = True
            self.horizontal = False
    def move(self):
        self.moveLeft()
        self.moveRight()
        self.moveUp()
        self.moveDown()
    def leftOn(self):
        self.left = True
        self.right = False
        self.up = False
        self.down = False
    def rightOn(self):
        self.right = True
        self.left = False
        self.up = False
        self.down = False
    def upOn(self):
        self.right = False
        self.left = False
        self.up = True
        self.down = False
    def downOn(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = True

