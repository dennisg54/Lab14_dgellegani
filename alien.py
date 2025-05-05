
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """
    A class to represent a single alien in the fleet.
    
    Args:
        Sprite (): Inherits from the Sprite class in pygame.
    """
    
    def __init__(self, fleet: "AlienFleet", x: float, y: float) -> None:
        """
        Initialize the alien and set its starting position.
        
        Args:
            fleet (AlienFleet): class instance of the fleet to which the alien belongs.
            x (float): x-coordinate of the alien.
            y (float): y-coordinate of the alien.
        """
        super().__init__() # Call the parent class (Sprite) constructor
 
        self.fleet = fleet 
        self.screen = fleet.game.screen 
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings
        
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def update(self) -> None:
        """
        Update the position of the alien based on the fleet's direction and speed.
        """
        temp_speed = self.settings.fleet_speed
        
        self.x += temp_speed * self.fleet.fleet_direction       
        self.rect.x = self.x
        self.rect.y = self.y
        
    def check_edges(self) -> bool:
        """
        Check if the alien is at the edge of the screen.

        Returns:
            bool: True if the alien is at the edge of the screen, False otherwise.
        """
        return(self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left)
        
    def draw_alien(self) -> None:
        """
        Draw the alien on the screen at its current position.
        """
        
        self.screen.blit(self.image, self.rect)
        
