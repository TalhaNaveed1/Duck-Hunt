import pygame,random


class Dog:
    def __init__(self,surface):
        """Creates a dog (default) object for a surface that will move back on forth and react to certain circumstances

        Args:
            surface (Surface): Surface object in where we will draw the image on
        """        
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
        """Returns the speed the image is travelling at horizontally.

        Returns:
            int: The image's horizontal speed.
        """        
        return self.xspeed
    
    def getYspeed(self):
        """Returns the speed the image is travelling at vertically.

        Returns:
            int: The image's vertical speed.
        """        
        return self.yspeed
        
    def getBounds(self):
        """Returns the dimensions of the image inside of a rectangle

        Returns:
            pygame.rect: A rectangle with the dimensions of the image with the image inside. 
        """        
        return pygame.Rect(self.xpos,self.ypos,self.dogwidth,self.dogheight)
    
    def getDirection(self):
        """Returns the direction in where the image is moving towards

        Returns:
            str: The direction the image is moving towards
        """        
        return self.dogDirection
    
    def getHeight(self):
        """Returns the height of the image.

        Returns:
            int: The heigh of the image.
        """        
        return self.dogheight
    
    def getImage(self):
        """Returns the image of the dog (default) or the image the programmer chooses to use

        Returns:
            image: The image of the dog or the image the programmer chooses to use
        """        
        return self.currentimageDog
    
    def getWidth(self):
        """Returns the width of the image of the image.

        Returns:
            int: The width of the image of the image.
        """        
        return self.dogwidth
    
    def getX(self):
        """Returns the horizontal (x) position of the image

        Returns:
            int: The horizontal (x) position of the image
        """        
        return self.xpos
    
    def getY(self):
        """Returns the vertical (y) position of the image.

        Returns:
            int: The vertical (y) position of the image.
        """        
        return self.ypos
    
    def isHit(self):
        """Returns a boolean that states whether the image has been hit or not. 
        Returns:
            boolean: States whether the image has been hit or not. If True, the image has been hit, if false, the image has not been hit. 
        """       
        return self.dogHit
    
    def getLocation(self):
        """Returns a tuple containing the horizontal (x) and vertical (y) position of the image.

        Returns:
            tuple: Consists of the horizontal (x) and vertical (y) position of the image, respectively. 
        """        
        return (self.xpos,self.ypos)

    
    def reset(self):
        """Resets the image to it's default values if called on.
        """        
        self.dogHit = False
        self.xpos = random.choice([0, self.surfacewidth - self.dogwidth])
        self.ypos = 300
        self.xspeed = 8
        self.yspeed = 0 
        self.currentindexDog = 0 
        self.timer = 0 
        
    
    def move(self):
        """Moves the image back and forth along the surface object horizontally and calls on the reset function if the dogHit boolean is returned as True.
        """        
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
        """Sets the direction to where the image should face

        Args:
            dir (str): The direction to where the image should face ("left", "right")
        """        
        self.dogDirection = dir
        if self.dogDirection == "right":
            self.currentindexDog = 0 
        else: 
            self.currentindexDog = 4
    
    def setImage(self,img):
        """Sets the image

        Args:
            img (image): A image that this class will use
        """        
        self.currentimageDog = img
    
    def setLocation(self,x,y):
        """Sets the horizontal (x) and vertical (y) positions of the image

        Args:
            x (int): The horizontal position of the image
            y (int): The vertical position of the image
        """        
        self.xpos = x
        self.ypos = y
    
    def setX(self,x):
        """Sets the horizontal (x) position of the image

        Args:
            x (int): The horizontal position of the image
        """        
        self.xpos = x
    
    def setY(self,y):
        """Sets the vertical (y) position of the image

        Args:
            y (int): The vertical position of the image
        """        
        self.ypos = y
    
    def shootDog(self):
        """If this function was called change the boolean of dogHit and change the image index
        """        
        self.dogHit = True
        self.currentindexDog = 8
        
    def setXspeed(self,val):
        """Sets the horizontal speed the image will move at

        Args:
            val (int): The horizontal speed the image will move at 
        """        
        self.xspeed = val
    
    def setYspeed(self,val):
        """Sets the vertical speed the image will move at 

        Args:
            val (int): The vertical speed the image will move at 
        """        
        self.yspeed = val