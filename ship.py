
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import ShipArsenal      

class Ship:
    """
    Class to manage the ship in the game.
    This class is responsible for the ship's position, movement, and firing bullets.
    """
    def __init__ (self, game: "AlienInvasion", arsenal: "ShipArsenal") -> None:
        """
        Initialize the ship and set its starting position.
        The ship will be created at the bottom center of the screen.

        Args:
            game (AlienInvasion): the main game instance. This will allow the ship to access game settings and resources.
            arsenal (ShipArsenal): the ship's arsenal of bullets. This will allow the ship to fire bullets.
        """
        
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))
        
        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False
        
        self.arsenal = arsenal

    def _center_ship(self):
        """
        Center the ship on the screen.
        """
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)
        
    def update(self) -> None:
        """
        Update the ship's position based on the movement flags.
        This method is called every frame to update the ship's position and check for collisions.
        It also updates the ship's arsenal (bullets).
        """      
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """
        Update the ship's position based on the movement flags.
        This method checks if the ship is moving left or right and updates its position accordingly.
        It also ensures that the ship does not move off-screen by checking the boundaries of the screen.
        """
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed
        
        self.rect.x = self.x
        
    def draw(self) -> None:
        """
        Draw the ship on the screen.
        This method will be called in the game loop to ensure that the ship is drawn on the screen.
        It will also draw the ship's arsenal (bullets) on the screen.
        """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)
               
    
    def fire(self) -> bool:
        """
        Fire a bullet from the ship's arsenal.
        This method will check if the maximum number of bullets has been reached.

        Returns:
            bool: True if a bullet was successfully fired, False otherwise.
        If the maximum number of bullets has not been reached, a new bullet will be created
        """
        return self.arsenal.fire_bullet()
    
    
    def check_collisions(self, other_group) -> bool:
        """
        Check for collisions between the ship and another group of sprites.
        
        Args:
            other_group (holding class): the group of sprites to check for collisions with.
        This could be a group of aliens, bullets, or any other sprites in the game.
        Returns:
            bool: True if the ship has collided with any of the sprites in the other group.
        """
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False
            
    