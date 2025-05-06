
import pygame.font    
class HUD:
    """
    manages and displays various game statistics and visuals such as scores,
    levels, and player lives.
    """        
    def __init__(self, game) -> None:
        """
        The function initializes various attributes related to the game, such as settings, screen, game
        stats, font, and updates scores, life image, and level.
        
        :param game: instance of a game object that is passed to the class constructor. 
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.HUD_font_file, self.settings.HUD_font_size)
        self.padding = 20
        self.update_scores()
        self._setup_life_image()
        self.update_level()
    
    def _setup_life_image(self) -> None:
        """
        loads an image, scales it, and gets its rectangle for use as indicator of lives left
        """
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(self.life_image, (self.settings.ship_w, self.settings.ship_h))
        self.life_rect = self.life_image.get_rect()
    
    def update_scores(self) -> None:
        """
        function updates the maximum score, score, and high score.
        """
        self._update_max_score()
        self._update_score()
        self._update_hi_score()
            
    def _update_score(self) -> None:
        """
        updates the score display in a game interface.
        """
        score_str = f"Score: {self.game_stats.score: ,.0f}"
        self.score_image = self.font.render(score_str, True, self.settings.HUD_font_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.max_score_rect.bottom + self.padding             
        
    def _update_max_score(self) -> None:
        """
        The function renders and positions the maximum score text on the game screen.
        """
        max_score_str = f"Max-Score: {self.game_stats.max_score: ,.0f}"
        self.max_score_image = self.font.render(max_score_str, True, self.settings.HUD_font_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.padding
        
    def _update_hi_score(self) -> None:
        """
        The function updates the high score display in a game interface.
        """
        hi_score_str = f"Hi-Score: {self.game_stats.hi_score: ,.0f}"
        self.hi_score_image = self.font.render(hi_score_str, True, self.settings.HUD_font_color, None)
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.boundaries.centerx, self.padding)        
        
    def update_level(self) -> None:
        """
        function updates the difficulty level display on the game screen with the current level information.
        """
        level_str = f"Level: {self.game_stats.level: ,.0f}"
        self.level_image = self.font.render(level_str, True, self.settings.HUD_font_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.life_rect.bottom + self.padding
        
    def draw_lives(self) -> None:
        """
        The function draws a certain number of life images on the screen based on
        the number of ships left in the game statistics.
        """
        current_x = self.padding
        current_y = self.padding
        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding      
        
    def draw(self) -> None:
        """
        function blits several images onto the screen including high
        score, max score, current score, and level images, as well as calls the `draw_lives` method.
        """
        self.screen.blit(self.hi_score_image, self.hi_score_rect)   
        self.screen.blit(self.max_score_image, self.max_score_rect)   
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.draw_lives()   
        
        