from __future__ import annotations 

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np
import math

from utils import Color, PlayerId
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
        print(f"Player {self.id.value}'s score is {self.score}")

class Scoreboard():
    def __init__(self,
                 width: float,
                 height: float,
                 depth : float):
        self.width = width
        self.height = height
        self.depth = depth
        self.color = Color.GREEN.value
        
    def draw(self):
        
        cx =8; cy=5; cz =0
        bw = self.width/2; bh = self.height/2; bd = self.depth/2
        ## Spot light 
        lightPosition = [5, 15, 5, 1]
        glLightfv(GL_LIGHT0, GL_POSITION, lightPosition)
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, self.color)
        glBegin(GL_TRIANGLES)
        glNormal3d(0, 1, 0)
        
        # right
        glVertex3f(cx+bw, cy+bh ,cz-bd)
        glVertex3f(cx+bw, cy+bh ,cz+bd)
        glVertex3f(cx+bw, cy-bh ,cz-bd)
        
        glVertex3f(cx+bw, cy-bh ,cz+bd)
        glVertex3f(cx+bw, cy+bh ,cz+bd)
        glVertex3f(cx+bw, cy-bh ,cz-bd)
        
        #left
        glVertex3f(cx-bw, cy+bh ,cz-bd)
        glVertex3f(cx-bw, cy+bh ,cz+bd)
        glVertex3f(cx-bw, cy-bh ,cz-bd)
        
        glVertex3f(cx-bw, cy-bh ,cz+bd)
        glVertex3f(cx-bw, cy+bh ,cz+bd)
        glVertex3f(cx-bw, cy-bh ,cz-bd)
        
        #front
        glVertex3f(cx-bw, cy+bh ,cz-bd)
        glVertex3f(cx-bw, cy-bh ,cz-bd)
        glVertex3f(cx+bw, cy+bh ,cz-bd)
        
        glVertex3f(cx+bw, cy-bh ,cz-bd)
        glVertex3f(cx-bw, cy-bh ,cz-bd)
        glVertex3f(cx+bw, cy+bh ,cz-bd)
        
        #back
        glVertex3f(cx-bw, cy+bh ,cz+bd)
        glVertex3f(cx-bw, cy-bh ,cz+bd)
        glVertex3f(cx+bw, cy+bh ,cz+bd)
        
        glVertex3f(cx+bw, cy-bh ,cz+bd)
        glVertex3f(cx-bw, cy-bh ,cz+bd)
        glVertex3f(cx+bw, cy+bh ,cz+bd)
        
        #up
        glVertex3f(cx-bw, cy+bh ,cz+bd)
        glVertex3f(cx-bw, cy+bh ,cz-bd)
        glVertex3f(cx+bw, cy+bh ,cz-bd)
        
        glVertex3f(cx-bw, cy+bh ,cz+bd)
        glVertex3f(cx+bw, cy+bh ,cz+bd)
        glVertex3f(cx+bw, cy+bh ,cz-bd)
        
        #down
        glVertex3f(cx-bw, cy-bh ,cz+bd)
        glVertex3f(cx-bw, cy-bh ,cz-bd)
        glVertex3f(cx+bw, cy-bh ,cz-bd)
        
        glVertex3f(cx-bw, cy-bh ,cz+bd)
        glVertex3f(cx+bw, cy-bh ,cz+bd)
        glVertex3f(cx+bw, cy-bh ,cz-bd)
        
        glEnd();
        