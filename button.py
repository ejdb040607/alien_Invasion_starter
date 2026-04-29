'''
Button
Evan Blanton
April 29th, 2026
Contains the Button class which is used to create and display the play button.
'''
import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Button:
    def __init__(self, game: 'AlienInvasion', msg, type):
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.padding = self.settings.padding
        self.msg = msg

        if type == 'play':
            self.font = pygame.font.Font(self.settings.font_file, 
                                        self.settings.button_font_size)
            self.rect = pygame.Rect(0, 0, self.settings.play_button_w, self.settings.play_button_h)
            self.color = self.settings.play_button_color

            self.rect.center = self.boundaries.center
        else:
            self.font = pygame.font.Font(self.settings.font_file, 
                                        self.settings.HUD_font_size)
            self.rect = pygame.Rect(0, 0, self.settings.upgrade_button_w, self.settings.upgrade_button_h)
            self.color = self.settings.upgrade_button_color

            if type == 'upgrade1':
                self.rect.midright = (self.boundaries.centerx - (self.settings.upgrade_button_w // 2) - self.padding, 
                                      self.boundaries.centery)
            elif type == 'upgrade2':
                self.rect.center = self.boundaries.center
            else:
                self.rect.midleft = (self.boundaries.centerx + (self.settings.upgrade_button_w // 2) + self.padding,
                                     self.boundaries.centery)

        self._prep_message()

    def _prep_message(self):
        self.msg_image = self.font.render(self.msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    
    def draw(self):
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)