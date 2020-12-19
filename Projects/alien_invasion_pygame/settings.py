'''
- Each time we introduce new functionality into the game, we’ll typically create some new settings as well. 

- Instead of adding settings throughout the code, let’s write a module called settings that 
  contains a class called Settings to store all these values in 1 place. 

- This approach allows us to work with just 1 settings object any time we need to access an individual setting. 

- This also makes it easier to modify the game’s appearance and behavior as our project grows: 
  to modify the game, we’ll simply change some values in settings.py, which we’ll create next, 
  instead of searching for different settings throughout the project
'''
class Settings:
    """ a class to store the game's settings """
    def __init__(self):
        """ initialize the settings """
        # screen settings
        self.screen_width = 1200

        self.screen_height = 800

        self.background_color = (230, 230, 230) # RGB colors

        '''
        - Currently, the ship moves 1 pixel per cycle through the while loop in alien_invasion.py but 
          we can take finer control over its speed by adding the ship_speed attribute here. 

        - We’ll use this attribute to determine how far to move the ship on each pass through the loop

        - We set the initial value of ship_speed to 1.5 

        - When the ship moves now, its position is adjusted by 1.5 pixels rather than 1 pixel on each pass through the loop.

        - We’re using decimal values for the speed setting to give us finer control of the ship’s speed 
          when we increase the tempo of the game later on.

        - However, rect attributes such as x store only integer values, so we need to make some modifications to Ship in ship.py
        '''
        self.ship_speed = 1.5

        # bullet settings
        self.bullet_speed = 1.0

        self.bullet_width = 3

        self.bullet_height = 15

        self.bullet_color = (60, 60, 60)

        '''
        - Many shooting games limit the number of bullets a player can have on the screen at 1 time
        
        - Doing so encourages players to shoot accurately
        
        - This limits the player to 3 bullets at a time. 
        
        - Use this setting in AlienInvasion to check how many bullets exist before creating a new bullet in _fire_bullet()
        '''
        self.bullets_allowed = 3

        '''
        - Let’s make the fleet of aliens move to the right across the screen until it hits the edge and 
          then make it drop a set amount and move in the other direction. 

        - We’ll continue this movement until all aliens have been shot down, 1 collides with the ship or 
          1 reaches the bottom of the screen.

        - Let’s begin by making the fleet move to the right

        - To move the aliens, we’ll use the update() method in alien.py, which is called for each alien in the aliens group. 

        - 1st, add a setting to control the speed of each alien
        '''
        # alien settings
        self.alien_speed = 1.0

        '''
        - Now we’ll create the settings that will make the fleet move down the screen & 
          to the left when it hits the right edge of the screen

        - fleet_drop_speed controls how quickly the fleet drops down the screen each time an alien reaches either edge. 

        - It’s helpful to separate this speed from the aliens’ horizontal speed so you can adjust the 2 speeds independently.

        - To implement fleet_direction, we could use a text value like 'left' or 'right' 
          but we’d end up with if-elif statements testing for the fleet direction. 

        - Instead, as we have only 2 directions to deal with, let’s use the values 1 and –1 and 
          switch between them each time the fleet changes direction 
        
        - Using numbers also makes sense because moving right involves adding to each alien’s x-coordinate value and 
          moving left involves subtracting from each alien’s x-coordinate value
        '''
        # fleet settings
        self.fleet_drop_speed = 10

        self.fleet_direction = 1 # each alien’s x-coordinate value: 1 = right | -1 = left



















