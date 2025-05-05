
import pygame
import random
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    
class AlienFleet:
    """
    Class to manage the alien fleet in the game.
    This class is responsible for creating the fleet, updating its position,
    checking for collisions, and drawing the aliens on the screen.
    """
    def __init__(self, game: "AlienInvasion") -> None:
        """
        Initialize the alien fleet and set its attributes.
        This includes the fleet direction, drop speed, and the group of aliens.
        The fleet is created based on the screen size and alien size.

        Args:
            game (AlienInvasion): The main game instance.
        """
        # Initialize the alien fleet attributes
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed
        
        self.createFleet()
        
        
    def createFleet(self) -> None:
        """
        Create the alien fleet based on the screen size and alien size.
        The fleet is arranged in a rectangle, and the number of aliens is calculated
        based on the screen dimensions.
        """   
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h
        
        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)        
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)
        
        self._create_random_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)
        

    def _create_random_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """
        Create a rectangle fleet of aliens.
        The fleet is arranged in rows and columns, with a specified offset for positioning.
        
        Args:
            alien_w (int): width of the alien sprite
            alien_h (int): height of the alien sprite
            fleet_w (int): width of the fleet (number of aliens in a row)
            fleet_h (int): height of the fleet (number of aliens in a column)
            x_offset (int): offset for the x position of the fleet
            y_offset (int): offset for the y position of the fleet
        """
        spawn_chance = 5 # Chance of spawning an alien in a given position
        
        for row in range(fleet_h):
            for column in range(fleet_w):
                if random.randint(0,100) < spawn_chance:                    
                    current_x = x_offset + (column * alien_w)
                    current_y = y_offset + (row * alien_h)
                    self._create_alien(current_x, current_y)
                else:
                    continue
                

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        """
        Calculate the offsets for positioning the fleet on the screen.
        The offsets are calculated to center the fleet on the screen.

        Args:
            alien_w (int): width of the alien sprite
            alien_h (int): height of the alien sprite
            screen_w (int): width of the screen
            screen_h (int): height of the screen
            fleet_w (int): width of the fleet (number of aliens in a row)
            fleet_h (int): height of the fleet (number of aliens in a column)
        Returns:
            tuple: x_offset and y_offset for positioning the fleet     
        """
        half_screen = self.settings.screen_h // 2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w - fleet_horizontal_space) // 2)
        y_offset = int((half_screen - fleet_vertical_space) // 2)
        return x_offset,y_offset
            

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        """
        Calculate the size of the fleet based on the screen size and alien size.
        The fleet size is determined by the number of aliens that can fit in the screen dimensions.

        Args:
            alien_w (int): width of the alien sprite
            screen_w (int): width of the screen
            alien_h (int): height of the alien sprite
            screen_h (int): 

        Returns:
            tuple: width and height of the fleet (number of aliens in a row and column)
        """
        fleet_w = (screen_w // alien_w)
        fleet_h = ((screen_h / 2) // alien_h)
        
        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w += 2
            
        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h += 2
            
        return int(fleet_w), int(fleet_h)
    
        
    def _create_alien(self, current_x: int, current_y: int):
        """
        Create a new alien and add it to the fleet.
        The alien is positioned based on the current_x and current_y coordinates.

        Args:
            current_x (int): the x-coordinate for the alien's position
            current_y (int): the y-coordinate for the alien's position
        """
        new_alien = Alien(self, current_x, current_y)
        
        self.fleet.add(new_alien)
        
    
    def _check_fleet_edges(self) -> None:
        """
        Check if any alien in the fleet has reached the edge of the screen.
        If so, change the fleet's direction and drop the fleet down.
        """
        alien: "Alien"
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()                
                self.fleet_direction *= -1
                break
            
    def _drop_alien_fleet(self) -> None:
        """
        Drop the entire fleet down by a specified amount.
        This method is called when an alien reaches the edge of the screen.
        """
        alien: "Alien"
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed
            
            
                       
    def update_fleet(self) -> None:
        """
        Update the position of the fleet based on the fleet direction.
        If the fleet is moving to the right, move all aliens to the right.
        If the fleet is moving to the left, move all aliens to the left.
        """
        self._check_fleet_edges()
        self.fleet.update()
        
        
    def draw(self) -> None:
        """
        Draw the entire fleet of aliens on the screen.
        This method iterates through all aliens in the fleet and calls their draw method.
        """
        alien: "Alien"
        for alien in self.fleet:
            alien.draw_alien()
            
            
    def check_collisions(self, other_group) -> bool:
        """
        Check for collisions between the alien fleet and another group of sprites.
        This method uses pygame's sprite group collision detection to check for collisions.

        Args:
            other_group (pygame.sprite.Group): The other group of sprites to check for collisions with.

        Returns:
            bool: True if there are collisions, False otherwise.
        
        Args:
            other_group (container class): The other group of sprites to check for collisions with.

        Returns:
            bool: true if there are collisions, false otherwise.
        """
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)         
            
        
    def check_fleet_bottom(self) -> None:
        """
        Check if any alien in the fleet has reached the bottom of the screen.
        If so, return True to indicate that the fleet has reached the bottom.
        """
        alien: "Alien"
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False
    
    
    def check_destroyed_status(self) -> bool:
        """
        Check if the fleet is empty (all aliens are destroyed).
        This method is used to determine if the player has successfully destroyed all aliens.

        Returns:
            bool: True if the fleet is empty, False otherwise.
        """
        return not self.fleet
    