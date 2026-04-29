'''
Settings
Evan Blanton
April 29th, 2026
Contains variables for different part of the game such as file paths, sizes, speed, etc.
'''
from pathlib import Path
class Settings:

    def __init__(self):
        # Game
        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        self.fps = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        # Ship
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        
        # Bullet
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'

        # Alien
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'
        self.alien_w = 40
        self.alien_h = 40

        # Fleet
        self.fleet_direction = 1

        # Button
        self.play_button_w = 200
        self.play_button_h = 50
        self.play_button_color =(0, 135, 50)
        self.upgrade_button_w = 300
        self.upgrade_button_h = 75
        self.upgrade_button_color = (128, 0, 128)

        # Font
        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'
        self.padding = 20


    def initialize_dynamic_settings(self):
        # Ship
        self.ship_speed = 5
        self.starting_ship_count = 3

        # Bullet
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_speed = 7
        self.bullet_amount = 5

        # Alien
        self.alien_points = 50

        # Fleet
        self.fleet_speed = 2
        self.fleet_drop_speed = 40

    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale