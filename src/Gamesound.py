import pygame
import time


class Sound():
    def __init__(self):
        pygame.init()

        size = [800,600]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("final_project")


        self.background = pygame.mixer.Sound("sound/background.mp3")
        self.background.set_volume(0.2)
        
        self.bounce_h = pygame.mixer.Sound("sound/bounce_heavy.mp3")
        self.bounce_l = pygame.mixer.Sound("sound/bounce_light.mp3")
        
        self.sbounce_h = pygame.mixer.Sound("sound/bounce_heavy.mp3")
        self.sbounce_l = pygame.mixer.Sound("sound/bounce_light.mp3")
        self.sbounce_h.set_volume(0.1)
        self.sbounce_l.set_volume(0.1)
        
        self.bomb = pygame.mixer.Sound("sound/bomb.mp3")
        self.success2 = pygame.mixer.Sound("sound/success2.mp3")
        
        self.end = pygame.mixer.Sound("sound/end.mp3")
        self.fail = pygame.mixer.Sound("sound/fail.mp3")
        
        
        self.background.play(-1)

         
    def sound_bounce_h(self):
        self.bounce_h.play()
    def sound_bounce_l(self):
        self.bounce_l.play()
        
    def small_sound_bounce_h(self):
        self.sbounce_h.play()
    def small_sound_bounce_l(self):
        self.sbounce_l.play()
        
    def sound_bomb(self):
        self.bomb.play()
    def sound_success2(self):
        self.success2.play()
    
    def sound_end(self):
        self.end.play()
    def sound_fail(self):
        self.fail.play()
        
    def quit(self):
        pygame.quit()

