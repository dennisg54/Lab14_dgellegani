import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    
class ShipArsenal:
    """
    Class to manage the ship's arsenal of bullets.
    """
    def __init__(self, game: "AlienInvasion") -> None:
        """
        Initialize the arsenal with the game instance.
        This will allow the arsenal to access game settings and resources.
        The arsenal is a sprite group that will hold all the bullets fired by the ship.
        The bullets will be updated and drawn on the screen as part of the game loop.
        The arsenal will also manage the firing of bullets, ensuring that the maximum number of bullets
        is not exceeded.
        The arsenal will also handle the removal of bullets that have gone off-screen.
        
        Args:
            game (AlienInvasion): The main game instance.             
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()
        
    def update_arsenal(self) -> None:
        """
        Update the position of all bullets in the arsenal.
        This method will be called in the game loop to ensure that all bullets are updated
        and drawn on the screen.
        """
        self.arsenal.update()
        self.remove_bullet_offscreen(self.arsenal)
    
    def remove_bullet_offscreen(self, bullet: Bullet) -> None:
        """
        Remove bullets that have gone off-screen.

        Args:
            bullet (Bullet): The bullet to check for off-screen status.
        This method will check if the bullet's rectangle is off-screen (i.e., if its bottom is less than or equal to 0).
        If it is, the bullet will be removed from the arsenal.
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)
        
    def draw(self) -> None:
        """
        This method will be called in the game loop to ensure that all bullets are drawn
        on the screen.
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()
            
    def fire_bullet(self) -> None:
        """
        Fire a bullet from the ship's arsenal.
        This method will check if the maximum number of bullets has been reached.

        Returns: bool: True if a bullet was successfully fired, False otherwise.
        If the maximum number of bullets has not been reached, a new bullet will be created
        and added to the arsenal. The bullet will be initialized with the ship's current position.
        The bullet will be added to the arsenal, and the method will return True.
        If the maximum number of bullets has been reached, the method will return False.
        The bullet will be created using the Bullet class, which is defined in the bullet module.
        The bullet will be initialized with the game instance, which will allow it to access
        game settings and resources.
    
        """
        if len(self.arsenal) < self.settings.bullets_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False