'''
Upgrades
Evan Blanton
April 29th, 2026
Contains methods for selecting three random upgrades, creating buttons for them, and applying an upgrade when selected.
'''
import random
from typing import TYPE_CHECKING
from button import Button

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Upgrades:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.game_stats = game.game_stats
        self.upgrade_list = ['Larger Bullets', 
                             'Faster Ship',
                             'More Bullets',
                             'Faster Bullets',
                             'Slower Aliens']
        
    def pick_upgrades(self):
        selected_upgrades = random.sample(self.upgrade_list, 3)
        self.upgrade_button1 = Button(self.game, selected_upgrades[0], 'upgrade1')
        self.upgrade_button2 = Button(self.game, selected_upgrades[1], 'upgrade2')
        self.upgrade_button3 = Button(self.game, selected_upgrades[2], 'upgrade3')
    
    def apply_upgrade(self, upgrade_msg):
        if upgrade_msg == 'Larger Bullets':
            self.settings.bullet_h += 32
            self.settings.bullet_w += 10
        elif upgrade_msg == 'Faster Ship':
            self.settings.ship_speed += 2
        elif upgrade_msg == 'More Bullets':
            self.settings.bullet_amount += 2
        elif upgrade_msg == 'Faster Bullets':
            self.settings.bullet_speed += 3
        elif upgrade_msg == 'Slower Aliens':
            self.settings.fleet_speed *= .8
