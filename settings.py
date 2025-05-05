
from pathlib import Path

class Settings:   
    def __init__ (self) -> None:
        """
        Initialize the game settings.
        This method sets the default values for various game parameters such as screen size,
        ship speed, bullet speed, alien speed, and sound file paths.
        It also sets the initial values for the ship and alien fleet.
        """
        # Initialize the game screen size settings and animation frame rate
        self.name: str = "Alien Invasion"
        self.screen_w: int = 1200
        self.screen_h: int = 800
        self.FPS = 60
        
        # Initialize the game background
        """
        self.bg_file source:
        Source URL: https://www.pexels.com/photo/space-background-11657224/
        filename: pexels-photo-11657224.jpeg
        """
        self.bg_file = Path.cwd() / "Assets" / "images" / "pexels-photo-11657224.png"
        
        # Initialize the game ship settings - the player's ship
        """
        self.ship_file source:
        Source URL: https://www.hiclipart.com/free-transparent-background-png-clipart-okdip
        original filename: starship-enterprise-harley-benton-television-fan-art-star-trek.jpg
        """
        self.ship_file = Path.cwd() / "Assets" / "images" / "starship(nobg).png"
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5
        self.starting_ship_amount = 3
        
        # Initialize the game bullet settings - the player's ship bullets
        self.bullet_file = Path.cwd() / "Assets" / "images" / "beam_nobg.png"
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullets_amount = 5
        
        # Initialize the game alien settings - the enemy ship
        """
        self.alien_file source:
        Source URL: https://www.pinterest.com/pin/klingon-bird-of-prey-token-by-thebalzan--527343437621168351/
        original filename: klingon-bird-of-prey-token-by-thebalzan.jpg
        """

        self.alien_file = Path.cwd() / "Assets" / "images" / "enemy_ship_nobg.png"
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 1
        self.fleet_direction = 1
        self.fleet_drop_speed = 40
        
        # Initialize the game sound settings
        """
        self.laser_sound source:
        Source URL: https://pixabay.com/sound-effects/search/laser/
        filename: laser-zap-90575.mp3
        
        self.impact_sound source:
        Source URL: https://pixabay.com/sound-effects/search/explosion/
        filename: explosion-312361.mp3
        """
        self.laser_sound = Path.cwd() / "Assets" / "sound" / "laser-zap-90575.mp3" # Ship firing sound                
        self.impact_sound = Path.cwd() / "Assets" / "sound" / "explosion-312361.mp3" # Impact sound for bullets hitting aliens
        
        
        