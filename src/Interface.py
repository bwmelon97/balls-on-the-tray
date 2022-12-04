from __future__ import annotations 

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np

from utils import Color, PlayerId, drawText
from Gamesound import Sound

sound = Sound()

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

class Scoreboard():
    def __init__(self, player_1: Player, player_2: Player):
        self.player_1 = player_1
        self.player_2 = player_2
        
    def draw(self):

        ## for player_1
        p1_score = self.player_1.score
        pos = np.array([-4.5, 6.4, 10])
        drawText(pos, str(p1_score), Color.LIGHT_BLUE.value)

        ## for player_2
        p2_score = self.player_2.score
        pos = np.array([4.5, 6.4, 10])
        drawText(pos, str(p2_score), Color.RED.value)

        ## Timer
        remain_time = 60
        pos = np.array([0, 6.4, 10])
        drawText(pos, str(remain_time), Color.WHITE.value)
