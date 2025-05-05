
import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    
class Button:
    """
    A class to create a button in the game.
    This class is responsible for creating a button with a specified message,
    handling its appearance, and checking if it has been clicked.
    """
    def __init__(self, game: 'AlienInvasion', msg: str) -> None:
        """
        Initialize the button attributes.

        Args:
            game (AlienInvasion): _AlienInvasion instance to access game settings and screen._
            msg (str): The message to be displayed on the button.
        """
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.button_font_file, self.settings.button_font_size)
        self.rect = pygame.Rect(0, 0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self.color = self.settings.button_color
        self.text_color = self.settings.button_font_color
        self._prep_msg(msg)
        
    
    def _prep_msg(self, msg: str) -> None:
        """
        Prepare the message to be displayed on the button.
        """
        self.msg_image = self.font.render(msg, True, self.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self) -> None:
        """
        Draw the button and then draw the message.
        """
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
    def check_clicked(self, mouse_pos: tuple[int, int]) -> bool:
        """
        Check if the button is clicked.
        :param mouse_pos: The position of the mouse cursor.
        """
        return self.rect.collidepoint(mouse_pos)
    