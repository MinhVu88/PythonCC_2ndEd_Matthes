'''
- The Bullet class inherits from Sprite, which we import from the pygame.sprite module 

- When you use sprites, you can group related elements in your game and act on all the grouped elements at once. 

- To create a bullet instance, __init__() needs the current instance of AlienInvasion and 
  we call super() to inherit properly from Sprite. 

- We also set attributes for the screen and settings objects and for the bullet’s color
'''
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired from the ship """
    def __init__(self, ai_game):
        """ Create a bullet object at the ship's current position """
        super().__init__()

        self.screen = ai_game.screen

        self.settings = ai_game.settings

        self.color = self.settings.bullet_color

        # create a bullet rect at (0, 0) & then set the correct position
        '''
        - We create the bullet’s rect attribute. 
        
        - The bullet isn’t based on an image, so we have to build a rect from scratch using the pygame.Rect() class

        - This class requires the x- and y-coordinates of the top-left corner of the rect and the width and height of the rect. 

        - We initialize the rect at (0, 0) but we’ll move it to the correct location in the next line because 
          the bullet’s position depends on the ship’s position. 

        - We get the width and height of the bullet from the values stored in self.settings
        '''
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        '''
        - We set the bullet’s midtop attribute to match the ship’s midtop attribute. 

        - This will make the bullet emerge from the top of the ship, making it look like the bullet is fired from the ship. 

        - We store a decimal value for the bullet’s y-coordinate so we can make fine adjustments to the bullet’s speed
        '''
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y) # store the bullet's vertical position as a decimal value

    def update(self):
        """ Move the bullet up the screen """
        '''
        - The update() method manages the bullet’s position. 
        
        - When a bullet is fired, it moves up the screen, which corresponds to a decreasing y-coordinate value. 

        - To update the position, we subtract the amount stored in settings.bullet_speed from self.y 

        - We then use the value of self.y to set the value of self.rect.y

        - The bullet_speed setting allows us to increase the speed of the bullets as the game progresses or 
          as needed to refine the game’s behavior. 

        - Once a bullet is fired, we never change the value of its x-coordinate, 
          so it will travel vertically in a straight line even if the ship moves
        '''
        # update the bullet's decimal position
        self.y -= self.settings.bullet_speed

        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the bullet to the screen """
        # The draw.rect() function fills the part of the screen defined by the bullet’s rect with the color stored in self.color    
        pygame.draw.rect(self.screen, self.color, self.rect)
