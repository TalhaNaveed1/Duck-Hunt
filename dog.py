import pygame,random


class Dog:
    def __init__(self,surface):
        self.timer = 0 
        self.currentindexDog = 0
        self.dogDirection = "right"
        self.dogHit = False
        self.imagelistDog = []
        for counter2 in range(4):
            self.imagelistDog.append(pygame.image.load("images/dogEast" + str(counter2) + ".png"))
        for counter3 in range(4):
            self.imagelistDog.append(pygame.image.load("images/dogWest" + str(counter3) + ".png"))
        for counter4 in range(2):
            self.imagelistDog.append(pygame.image.load("images/laughing_dog" + str(counter4) + ".png"))
        self.surfacewidth = surface.get_width()
        self.currentimageDog = self.imagelistDog[self.currentindexDog]
        self.dogwidth = self.currentimageDog.get_width()
        self.dogheight = self.currentimageDog.get_height()
        self.xpos = random.choice([0, surface.get_width() - self.dogwidth])
        self.ypos = 300
        self.xspeed = 8
        self.yspeed = 0 
        
    def getXspeed(self):
        return self.xspeed
    
    def getYspeed(self):
        return self.yspeed
        
    def getBounds(self):
        return pygame.Rect(self.xpos,self.ypos,self.dogwidth,self.dogheight)
    
    def getDirection(self):
        return self.dogDirection
    
    def getHeight(self):
        return self.dogheight
    
    def getImage(self):
        return self.currentimageDog
    
    def getWidth(self):
        return self.dogwidth
    
    def getX(self):
        return self.xpos
    
    def getY(self):
        return self.ypos
    
    def isHit(self):
        return self.dogHit
    
    def getLocation(self):
        return (self.xpos,self.ypos)

    
    def reset(self):
        self.dogHit = False
        self.xpos = random.choice([0, self.surfacewidth - self.dogwidth])
        self.ypos = 300
        self.xspeed = 8
        self.yspeed = 0 
        self.currentindexDog = 0 
        self.timer = 0 
        
    
    def move(self):
        if self.dogDirection == "right" and self.dogHit == False:
            self.xpos += self.xspeed
            self.currentindexDog += 1 
            if self.currentindexDog == 4:
                self.currentindexDog = 0
        elif self.dogDirection == "left" and self.dogHit == False: 
            self.xpos -= self.xspeed
            self.currentindexDog += 1 
            if self.currentindexDog == 8:
                self.currentindexDog = 4 
        elif self.dogHit == True:
            self.ypos = 270
            self.currentindexDog += 1 
            if self.currentindexDog == 10:
                self.currentindexDog = 8 
            self.timer += 1 
            if self.timer == 50:
                self.reset()
        self.currentimageDog = self.imagelistDog[self.currentindexDog]

    

    
    def setDirection(self, dir):
        self.dogDirection = dir
        if self.dogDirection == "right":
            self.currentindexDog = 0 
        else: 
            self.currentindexDog = 4
    
    def setImage(self,img):
        self.currentimageDog = img
    
    def setLocation(self,x,y):
        self.xpos = x
        self.ypos = y
    
    def setX(self,x):
        self.xpos = x
    
    def setY(self,y):
        self.ypos = y
    
    def shootDog(self):
        self.dogHit = True
        self.currentindexDog = 8
        
    def setXspeed(self,val):
        self.xspeed = val
    
    def setYspeed(self,val):
        self.yspeed = val