''' Reviewing the Project so far:

- Examine our code and determine if we need to refactor before implementing new features.

- Add a single alien to the top-left corner of the screen with appropriate spacing around it.

- Use the spacing around the 1st alien and the overall screen size to determine how many aliens can fit on the screen. 
  We’ll write a loop to create aliens to fill the upper portion of the screen.

- Make the fleet move sideways and down until the entire fleet is shot down, an alien hits the ship or reaches the ground. 
  If the entire fleet is shot down, we’ll create a new fleet. 
  If an alien hits the ship or the ground, we’ll destroy the ship and create a new fleet.

- Limit the number of ships the player can use and end the game when the player has used up the allotted number of ships
'''
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class to represent a single alien in the fleet """
    '''
    - This class doesn’t need a method for drawing the alien to the screen

    - Instead, we’ll use a Pygame group method, draw(), that automatically draws all the elements of a group to the screen
    '''
    def __init__(self, ai_game):
        """ Initialize the alien and set its starting position """
        super().__init__()

        self.screen = ai_game.screen

        # load the alien image & access the alien surface’s rect attribute by calling get_rect()
        self.image = pygame.image.load('D:/VS Code Programs/Python/PythonCrashCourse2ndEd/Projects/alien_invasion_pygame/images/alien.bmp')

        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        # add a space to its left that's equal to its width & a space above it equal to its height
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact horizontal position as its horizontal speed is the main concern
        self.x = float(self.rect.x)

        self.settings = ai_game.settings

    def check_edges(self):
        " Return True if an alien is at either edge of the screen "
        '''
        - We need a method to check whether an alien is at either edge and we need to modify update() to 
          allow each alien to move in the appropriate direction

        - We can call check_edges() on any alien to see whether it’s at the left or right edge. 

        - The alien is at the right edge if the right attribute of its rect is greater than or 
          equal to the right attribute of the screen’s rect. 

        - It’s at the left edge if its left value is less than or equal to 0
        '''
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        " Move the alien to the right of left "
        '''
        - A settings attribute is created in __init__() so we can access the alien’s speed in this method. 

        - Each time we update an alien’s position, we move it to the right by the amount stored in settings.alien_speed 

        - We track the alien’s exact position with the self.x attribute, which can hold decimal values. 

        - We then use the value of self.x to update the position of the alien’s rect

        - We modify update() to allow motion to the left or right by multiplying the alien’s speed by the value of fleet_direction 

        - If fleet_direction is 1, the value of alien_speed will be added to the alien’s current position, moving the alien to the right; 
          if fleet_direction is –1, the value will be subtracted from the alien’s position, moving the alien to the left
        '''
        #self.x += self.settings.alien_speed

        self.x += self.settings.alien_speed * self.settings.fleet_direction

        self.rect.x = self.x