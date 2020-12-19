'''
- After choosing an image for the ship, we need to display it on the screen. 

- To use our ship, we’ll create a new ship module that will contain the class Ship.

- This class will manage most of the behavior of the player’s ship

- Pygame is efficient because it lets you treat all game elements like rectangles (rects), 
  even if they’re not exactly shaped like rectangles. 

- Treating an element as a rectangle is efficient because rectangles are simple geometric shapes. 

- When Pygame needs to figure out whether 2 game elements have collided, for example, 
  it can do this more quickly if it treats each object as a rectangle. 

- This approach usually works well enough that no one playing the game will notice that 
  we’re not working with the exact shape of each game element. 

- We’ll treat the ship and the screen as rectangles in this class
'''
import pygame

class Ship:
    def __init__(self, ai_game):
        """ initialize the ship & set its starting position """
        '''
        - The __init__() method of Ship takes 2 parameters: self & a reference to the current instance of the AlienInvasion class. 

        - This will give Ship access to all the game resources defined in AlienInvasion. 

        - At (1) we assign the screen to an attribute of Ship, so we can access it easily in all the methods in this class. 

        - At (2) we access the screen’s rect attribute using the get_rect() method and assign it to self.screen_rect 

        - Doing so allows us to place the ship in the correct location on the screen.

        - To load the image, we call pygame.image.load() (3) and give it the location of our ship image. 

        - This function returns a surface representing the ship, which we assign to self.image 

        - When the image is loaded, we call get_rect() to access the ship surface’s rect attribute so we can later use it to place the ship

        - We’ll position the ship at the bottom center of the screen. 

        - To do so, make the value of self.rect.midbottom match the midbottom attribute of the screen’s rect (4) 

        - Pygame uses these rect attributes to position the ship image so it’s centered horizontally and aligned with the bottom of the screen
        '''

        '''
        - When you’re working with a rect object, you can use the x- and y- coordinates of the top, bottom, left and right edges of the rectangle, 
          as well as the center, to place the object. 

        - You can set any of these values to establish the current position of the rect. 

        - When you’re centering a game element, work with the center, centerx or centery attributes of a rect. 

        - When you’re working at an edge of the screen, work with the top, bottom, left or right attributes. 

        - There are also attributes that combine these properties, such as midbottom, midtop, midleft and midright. 

        - When you’re adjusting the horizontal or vertical placement of the rect, you can just use the x and y attributes, 
          which are the x- and y- coordinates of its top-left corner. 

        - These attributes spare you from having to do calculations that game developers formerly had to do manually and you’ll use them often
        '''
        self.screen = ai_game.screen # (1)

        self.screen_rect = ai_game.screen.get_rect() # (2): access the screen surface’s rect attribute by calling get_rect()

        # load the image & access the ship surface’s rect attribute by calling get_rect() (3)
        self.image = pygame.image.load('D:/VS Code Programs/Python/PythonCrashCourse2ndEd/Projects/alien_invasion_pygame/images/ship.bmp')

        self.rect = self.image.get_rect() 

        # start each new ship at the bottom center of the screen by matching the value of self.rect.midbottom
        # with the midbottom attribute of the screen’s rect (4)
        self.rect.midbottom = self.screen_rect.midbottom

        # movement flag, set to False initially
        self.moving_right = False
        self.moving_left = False

        '''
        - We create a settings attribute for Ship, so we can use it in update()

        - Because we’re adjusting the position of the ship by fractions of a pixel, 
          we need to assign the position to a variable that can store a decimal value. 

        - You can use a decimal value to set an attribute of rect but the rect will only keep the integer portion of that value. 

        - To keep track of the ship’s position accurately, we define a new self.x attribute that can hold decimal values.

        - We use the float() function to convert the value of self.rect.x to a decimal and assign this value to self.x
        '''
        self.settings = ai_game.settings

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
    
    def blitme(self):
        """ this method draws the image to the screen at the position specified by self.rect """
        self.screen.blit(self.image, self.rect)
    
    def update(self):
      """ update the ship's position based on moving_right & moving_left """
      '''
      - In __init__(), we add a self.moving_left flag 
      
      - In update(), we use 2 separate if blocks rather than an elif to allow the ship’s rect.x value to be increased and 
        then decreased when both arrow keys are held down. 

      - This results in the ship standing still. 

      - If we used elif for motion to the left, the right arrow key would always have priority. 

      - Doing it this way makes the movements more accurate when switching from right to left 
        when the player might momentarily hold down both keys
      '''

      '''
      - Now when we change the ship’s position in update(), the value of self.x is adjusted by the amount stored in settings.ship_speed 

      - After self.x has been updated, we use the new value to update self.rect.x, which controls the position of the ship. 

      - Only the integer portion of self.x will be stored in self.rect.x but that’s fine for displaying the ship.

      - Now we can change the value of ship_speed and any value greater than 1 will make the ship move faster. 

      - This will help make the ship respond quickly enough to shoot down aliens and 
        it will let us change the tempo of the game as the player progresses in gameplay
      '''

      '''
      - At this point, the ship will disappear off either edge of the screen if you hold down an arrow key long enough. 

      - Let’s correct this so the ship stops moving when it reaches the screen’s edge. 

      - We do this by modifying the update() method in Ship

      - The new if conditions check the position of the ship before changing the value of self.x 

      - self.rect.right returns the x-coordinate of the right edge of the ship’s rect 

      - If this value is less than the value returned by self.screen_rect.right, the ship hasn’t reached the right edge of the screen.

      - The same goes for the left edge: if the value of the left side of the rect is greater than zero, 
        the ship hasn’t reached the left edge of the screen. 

      - This ensures the ship is within these bounds before adjusting the value of self.x

      - When you run alien_invasion.py now, the ship should stop moving at either edge of the screen. 
      '''
      if self.moving_right and self.rect.right < self.screen_rect.right:
        #self.rect.x += 1
        self.x += self.settings.ship_speed # update the ship's x value, not the rect
      
      if self.moving_left and self.rect.left > 0:
        #self.rect.x -= 1
        self.x -= self.settings.ship_speed
      
      self.rect.x = self.x # update the rect object from self.x