from __future__ import annotations 

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np
import math

from utils import Color


## A ball. A ball has a radius, a color, a position and its velocity. 
class Ball():
    def __init__(self,
                 radius: float,
                 color: list[float],
                 position: np.ndarray):
        self.radius = radius
        self.color = color
        self.position = position
        
        ## properties for movement
        self.v = np.array([0, 0, 0], dtype=np.float64)   # velocity
        

    ## update the position of the ball for each frame
    ## updated position = position + velocity
    def update(self):
        n = np.array([0, 1, 0], dtype=np.float64)               # normal vector of the plain

        g = np.array([0, -9.8, 0], dtype=np.float64) / 3000     # gravity acceleration (dv)
        self.v += g                                             # add g to the v

        ## v can devide into vn and vt (v = vn + vt)
        vn = n * np.dot(self.v, n)                              # n direction vecotr of v
        vt = self.v - vn                                        # vt = v - vn

        dist = np.dot(n, self.position) / (np.linalg.norm(n))   # distance between the center of shpere and the plane
        ## collision detection
        ## if the shpere becomes under the plane, reflect the vn
        if dist < self.radius:
            vn = -vn * 0.7
            self.v = vn + vt

            ## 구를 평면 아래에서 평면과 인접한 위치로 올려놓지 않으면,
            ## vn이 계속 reflect되는 버그가 발생 (순식간에 지면에서 작게 진동)
            self.position = self.position + (n * (self.radius - dist))
            ## self.position = self.position + self.v   # -> 버그 시현
        
        else:
            self.v = vn + vt
            self.position = self.position + self.v
        
        self.render()
        
    ## Render the ball
    def render(self):
        x, y, z = self.position
        glPushMatrix()
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, self.color)
        glTranslated(x, y, z)
        glutSolidSphere(self.radius, 30, 30)
        glPopMatrix()



## A Tray. One corner of the board is (0, 0) and the board stretches out
## along positive x and positive z.  It rests on the xz plane.  I put a
## spotlight at (4, 3, 7).
class Tray():
    def __init__(self, radius: float):
        self.radius = radius

    def create(self):
        self.displayListId = glGenLists(1)
        glNewList(self.displayListId, GL_COMPILE)

        ## Spot light 
        lightPosition = [5, 15, 5, 1]
        glLightfv(GL_LIGHT0, GL_POSITION, lightPosition)

        glBegin(GL_TRIANGLE_FAN)
        glNormal3d(0, 1, 0)

        sharp = 100                 # Sharpness(선명도) of Ellipse
        cycle_degree = 2 * math.pi  # 1 cycle degree = 2 pi
        
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, Color.GREY.value)
        glVertex3f(0, 0, 0)         # centor coordinate
        for i in range(sharp + 1):
            unit_theta = cycle_degree / sharp
            glVertex3f (
                self.radius * math.cos( i * unit_theta ),  # x = r * cos(theta)
                0,
                self.radius * math.sin( i * unit_theta ),  # z = r * sin(theta)
            )
        glEnd()
        glEndList()

    def draw(self):
        glCallList(self.displayListId)
