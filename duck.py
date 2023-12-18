import pygame, random

class Duck:
    def __init__(self,surface):
        self.currentindexDuck = 0 
        self.dead = False
        self.moveupanddownboolean = False 
        self.DirectionX = "left" 
        self.DirectionY = "down"
        self.imagelistDuck = [] 
        for counter in range(3):
            self.imagelistDuck.append(pygame.image.load("images/duckEast" + str(counter) + ".png"))
        for counter1 in range(3):
            self.imagelistDuck.append(pygame.image.load("images/duckWest" + str(counter1) + ".png"))
        self.imagelistDuck.append(pygame.image.load("images/fallingDuck.png"))
        self.currentimageDuck = self.imagelistDuck[self.currentindexDuck]
        self.width = self.currentimageDuck.get_width() 
        self.height = self.currentimageDuck.get_height() 
        self.surfacewidth = surface.get_width()
        self.xpos = random.choice([0 - self.width, surface.get_width()])
        self.ypos = random.randint(0,250)
        self.xdir = 8
        self.ydir = 8
        
    def getBounds(self):
        return pygame.Rect(self.xpos,self.ypos,self.width,self.height)

    def getDirectionX(self):
        return self.DirectionX
    
    def getDirectionY(self):
        return self.DirectionY
    
    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width
    
    def getX(self):
        return self.xpos
    
    def getY(self):
        return self.ypos

    def getLocation(self):
        return(self.xpos,self.ypos)
    
    def getImage(self):
        return self.currentimageDuck
    
    def isDead(self):
        return self.dead
    
    def killDuck(self):
        self.dead = True
        self.currentimageDuck = self.imagelistDuck[6]
        if self.ypos <= 300:
            self.ydir = 10
            self.xdir = 0 

    def move(self):
        if self.DirectionX == "right": 
            if self.dead == True:
                self.ypos += 10
                if self.ypos >=300:
                    self.reset()
            elif self.DirectionY == "down":
                self.ypos += self.ydir
            elif self.DirectionY == "up":
                self.ypos -= self.ydir
            self.xpos += self.xdir
            if self.dead == False:
                self.currentindexDuck += 1
                if self.currentindexDuck == 3:
                    self.currentindexDuck = 0
            elif self.dead == True:
                self.currentindexDuck = 6 
        elif self.DirectionX == "left" :
            if self.dead == True:
                self.ypos += 10
                if self.ypos >= 300:
                    self.reset()
            elif self.DirectionY == "down":
                self.ypos += self.ydir
            elif self.DirectionY == "up":
                self.ypos -= self.ydir
            self.xpos -= self.xdir
            if self.dead == False:
                self.currentindexDuck += 1 
                if self.currentindexDuck == 6:
                    self.currentindexDuck = 3
            elif self.dead == True:
                self.currentindexDuck = 6 
        self.currentimageDuck = self.imagelistDuck[self.currentindexDuck]
    
    def moveUP(self, val):
        self.ydir += val
    
    def moveDown(self, val):
        self.ydir -= val
    
    def setDirectionX(self,dir):
        self.DirectionX = dir
        if self.DirectionX == "right":
            self.currentindexDuck = 0 
        else: 
            self.currentindexDuck = 4
    
    def setDirectionY(self,dir):
        self.DirectionY = dir
        
    def setImage(self,img):
        self.currentimageDuck = img
    
    def setPosition(self,x,y):
        self.xpos = x
        self.ypos = y 
    
    def reset(self):
        self.dead = False
        self.xpos = random.choice([0 - self.width, self.surfacewidth])
        self.ypos = random.randint(0,250)
        self.xdir = 8
        self.ydir = 8
        self.currentindexDuck = 0 

    
    def setX(self,x):
        self.xpos = x
    
    def setY(self,y):
        self.ypos = y 
    
class cursor:
    def __init__(self):
        self.xpos = 0
        self.ypos = 0 
        self.crosshairimage = pygame.image.load("images/cursor.png")
        self.width = self.crosshairimage.get_width()
        self.height = self.crosshairimage.get_height()
        
    def setX(self,x):
        self.xpos = x
    
    def setY(self,y):
        self.ypos = y
    
    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos
    
    def getDirections(self):
        return(self.xpos,self.ypos)
    
    def getcrosshairimg(self):
        return self.crosshairimage
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getBounds(self):
        return pygame.Rect(self.xpos,self.ypos,self.width,self.height)
    

