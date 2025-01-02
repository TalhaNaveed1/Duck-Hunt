import pygame, random

class Duck:
    def __init__(self,surface):
        """Creats a duck (default) object for a surface that will move up,down,left and right and react to certain circumstances. 

        Args:
            surface (Surface): A surface in where we will draw the duck (default) object on. 
        """        
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
        """Returns a rectangle with the dimensions of the image consisting of the image inside as well. 

        Returns:
            pygame.Rect: A rectangle that has the dimensions of the image consisting of the image inside as well. 
        """        
        return pygame.Rect(self.xpos,self.ypos,self.width,self.height)

    def getDirectionX(self):
        """Returns the speed the image is travelling at horizontally (x)

        Returns:
            int: The horizontal (x) speed of the image
        """        
        return self.DirectionX
    
    def getDirectionY(self):
        """Returns the speed of the image vertically (y)

        Returns:
            int: The vertical (y) speed of the image
        """        
        return self.DirectionY
    
    def getHeight(self):
        """Returns the height of the image

        Returns:
            int: The height of the image
        """        
        return self.height
    
    def getWidth(self):
        """Returns the width of the image

        Returns:
            int: The width of the image
        """        
        return self.width
    
    def getX(self):
        """Returns the horizontal (x) position of the image

        Returns:
            int: The horizontal (x) position of the image
        """        
        return self.xpos
    
    def getY(self):
        """Returns the vertical (y) position of the image

        Returns:
            int: The vertical (y) position of the image
        """        
        return self.ypos

    def getLocation(self):
        """Returns the horizontal (x) and vertical (y) positions of the image as a tuple
        
        Returns: 
            tuple: The horizontal (x) and vertical (y) positions of the image, respectively
        """           
        return(self.xpos,self.ypos)
    
    def getImage(self):
        """Returns the image that is being used.

        Returns:
            image: Returns the image that is currenlty being used. 
        """        
        return self.currentimageDuck
    
    def isDead(self):
        """Returns a boolean stating whether the image was hit or not by the curosr. 

        Returns:
            boolean: A boolean stating whether the image was hit or not. If true, the image was hit, if false, the image was not hit. 
        """        
        return self.dead
    
    def killDuck(self):
        """Sets the values to certain information if the image was hit by the cursor. 
        """        
        self.dead = True
        self.currentimageDuck = self.imagelistDuck[6]
        if self.ypos <= 300:
            self.ydir = 10
            self.xdir = 0 

    def move(self):
        """Moves the image along the surface up, down, left, and right according to where it is located. 
        """        
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
        """Moves the image vertically (y) up

        Args:
            val (int): The value that the image will move up by
        """        
        self.ydir += val
    
    def moveDown(self, val):
        """Moves the image vertically (y) down

        Args:
            val (int): The value that the image will move down by 
        """        
        self.ydir -= val
    
    def setDirectionX(self,dir):
        """Sets the direction horizontally (x) the image will move towards

        Args:
            dir (str): The direction the image is moving towards. If "right", the image is moving right, or else it is considered to be moving left. 
        """        
        self.DirectionX = dir
        if self.DirectionX == "right":
            self.currentindexDuck = 0 
        else: 
            self.currentindexDuck = 4
    
    def setDirectionY(self,dir):
        """Sets the direction vertically (y) the image will move towards

        Args:
            dir (str): The direction the image is travelling towards. If "down", the image is moving down, if "up" the image is moving up . 
        """        
        self.DirectionY = dir
        
    def setImage(self,img):
        """Sets the image this class will utiilize

        Args:
            img (image): The image that this class will use
        """        
        self.currentimageDuck = img
    
    def setPosition(self,x,y):
        """Sets the horizontal (x) and vertical (y) position of the image

        Args:
            x (int): The horizontal (x) position of the image
            y (int): The vertical (y) position of the image
        """        
        self.xpos = x
        self.ypos = y 
    
    def reset(self):
        """Resets the image and certain values to it's default settings if called on 
        """        
        self.dead = False
        self.xpos = random.choice([0 - self.width, self.surfacewidth])
        self.ypos = random.randint(0,250)
        self.xdir = 8
        self.ydir = 8
        self.currentindexDuck = 0 

    
    def setX(self,x):
        """Set the horizontal (x) position of the image

        Args:
            x (int): The horizontal (x) position of the image
        """        
        self.xpos = x
    
    def setY(self,y):
        """Set the vertical (y) position of the image

        Args:
            y (int): The vertical (y) position of the image
        """        
        self.ypos = y 
    
class cursor:
    def __init__(self):
        """Creates a cursor object that becomes the cursor (default) and acts as the cursor on any surface.
        """        
        self.xpos = 0
        self.ypos = 0 
        self.crosshairimage = pygame.image.load("images/cursor.png")
        self.width = self.crosshairimage.get_width()
        self.height = self.crosshairimage.get_height()
        
    def setX(self,x):
        """Sets the horizontal (x) position of the image

        Args:
            x (int): The horizontal (x) position of the image
        """        
        self.xpos = x
    
    def setY(self,y):
        """Sets the vertical (y) position of the image

        Args:
            y (int): The vertical (y) position of the image
        """        
        self.ypos = y
    
    def getX(self):
        """Returns the horizontal (x) position of the image

        Returns:
            int: The horizontal (x) position of the image
        """        
        return self.xpos

    def getY(self):
        """Returns the vertical (y) position of the image

        Returns:
            int: The vertical (y) position of the image
        """        
        return self.ypos
    
    def getDirections(self):
        """Returns the horizontal (x) and vertical (y) positions of the image as a tuple
        
        Returns: 
            tuple: A tuple consisting of the horizontal (x) and vertical (y) position of the image, respictely 
        """        
        return(self.xpos,self.ypos)
    
    def getcrosshairimg(self):
        """Returns the image 

        Returns:
            image: Returns the image the class utilizes 
        """        
        return self.crosshairimage
    
    def getWidth(self):
        """Returns the width of the image

        Returns:
            int: The width of the image the class is utilizing
        """        
        return self.width
    
    def getHeight(self):
        """Returns the height of the image

        Returns:
            int: The height of the image the class is utilzing 
        """        
        return self.height
    
    def getBounds(self):
        """Returns a rectangle with the dimensions of the image consisting of the image inside as well

        Returns:
            pygame.Rect: A rectangle with the dimensions of the image consisting of the image inside as well
        """        
        return pygame.Rect(self.xpos,self.ypos,self.width,self.height)
    

