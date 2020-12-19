'''
- We’ll begin building the game by creating an empty Pygame window. 

- Later, we’ll draw the game elements, such as the ship & the aliens, on this window. 

- We’ll also make our game respond to user input, set the background color & load a ship image

- We’ll make an empty Pygame window by creating a class to represent the game
'''
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """ the overall class to manage game assets & behavior """
    def __init__(self):
        """ initialize the game & create game resources """
        '''
        - In the __init__() method, the pygame.init() function initializes the background settings that Pygame needs to work properly

        - We call pygame.display.set_mode() to create a display window, on which we’ll draw all the game’s graphical elements

        - The argument (self.settings.screen_width, self.settings.screen_height) is a tuple that defines the dimensions of the game window, 
          which will be 1200 pixels wide by 800 pixels high
        
        - We assign this display window to the attribute self.screen, so it will be available in all methods in the class

        - The object we assigned to self.screen is called a surface. 

        - A surface in Pygame is a part of the screen where a game element can be displayed. 

        - Each element in the game, like an alien or a ship, is its own surface. 

        - The surface returned by display.set_mode() represents the entire game window. 

        - When we activate the game’s animation loop, this surface will be redrawn on every pass through the loop, 
          so it can be updated with any changes triggered by user input
        '''
        pygame.init()

        self.settings = Settings() # create a Settings instance

        #self.screen = pygame.display.set_mode((1200, 800))

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption('Alien Invasion')

        #self.background_color = (230, 230, 230)

        '''
        - We import Ship and then make an instance of Ship after the screen has been created. 
        
        - The call to Ship() requires 1 argument: an instance of AlienInvasion. 

        - The self argument here refers to the current instance of AlienInvasion. 

        - This is the parameter that gives Ship access to the game’s resources, such as the screen object. 

        - We assign this Ship instance to self.ship

        - After filling the background, we draw the ship on the screen by calling ship.blitme() in run_game()
        '''
        self.ship = Ship(self)

        '''
        - Pygame has a fullscreen mode that you might like better than running the game in a regular window (optional)

        - When creating the screen surface, we pass a size of (0, 0) and the parameter pygame.FULLSCREEN 

        - This tells Pygame to figure out a window size that will fill the screen. 

        - Because we don’t know the width & height of the screen ahead of time, we update these settings after the screen is created

        - We use the width and height attributes of the screen’s rect to update the settings object

        - Make sure you can quit by pressing Q before running the game in fullscreen mode; 
          Pygame offers no default way to quit a game while in fullscreen mode
        '''
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        #self.settings.screen_width = self.screen.get_rect().width

        #self.settings.screen_height = self.screen.get_rect().height

        '''
        - Now that we have a Bullet class and the necessary settings defined, 
          we can write code to fire a bullet each time the player presses the spacebar. 

        - We’ll create a group in AlienInvasion to store all the live bullets 
          so we can manage the bullets that have already been fired. 

        - This group will be an instance of the pygame.sprite.Group class, 
          which behaves like a list with some extra functionality that’s helpful when building games. 

        - We’ll use this group to draw bullets to the screen on each pass through the main loop and to update each bullet’s position

        - Then we need to update the position of the bullets on each pass through the while loop in run_game()
        '''
        self.bullets = pygame.sprite.Group()

        '''
        - We want to create an instance of Alien so we can see the 1st alien on the screen. 

        - As part of our setup work, the code for this instance is at the end of __init__() in AlienInvasion. 

        - Eventually, we’ll create an entire fleet of aliens, which will be quite a bit of work, 
          so we’ll make a new helper method called _create_fleet()

        - The order of methods in a class doesn’t matter as long as there’s some consistency to how they’re placed. 

        - I’ll place _create_fleet() just before _update_screen() but anywhere in AlienInvasion will work. 

        - 1st, we’ll import the Alien class
        '''
        self.aliens = pygame.sprite.Group()
        self._create_fleet()        
    
    def run_game(self):
        """ start the game's main loop """
        '''
        - This method contains a while loop that runs continually. 

        - The while loop contains an event loop and code that manages screen updates. 

        - An event is an action that the user performs while playing the game, such as pressing a key or moving the mouse. 

        - To make our program respond to events, we write this event loop to listen for events and 
          perform appropriate tasks depending on the kinds of events that occur. 

        - The for loop is an event loop.

        - To access the events that Pygame detects, we’ll use the pygame.event.get() function. 

        - This function returns a list of events that have taken place since the last time this function was called. 

        - Any keyboard or mouse event will cause this for loop to run. 

        - Inside the loop, we’ll write a series of if statements to detect and respond to specific events. 

        - For example, when the player clicks the game window’s close button, a pygame.QUIT event is detected and we call sys.exit() to exit the game.

        - The call to pygame.display.flip() tells Pygame to make the most recently drawn screen visible. 

        - In this case, it simply draws an empty screen on each pass through the while loop, erasing the old screen so only the new screen is visible. 

        - When we move the game elements around, pygame.display.flip() continually updates the display to show the new positions of game elements and 
          hides the old ones, creating the illusion of smooth movement
        
        - We fill the screen with the background color using the fill() method, which acts on a surface and takes only 1 argument: a color
        '''
        while True:
            # for mouse & keyboard events
            '''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            '''
            self._check_events() # a helper method call using dot notation with self & the method name

            '''
            - The ship’s position will be updated after we’ve checked for keyboard events and before we update the screen. 

            - This allows the ship’s position to be updated in response to player input and 
              ensures the updated position will be used when drawing the ship to the screen
            '''
            self.ship.update()

            # When you call update() on a group, the group automatically calls update() for each sprite in the group
            # -> this line of code calls bullet.update() for each bullet we place in the bullets group
            #self.bullets.update()

            '''
            - At the moment, the bullets disappear when they reach the top but only 
              because Pygame can’t draw them above the top of the screen. 

            - The bullets actually continue to exist; their y-coordinate values just grow increasingly negative. 

            - This is a problem because they continue to consume memory and processing power.

            - We need to get rid of these old bullets or the game will slow down from doing so much unnecessary work. 

            - To do this, we need to detect when the bottom value of a bullet’s rect has a value of 0, 
              which indicates the bullet has passed off the top of the screen

            - When you use a for loop with a list (or a group in Pygame), 
              Python expects that the list will stay the same length as long as the loop is running.

            - As we can’t remove items from a list or group within a for loop, we have to loop over a copy of the group. 

            - We use the copy() method to set up the for loop, which enables us to modify bullets inside the loop. 

            - We check each bullet to see whether it has disappeared off the top of the screen. 

            - If it has, we remove it from bullets.             
            '''
            '''
            for bullet in self.bullets.copy():
              if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            '''
            '''
            - Finally we insert a print() call to show how many bullets currently exist in the game and 
              verify that they’re being deleted when they reach the top of the screen
            
            - If this code works correctly, we can watch the terminal output while firing bullets and 
              see that the number of bullets decreases to zero after each series of bullets has cleared the top of the screen. 

            - After you run the game and verify that bullets are being deleted properly, remove the print() call 

            - If you leave it in, the game will slow down significantly because it takes more time to 
              write output to the terminal than it does to draw graphics to the game window
            '''
            #print(len(self.bullets))

            # to keep run_game() well-organized, move the code that updates the bullets & removes the old ones to _update_bullets()
            self._update_bullets()    

            # update the position of each alien in the aliens group
            # We update the aliens’ positions after the bullets have been updated 
            # as we’ll soon be checking to see whether any bullets hit any aliens
            self._update_aliens() 
            
            '''
            # redraw the screen during each pass thru the loop
            #self.screen.fill(self.background_color)
            self.screen.fill(self.settings.background_color)

            self.ship.blitme()

            # make the most recently drawn screen visible
            pygame.display.flip()
            '''
            self._update_screen() # a helper method call

    '''
    - In large projects, you’ll often refactor code you’ve written before adding more code. 

    - Refactoring simplifies the structure of the code you’ve already written, making it easier to build on. 

    - In this section, we’ll break the run_game() method, which is getting lengthy, into 2 helper methods: _check_events() & _update_screen() 

    - A helper method does work inside a class but isn’t meant to be called through an instance. 

    - In Python, a single leading underscore indicates a helper method

    - If you’ve already built a number of games, you’ll probably start out by breaking your code into methods like these. 

    - But if you’ve never tackled a project like this, you probably won’t know how to structure your code. 

    - This approach of writing code that works & then restructuring it as it grows more complex gives you an idea of a realistic development process: 
      you start out writing your code as simply as possible and then refactor it as your project becomes more complex
    '''
    def _check_events(self):
        '''
        - Moving the code that manages events to _check_events() simplifies run_game() & isolates the event management loop. 
        
        - Isolating the event loop allows you to manage events separately from other aspects of the game, such as updating the screen
        '''

        ''' elif event.type == pygame.KEYDOWN ->

        - we’ll give the player the ability to move the ship right and left. 
            
        - We’ll write code that responds when the player presses the right or left arrow key.

        - We’ll focus on movement to the right 1st and then we’ll apply the same principles to control movement to the left

        - Whenever the player presses a key, that keypress is registered in Pygame as an event. 

        - Each event is picked up by the pygame.event.get() method. 

        - We need to specify in our _check_events() method what kind of events we want the game to check for. 

        - Each keypress is registered as a KEYDOWN event.

        - When Pygame detects a KEYDOWN event, we need to check whether the key that was pressed is one that triggers a certain action. 

        - For example, if the player presses the right arrow key, we want to increase the ship’s rect.x value to move the ship to the right
        '''

        ''' elif event.type == pygame.KEYUP ->

        - When the player holds down the right arrow key, we want the ship to continue moving right until the player releases the key. 

        - We’ll have the game detect a pygame.KEYUP event so we’ll know when the right arrow key is released; 
          then we’ll use the KEYDOWN and KEYUP events together with a flag called moving_right to implement continuous motion.

        - When the moving_right flag is False, the ship will be motionless. 

        - When the player presses the right arrow key, we’ll set the flag to True and 
          when the player releases the key, we’ll set the flag to False again.

        - The Ship class in ship.py controls all attributes of the ship, so we’ll give it an attribute called moving_right and 
          an update() method to check the status of the moving_right flag. 

        - The update() method will change the position of the ship if the flag is set to True. 

        - We’ll call this method once on each pass through the while loop to update the position of the ship

        - The new elif block responds to KEYUP events. 

        - When the player releases the right arrow key (K_RIGHT), we set moving_right to False
        '''

        ''' elif event.key == pygame.K_LEFT ->

        - Now that the ship can move continuously to the right, adding movement to the left is straightforward. 
        
        - Again, we’ll modify the Ship class and the _check_events() method

        - If a KEYDOWN event occurs for the K_LEFT key, we set moving_left to True. 
        
        - If a KEYUP event occurs for the K_LEFT key, we set moving_left to False. 

        - We can use elif blocks here because each event is connected to only 1 key. 

        - If the player presses both keys at once, 2 separate events will be detected.

        - When you run alien_invasion.py now, you should be able to move the ship continuously to the right and left. 

        - If you hold down both keys, the ship should stop moving
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              sys.exit()  
            elif event.type == pygame.KEYDOWN:
              '''
              if event.key == pygame.K_RIGHT:
                #self.ship.rect.x += 1

                # how the game responds when the right arrow key's pressed: 
                # instead of changing the ship’s position directly, moving_right's set to True
                self.ship.moving_right = True
              elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
              '''
              self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
              '''
              if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
              elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False
              '''
              self._check_keyup_events(event)               
    
    '''
    - The _check_events() method will increase in length as we continue to develop the game, 
      so let’s break _check_events() into 2 new helper methods: one that handles KEYDOWN events & another that handles KEYUP events

    - Each needs a self parameter and an event parameter. 

    - The bodies of these 2 methods are copied from _check_events() & we’ve replaced the old code with calls to the new methods
    '''
    def _check_keydown_events(self, event):
      if event.key == pygame.K_RIGHT:
        self.ship.moving_right = True
      elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True
      elif event.key == pygame.K_q:
        # a keyboard shortcut to end the game when the player presses Q, instead of using cursor to close the game window
        sys.exit()
      elif event.key == pygame.K_SPACE:
        # modify _check_keydown_events() to fire a bullet when the player presses the spacebar
        # leave _check_keyup_events() unchanged as nothing happens when the spacebar is released
        # modify _update_screen() to make sure each bullet is drawn to the screen before calling flip()
        # write a new method called _fire_bullet() to handle this work
        self._fire_bullet()

    def _check_keyup_events(self, event):
      if event.key == pygame.K_RIGHT:
        self.ship.moving_right = False
      elif event.key == pygame.K_LEFT:
        self.ship.moving_left = False

    def _fire_bullet(self):
      """ Create a new bullet and add it to the bullets group """
      '''
      - In this method, we make an instance of Bullet and call it new_bullet 

      - We then add it to the group bullets using the add() method 

      - The add() method is similar to append() but it’s a method that’s written specifically for Pygame groups

      - When the player presses the spacebar, we check the length of bullets. 
      
      - If len(self.bullets) is less than 3, we create a new bullet. 

      - But if 3 bullets are already active, nothing happens when the spacebar is pressed. 

      - When you run the game now, you should be able to fire bullets only in groups of 3
      '''
      if len(self.bullets) < self.settings.bullets_allowed:
        new_bullet = Bullet(self)

        self.bullets.add(new_bullet)

    def _update_bullets(self):
      """ Update position of bullets and get rid of old bullets """
      self.bullets.update()

      for bullet in self.bullets.copy():
        if bullet.rect.bottom <= 0:
          self.bullets.remove(bullet)

    def _create_fleet(self):
      """ Create the fleet of aliens """
      '''
      - To draw a fleet, we need to figure out how many aliens can fit across the screen and 
        how many rows of aliens can fit down the screen. 

      - We’ll 1st figure out the horizontal spacing between aliens and create a row; 
        then we’ll determine the vertical spacing and create an entire fleet

      - To figure out how many aliens fit in a row, let’s look at how much horizontal space we have. 

      - The screen width is stored in settings.screen_width but we need an empty margin on either side of the screen. 

      - We’ll make this margin the width of 1 alien. 

      - Because we have 2 margins, the available space for aliens is the screen width minus 2 alien widths: 
        available_space_x = settings.screen_width – (2 * alien_width)

      - We also need to make the spacing between aliens 1 alien width. 

      - The space needed to display 1 alien is twice its width: 
        1 width for the alien & 1 width for the empty space to its right (alien_width & spacing_bw_aliens) 

      - To find the number of aliens that fit across the screen, we divide the available space by 2 times the width of an alien. 

      - We use floor division (//), which divides 2 numbers & drops any remainder, so we’ll get an integer number of aliens: 
        number_aliens_x = available_space_x // (alien_width + spacing_bw_aliens)

      - We’ll use these calculations when we create the fleet
      '''

      '''
      - To finish the fleet, we’ll determine the number of rows that fit on the screen and then 
        repeat the loop for creating the aliens in 1 row until we have the correct number of rows. 

      - To determine the number of rows, we find the available vertical space by subtracting the alien height from the top, 
        the ship height from the bottom & 2 alien heights from the bottom of the screen: 
        
        =>  available_space_y = settings.screen_height – (3 * alien_height) – ship_height

      - The result will create some empty space above the ship, 
        so the player has some time to start shooting aliens at the beginning of each level.

      - Each row needs some empty space below it, which is equal to the height of 1 alien. 

      - To find the number of rows, we divide the available vertical space by 2 times the height of an alien. 

      - We use floor division because we can only make an integer number of rows 
        (Again, if these calculations are off, we’ll see it right away & adjust our approach until we have reasonable spacing)

        =>  number_rows = available_height_y // (2 * alien_height)

      - Now that we know how many rows fit in a fleet, we can repeat the code for creating a row
      '''
      # an Alien instance is created & placed in the default upper-left area of the screen
      # but it isn't part of the fleet at this point, so it's not added to the aliens group yet
      alien = Alien(self) 

      #self.aliens.add(alien)

      #alien_width = alien.rect.width # 1 horizontal space

      # the size attribute contains a tuple with the width & height (1 vertical space) of a rect object
      alien_width, alien_height = alien.rect.size 

      empty_space = alien_width

      available_space_x = self.settings.screen_width - (alien_width * 2)

      alien_space = alien_width + empty_space

      alien_quantity_x = available_space_x // alien_space

      # determine the number of rows of aliens that fit on the screen
      ship_height = self.ship.rect.height

      available_space_y = self.settings.screen_height - (alien_height * 3) - ship_height

      rows_of_aliens = available_space_y // (alien_height * 2)

      # checking the attributes' values
      print(f'\n\tscreen_width: {self.settings.screen_width} | screen_height: {self.settings.screen_height}')

      print(f'\n\talien.rect.size: {alien.rect.size} | alien_width: {alien_width} | alien_height: {alien_height} | ship_height: {ship_height}')

      print(f'\n\tempty_space: {empty_space} | alien_space: {alien_space} | alien_quantity_x: {alien_quantity_x} | rows_of_aliens: {rows_of_aliens}')

      print(f'\n\tavailable_space_x: {available_space_x} | available_space_y: {available_space_y}\n')

      '''
      - we set up a loop that counts from 0 to the number of aliens we need to make. 

      - In the loop's main body, we create a new alien & then set its x-coordinate value to place it in the row. 

      - Each alien is pushed to the right 1 alien width from the left margin. 

      - Next, we multiply the alien width by 2 to account for the space each alien takes up, 
        including the empty space to its right & we multiply this amount by the alien’s position in the row. 

      - We use the alien’s x attribute to set the position of its rect. 

      - Then we add each new alien to the group aliens.

      - When you run Alien Invasion now, you should see the 1st row of aliens appear

      - The 1st row is offset to the left, which is actually good for gameplay.

      - The reason is that we want the fleet to move right until it hits the edge of the screen, 
        then drop down a bit, then move left & so forth. 

      - Like the classic game Space Invaders, this movement is more interesting than having the fleet drop straight down. 

      - We’ll continue this motion until all aliens are shot down or until an alien hits the ship or the bottom of the screen
      '''

      '''
      - To create multiple rows, we use 2 nested loops: 1 outer and 1 inner loop. 

      - The inner loop creates the aliens in 1 row. 

      - The outer loop counts from 0 to the number of rows we want; 
        Python uses the code for making a single row and repeats it specific number of times

      - Now when we call _create_alien(), we include an argument for the row position (1st, 2nd, 3rd, etc) 
        so each row can be placed farther down the screen.

      - The definition of _create_alien() needs a parameter to hold the row position. 
      '''
      # the outer loop creates a specific number of rows of aliens
      for row_position in range(rows_of_aliens):
        # the inner loop creates a specific number of aliens per row
        for alien_position in range(alien_quantity_x):
          '''
          et = Alien(self)

          # 1 horizontal space + (2 horizontal spaces * 0....8) => 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17
          # 60 + (120 * 0....8) => 60 | 180 | 300 | 420 | 540 | 660 | 780 | 900 |1020
          et.x = alien_width + (alien_space * alien_position) 

          et.rect.x = et.x

          self.aliens.add(et)
          '''
          self._create_alien(alien_position, row_position) # create the rows & aliens

    def _create_alien(self, alien_position, row_number):
      """ Create an alien and place it in the row """
      alien = Alien(self)

      #alien_width = alien.rect.width # get an alien's width inside the method instead of passing it as an argument

      alien_width, alien_height = alien.rect.size

      # 1 horizontal space + 2 horizontal spaces * (0....8) => 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17
      # 60 + 120 * (0....8) => 60 | 180 | 300 | 420 | 540 | 660 | 780 | 900 |1020
      alien.x = alien_width + 2 * alien_width * alien_position

      alien.rect.x = alien.x

      '''
      - Here we change an alien’s y-coordinate value when it’s not in the 1st row 
        by starting with 1 alien’s height to create empty space at the top of the screen. 

      - Each row (except the 1st row) starts 2 alien heights below the previous row, 
        so we multiply the alien height by 2 & then by the row position. 

      - The 1st row number is 0, so the vertical placement of the 1st row is unchanged. 

      - All subsequent rows are placed farther down the screen
      '''
      # 1 vertical space + 2 vertical spaces * (0...3) => 1 | 3 | 5 | 7
      # 58 + 2 * 58 * (0....3) => 58 | 174 | 290 | 406
      alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

      self.aliens.add(alien) # add the alien instance to the aliens group/fleet

      # checking the attributes' values
      print('\t----------------------------------------------------------------')

      print(f'\n\talien.rect.x: {alien.rect.x} | alien.rect.y: {alien.rect.y} | alien.rect.height: {alien.rect.height}\n')

    def _check_fleet_edges(self):
      " Respond appropriately if any aliens have reached an edge "
      '''
      - When an alien reaches the edge, the entire fleet needs to drop down and change direction. 

      - So AlienInvasion is where we’ll add code to check if any aliens are at the left or right edge. 

      - This's done by writing _check_fleet_edges() & _change_fleet_direction() & then modifying _update_aliens()

      - In this method, we loop through the fleet and call check_edges() on each alien. 

      - If check_edges() returns True, an alien is at an edge and the whole fleet needs to drop down & change direction; 
        so we call _change_fleet_direction() and break out of the if statement. 
      '''
      for alien in self.aliens.sprites():
        if alien.check_edges():
          self._change_fleet_direction()

          break

    def _change_fleet_direction(self):
      " Drop the entire fleet and change the fleet's direction "
      '''
      - In this method, we loop thru all the aliens and drop each one using the fleet_drop_speed setting, 
        then we change the value of fleet_direction by multiplying its current value by –1. 

      - The line that changes the fleet’s direction isn’t part of the for loop. 

      - We want to change every alien’s vertical position but the fleet's direction is changed just once
      '''     
      for alien in self.aliens.sprites():
        alien.rect.y += self.settings.fleet_drop_speed

      # fleet_direction's initial value in settings.py is 1 => the fleet at 1st moves towards the right edge
      # when it reaches the right edge & drops down, fleet_direction's value * -1 = -1 => now the fleet moves towards the left edge
      # when it reaches the left edge & drops down, fleet_direction's value * -1 => -1 * -1 = 1 => the fleet once again moves towards the right edge
      # and so on
      self.settings.fleet_direction *= -1

      # checking the attribute' values
      print(f'\n\tself.settings.fleet_direction: {self.settings.fleet_direction}')  

    def _update_aliens(self):
      " Update the positions of all aliens in the fleet, if the fleet is at an edge "
      '''
      - Using update() on the aliens group calls each alien’s update(), which is defined in alien.py 

      - When you run alien_invasion.py now, you should see the fleet move right and disappear off the side of the screen
      '''

      '''
      - We’ve modified the method by calling _check_fleet_edges() before updating each alien’s position.

      - When you run the game now, the fleet should move back and forth between the screen's edges and 
        drop down every time it hits an edge.

      - Now we can start shooting down aliens and watch for any aliens that hit the ship or reach the bottom of the screen
      '''
      self._check_fleet_edges()

      self.aliens.update()

    def _update_screen(self):
        '''
        - We moved the code that draws the background, the ship & flips the screen to _update_screen(). 

        - Now the body of the main loop in run_game() is much simpler. 

        - It’s easy to see that we’re looking for new events and updating the screen on each pass through the loop
        '''
        self.screen.fill(self.settings.background_color)

        self.ship.blitme()

        # The bullets.sprites() method returns a list of all sprites in the bullets group
        # To draw all fired bullets to the screen, loop thru the sprites in bullets & call draw_bullet() on each one
        for bullet in self.bullets.sprites():
          bullet.draw_bullet()

        '''
        - To make the alien appear, the aliens group’s draw() method is called

        - When you call draw() on a group, Pygame draws each element in the group at the position defined by its rect attribute. 

        - draw() requires 1 argument: a surface on which the elements from the group are drawn
        '''
        self.aliens.draw(self.screen)

        pygame.display.flip()

'''
- At the end of the file, we create an instance of the game and then call run_game(). 

- We place run_game() in an if block that only runs if the file is called directly. 

- When you run this alien_invasion.py file, you should see an empty Pygame window
'''
if __name__ == '__main__':
    # make a game instance & run the game
    ai = AlienInvasion()

    ai.run_game()

