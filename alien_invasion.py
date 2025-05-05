import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import ShipArsenal
from alien_fleet import AlienFleet
from time import sleep
from button import Button

class AlienInvasion:
    """
    Main class for the Alien Invasion game.
    This class is responsible for initializing the game, creating resources,
    and managing the game loop.  
    """
    def __init__(self) -> None:
        """
        Initialize the game and create resources.
        This includes setting up the screen, loading images, and initializing sounds.
        The game starts with a ship and an alien fleet.
        """           
        
        # Initialize pygame and create resources
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()
        self.game_stats = GameStats(self.settings.starting_ship_amount)
        
        # Create the game screen
        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)
        
        # Load the background image and scale it to fit the screen
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))
                
        self.running = True
        self.clock = pygame.time.Clock()
        
        # Initialize game sounds
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound) # Ship firing sound
        self.laser_sound.set_volume(0.8)
        
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound) # Impact sound for bullets hitting aliens
        self.impact_sound.set_volume(0.8)       

        ## Initialize the ship and alien fleet
        self.ship = Ship(self, ShipArsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.createFleet()
        
        self.play_button = Button(self, "Start Battle")
        self.game_active = False


    def run_game(self) -> None:
        """
        Main loop of the game. This method handles the game events, updates the game state,
        and renders the game screen.
        """
        
        # Main loop of the game
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()            
            self._update_screen()
            self.clock.tick(self.settings.FPS)
    
    def _check_collisions(self) -> None:
        """
        Check for collisions between the ship, alien fleet, and bullets.
        This method checks for collisions between the ship and the alien fleet,
        the alien fleet and the screen bottom, and between bullets and aliens.
        If a collision is detected, the game status is updated accordingly.
        """
        # check collisions for ship
        if self.ship.check_collisions(self.alien_fleet.fleet):
           self._check_game_status()         
        
        # check collisions for aliens and screen bottom
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()
        
        # check collisions for bullets and aliens           
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)        
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(750)
        
        # check if all aliens are destroyed
        if self.alien_fleet.check_destroyed_status():
            self._reset_level()         
    
    
    def _check_game_status(self) -> None:
        """
        Check the game status and update the game state accordingly.
        If the ship collides with an alien or the fleet reaches the bottom of the screen,
        the round is over and a player ship is lost. If the ship has no lives left, the game ends.
        """
        if self.game_stats.ships_left  > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(1)
        else:
            self.game_active = False
                        
           
    def _reset_level(self) -> None:
        """
        Reset the game level by removing all bullets and aliens, and creating a new fleet.
        """
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.createFleet()
        
    def restart_game(self) -> None:
        """
        Restart the game by resetting the game stats and creating a new fleet.
        """
        # setting up dynamic Settings
        # reset game stats
        # update HUD scores
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False) 
        
        
    def _update_screen(self):
        """
        Update the screen with the latest game state.
        This method draws the background, ship, and alien fleet on the screen.
        """
        # Update the screen with the latest game state
        self.screen.blit(self.bg, (0, 0))
        self.alien_fleet.draw()
        
        if not self.game_active:
            self.play_button.draw_button()
            pygame.mouse.set_visible(True)
        
        self.ship.draw()        
        pygame.display.flip()


    def _check_events(self) -> None:
        """
        Check for keyboard and mouse events.
        This method handles key presses and releases, as well as quitting the game.
        """       
        # Check for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)                                
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()
                

    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos) and not self.game_active:
            self.restart_game()
            
            
    def _check_keyup_events(self, event) -> None:
        """
        Check for key releases and update the ship's movement status accordingly.
        This method handles the release of the right and left arrow keys, stopping the ship's movement.
        
        Args:
            event (key release): The event object containing information about the key release.
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    
    def _check_keydown_events(self, event) -> None:
        """
        Check for key presses and update the ship's movement status accordingly.
        This method handles the pressing of the right and left arrow keys, firing bullets,
        and quitting the game.

        Args:
            event (key press): The event object containing information about the key press.
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
               self.laser_sound.play()
               self.laser_sound.fadeout(500)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()   
    
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

    

