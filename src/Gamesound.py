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
        self.defeat = pygame.mixer.Sound("sound/jaeap.mp3")
        self.bounce = pygame.mixer.Sound("sound/bounceball.mp3")
        self.bounce_s = pygame.mixer.Sound("sound/bounceball.mp3")
        self.bounce_s.set_volume(0.5)
        self.background.play()

    def gameend(self):
        # while True:
            
        # pygame.display.update()
        self.gameend.play() # play 안에 -1 을 넣으면 무한반복 (즉 다른 작업과 같이 된다.)
        
        # print("hello1")
        # self.sound2.play(-1)
        # time.sleep(5)
        # self.sound2.stop()
        
        # self.sound2.play(-1) # play 안에 -1 을 넣으면 무한반복
        # time.sleep(3)
        # self.sound2.stop()
         
    def bounceball(self):
        self.bounce.play()
    def bounceball_s(self):
        self.bounce_s.play() 
        
    def quit(self):
        pygame.quit()

