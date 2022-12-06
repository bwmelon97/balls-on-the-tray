from __future__ import annotations 

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np
import threading

from utils import Color, PlayerId, drawText
from Gamesound import Sound

sound = Sound()
sound.sound_background()

class Player():
    def __init__(self, player_id: PlayerId):
        self.id: PlayerId = player_id
        self.score: int = 0
    def add_score(self, score: int):
        
        if score > 0:
            sound.sound_success2()
        else:
            sound.sound_bomb()
            
        self.score = self.score + score

class Interface():
    def __init__(self, player_1: Player, player_2: Player):
        self.player_1 = player_1
        self.player_2 = player_2

        self.remain_time = 50
        self.is_play = False
        
    def draw_scoreboard(self):

        ## for player_1
        p1_score = self.player_1.score
        pos = np.array([-4.5, 6.4, 10])
        drawText(pos, str(p1_score), Color.LIGHT_BLUE.value)

        ## for player_2
        p2_score = self.player_2.score
        pos = np.array([4.5, 6.4, 10])
        drawText(pos, str(p2_score), Color.RED.value)

        ## Timer
        pos = np.array([0, 6.4, 10])
        drawText(pos, str(self.remain_time), Color.WHITE.value)

    def start(self):
        self.is_play = True
        self.time_tick()

    def time_tick(self):
        if self.is_play == False:
            return
        self.remain_time = self.remain_time - 1
        if self.remain_time == 0:
            sound.sound_end()
        
        if self.remain_time <= 0:
            self.is_play = False
        threading.Timer(1, self.time_tick).start()
