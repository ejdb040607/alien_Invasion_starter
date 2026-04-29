'''
Arsenal
Evan Blanton
April 29th, 2026
Contains the Arsenal class which keeps track of the bullets fired by the player.
'''
import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        # self.screen = game.screen
        # self.boundaries = game.screen.get_rect()
        self.bullets = pygame.sprite.Group()

    def update_arsenal(self):
        self.bullets.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def draw(self):
        for bullet in self.bullets:
            bullet.draw_bullet()

    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.bullets.add(new_bullet)
            return True
        return False