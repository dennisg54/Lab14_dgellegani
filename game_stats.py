
import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, game: 'AlienInvasion') -> None:
        """
        Initialize statistics.
        This method initializes the game statistics, including the number of ships left,
        the current score, and the level. It also sets the maximum score to zero.

        Args:
            game (AlienInvasion): The instance of the AlienInvasion game.
        """
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self) -> None:        
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 24:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get("hi_score", 0)
        else:
            self.hi_score = 0
            self.save_scores()
            #save the file
    
    
    def save_scores(self) -> None:
        scores = {
            "hi_score": self.hi_score,
            }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f"File not found: {e}")
                    
                
    def reset_stats(self):
        """
        reset the game statistics to their initial values.
        """
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1
        
    def update(self, collisions: list) -> None:
        """
        update the game statistics based on the collisions with aliens.
        This method updates the score based on the number of collisions with aliens,
        and updates the maximum score if the current score exceeds it.
        It also updates the level of the game.

        Args:
            collisions (list): List of collisions with aliens.
        """
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()

    def _update_max_score(self):
        """
        update the max score if the current score is greater than the max score.
        """
        if self.score > self.max_score:
            self.max_score = self.score              
        
    def _update_hi_score(self):        
        """
        update the hi score if the current score is greater than the hi score.
        """
        if self.score > self.hi_score:
            self.hi_score = self.score
            self.save_scores()            

    def _update_score(self, collisions):
        """
        update the score based on the number of collisions with aliens.
        This method iterates through the list of collisions and adds the alien points to the score.

        Args:
            collisions (list): List of collisions with aliens.
        """
        for alien in collisions:
            self.score += self.settings.alien_points
        # print(f"Score: {self.score}")
            
    def update_level(self) -> None:
        """
        update the game level.
        This method increases the level by 1 and updates the HUD level.
        """
        self.level += 1
        # print(f"Level: {self.level}")
        
    