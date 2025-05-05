
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """
    Class to manage bullets fired by the ship.
    This class inherits from the Sprite class and is used to create bullet objects
    that can be fired by the ship in the game.
    The bullet will move upwards on the screen and will be removed when it goes off-screen.

    Args:
        Sprite (): The base class for all visible game objects in Pygame.
    """
    def __init__(self, game: "AlienInvasion") -> None:
        """
        Initialize the bullet and set its starting position.
        The bullet will be created at the ship's position and will move upwards on the screen.

        Args:
            game (AlienInvasion): The main game instance.   This will allow the bullet to access game settings and resources.            
        """
        super().__init__() 
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_w, self.settings.bullet_h))
        
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        
        self.y = float(self.rect.y)
        
    def update(self) -> None:
        """
        Update the position of the bullet.
        This method will be called in the game loop to ensure that the bullet moves upwards on the screen.
        The bullet's position will be updated based on the bullet speed defined in the game settings.
        The bullet will be removed from the arsenal if it goes off-screen.
        """
        # Move the bullet upwards
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        
    def draw_bullet(self) -> None:
        """
        Draw the bullet on the screen.
        This method will be called in the game loop to ensure that the bullet is drawn on the screen.
        The bullet will be drawn on the screen using the rect attribute to determine its position.
        """
        # Draw the bullet on the screen
        self.screen.blit(self.image, self.rect)
        
